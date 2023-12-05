"""
Perform simulation conditioned on the windows structure according to
prior generators and models defined hereafter. The observed set of
statistics is used to get the list of stats. For each chunk of
simulations and for each model, two files are populated: one with the
values of parameters (defined by the model) and one with the values of
statistics.
"""

import egglib, lzmp, math, stats, re, random, pathlib, yaml

# load configuration
with open('params.yml') as f:
    cfg = yaml.load(f, yaml.Loader)

models = {} # models are stored in a code-index dictionary

# main function
def main():
    """
    Run the specified list of models
    """

    pool = lzmp.Pool(max_threads=cfg['simul']['nthreads'])
    seed = egglib.random.get_seed() # master seed
    mlist = ['M40', 'M41', 'M44'] # list if models
    t = 0
    c = 0

    pathlib.Path('simuls').mkdir(exist_ok=True) # ensures the output dir exists
    for rep in range(cfg['simul']['nbatch']):
        for name in mlist:
            t += 1
            stem = f'simuls/{name}-{rep+1:03d}'
            p = pathlib.Path(stem + '_p.txt')
            if not p.is_file(): # doesn't run a chunk that has been started
                seed += 1
                m = models[name](name) # create an instance of model
                pool.add(m.job, [(stem, cfg['simul']['szbatch'], seed)])
                print(stem)
                c += 1
    print(f'total: {t} - to do: {c}')
    pool.run(shuffle=False)

class Priors:
    """
    class holding functions to draw parameters from priors (as a class
    just for cosmetic)
    """

    def __init__(self):
        raise AttributeError('instanciation not available')

    @staticmethod
    def uniform_draw(mini, maxi):
        return egglib.random.uniform_closed()*(maxi-mini)+mini

    @staticmethod
    def loguniform_draw(mini, maxi):
        mini = math.log(mini)
        maxi = math.log(maxi)
        return math.exp(egglib.random.uniform_open()*(maxi-mini)+mini)

    @staticmethod
    def normal_draw(mean, stdev, mini, maxi):
        return egglib.random.normal_bounded(mean, stdev, mini, maxi)

    @staticmethod
    def lognormal_draw(mean, stdev):
        return math.exp(egglib.random.normal()*stdev + mean)

def maf(aln):
    """
    helper function to remove sites based on MAF
    """
    keep = []
    for i in range(aln.ls):
        site = aln.column(i)
        if min(site.count(0), site.count(1))/aln.ns >= cfg['MAF']:
            keep.append(i)
    return aln.extract(keep)

class Model:
    """
    base of simulating classes
    """
    def __init__(self, name):
        """
        get number of windows, number of sites, and missing data rates
        """
        self.name = name
        with open('windows.yml') as f:
            wins = yaml.load(f, yaml.Loader)
        self.nwindows = wins['windows'][5]['num']
        self.L = [None] * self.nwindows
        self.miss = [None] * self.nwindows
        for i in range(self.nwindows):
            with open(f'windows/infos/{i+1:>03}.txt') as f:
                self.L[i] = int(re.match('LG=contig_\d+ first=\d+ last=\d+ L=(\d+)', f.readline()).group(1))
                self.miss[i] = list(map(float, f))
        self.setup()
        self.set_events()

    def job(self, dest, num, seed):
        """
        run one simulation, making use of functions defined in
        subclasses
        """
        egglib.random.set_seed(seed)
        struct = egglib.struct_from_samplesizes([cfg['N_NA'], cfg['N_BR'], cfg['N_EU']], outgroup=1)
        cstats = stats.Cstats()

        # get the list of stats/params
        self.draw()
        keys_p = sorted(self.params)
        with open('obs.txt') as f:
            keys_s = [line.split()[0] for line in f]

        # run simulations
        self.coal.simul() # needed to make the alphabet alphabet
        self.coal.align.alphabet.add_missing(-1) # this is non-canonical
        sites = []
        c = 0
        cache = 0
        with open(dest + '_p.txt', 'w') as f1:
            with open(dest + '_s.txt', 'w') as f2:
                f1.write(' '.join(keys_p) + '\n')
                f2.write(' '.join(keys_s) + '\n')
                while c < num:
                    self.draw()
                    self.update()
                    cstats.init()
                    for i in range(self.nwindows):
                        self.coal.params['theta'] = self.params['theta'] * self.L[i]
                        self.coal.params['recomb'] = self.params['rho'] * self.L[i]
                        try:
                            for aln in self.coal.iter_simul(1):
                                aln = maf(aln)

                                # add an outgroup sample
                                otg = [int(egglib.random.bernoulli(self.params['m'])) for _ in range(aln.ls)]
                                aln.add_sample('outgroup', otg)

                                # insert missing data
                                for j, p in enumerate(self.miss[i]):
                                    if p > 0:
                                        n = int(round(p * aln.ls))
                                        idx = list(range(aln.ls))
                                        random.shuffle(idx)
                                        miss = idx[:n]
                                        for k in miss:
                                            aln.set(j, k, -1)
                                cstats.process(aln, self.L[i])
                        except Exception as e:
                            with open(f'error-{self.name}-{seed}.txt', 'w') as f:
                                f.write('EXCEPTION OCCURRED\n')
                                f.write(f'type: {type(e)}\n')
                                f.write(f'message: {e}\n')
                                f.write(f'model: {self.name}\n')
                                f.write(f'seed: {seed}\n')
                                for k in self.params:
                                    f.write(f'{k}={self.params[k]}\n')
                                f.write(self.coal.params.summary())
                            return
                    res = cstats.compute()
                    if res:
                        c += 1
                        if c%cfg['simul']['thin']==0: print(f'{dest}: {c}/{num}')
                        f1.write(' '.join(map(str, (self.params[k] for k in keys_p))) + '\n')
                        f2.write(' '.join(map(str, (res[k] for k in keys_s))) + '\n')

    def setup(self):
        """
        setup model (must be defined in subclasses)
        """
        raise NotImplemented

    def set_events(self):
        """
        setup event order (must be defined in subclasses)
        """
        raise NotImplemented

    def draw(self):
        """
        draw parameters (must be defined in subclasses)
        """
        raise NotImplemented

    def update(self):
        """
        apply parameters (must be defined in subclasses)
        """
        raise NotImplemented

class ThreePop(Model):
    """
    intermediate base class for models with three pop (no ghost
    Mesoamerica population)
    """

    def setup(self):
        self.coal = egglib.coalesce.Simulator(num_pop=3, num_chrom=[cfg['N_NA'], cfg['N_BR'], cfg['N_EU']], num_mut=0)

    def draw(self):
        self.params = {
            'theta': Priors.loguniform_draw(0.00001, 0.001),
            'rho': Priors.loguniform_draw(0.00001, 0.001),
            'N_BR': Priors.normal_draw(1, 1, 0.25, 4),
            'N_EU': Priors.normal_draw(1, 1, 0.25, 4),
            'T1': Priors.normal_draw(0.1, 0.2, 0, 1),
            'T2': Priors.normal_draw(0.1, 0.1, 0, 1),
            'S1': Priors.normal_draw(0.1, 0.3, 0, 1),
            'S2': Priors.normal_draw(0.1, 0.3, 0, 1),
            'M_NA_BR': Priors.normal_draw(0.1, 0.2, 0, 1.5),
            'M_BR_NA': Priors.normal_draw(0.1, 0.2, 0, 1.5),
            'M_NA_EU': Priors.normal_draw(0.1, 0.2, 0, 1.5),
            'M_EU_NA': Priors.normal_draw(0.1, 0.2, 0, 1.5),
            'M_BR_EU': Priors.normal_draw(0.1, 0.2, 0, 1.5),
            'M_EU_BR': Priors.normal_draw(0.1, 0.2, 0, 1.5),
            'm': Priors.normal_draw(0.1, 0.2, 0, 1)
            # note: in M3D: delete T2 and draw S3 and N_ANC
        }

    def update(self):
        # overruled in M3D
        self.coal.params['N'] = [1, self.params['N_BR'], self.params['N_EU']]
        self.coal.params['migr_matrix'] = [[None, self.params['M_NA_BR'], self.params['M_NA_EU']],
                                           [self.params['M_BR_NA'], None, self.params['M_BR_EU']],
                                           [self.params['M_EU_NA'], self.params['M_EU_BR'], None]]
        self.coal.params['events'].update(0, T=self.params['T1'], S=self.params['S1'])
        self.coal.params['events'].update(1, T=self.params['T1']+1e-6)
        self.coal.params['events'].update(2, T=self.params['T1']+self.params['T2']+2e-6, S=self.params['S2'])
        self.coal.params['events'].update(3, T=self.params['T1']+self.params['T2']+3e-6)

class M(ThreePop):
    """
    EU-->NA
      -->BR
    """
    def set_events(self):
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=1)
        self.coal.params.add_event('merge', T=0, src=1, dst=2)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=0)
        self.coal.params.add_event('merge', T=0, src=0, dst=2)
models['M31'] = M

class M(ThreePop):
    """
    EU-->BR
      -->NA
    """
    def set_events(self):
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=0)
        self.coal.params.add_event('merge', T=0, src=0, dst=2)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=1)
        self.coal.params.add_event('merge', T=0, src=1, dst=2)
models['M3B'] = M

class M(ThreePop):
    """
    NA-->EU
      -->BR
    """
    def set_events(self):
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=1)
        self.coal.params.add_event('merge', T=0, src=1, dst=0)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=2)
        self.coal.params.add_event('merge', T=0, src=2, dst=0)
models['M32'] = M

class M(ThreePop):
    """
    NA-->BR
      -->EU
    """
    def set_events(self):
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=2)
        self.coal.params.add_event('merge', T=0, src=2, dst=0)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=1)
        self.coal.params.add_event('merge', T=0, src=1, dst=0)
models['M33'] = M

class M(ThreePop):
    """
    BR-->NA
      -->EU
    """
    def set_events(self):
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=2)
        self.coal.params.add_event('merge', T=0, src=2, dst=1)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=0)
        self.coal.params.add_event('merge', T=0, src=0, dst=1)
models['M34'] = M

class M(ThreePop):
    """
    BR-->EU
      -->NA
    """
    def set_events(self):
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=0)
        self.coal.params.add_event('merge', T=0, src=0, dst=1)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=2)
        self.coal.params.add_event('merge', T=0, src=2, dst=1)
models['M3C'] = M

class M(ThreePop):
    """
    NA --> EU --> BR
    """
    def set_events(self):
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=1)
        self.coal.params.add_event('merge', T=0, src=1, dst=2)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=2)
        self.coal.params.add_event('merge', T=0, src=2, dst=0)
models['M35'] = M

class M(ThreePop):
    """
    NA --> BR --> EU
    """
    def set_events(self):
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=2)
        self.coal.params.add_event('merge', T=0, src=2, dst=1)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=1)
        self.coal.params.add_event('merge', T=0, src=1, dst=0)
models['M36'] = M

class M(ThreePop):
    """
    EU --> NA --> BR
    """
    def set_events(self):
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=1)
        self.coal.params.add_event('merge', T=0, src=1, dst=0)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=0)
        self.coal.params.add_event('merge', T=0, src=0, dst=2)
models['M37'] = M

class M(ThreePop):
    """
    EU --> BR --> NA
    """
    def set_events(self):
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=0)
        self.coal.params.add_event('merge', T=0, src=0, dst=1)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=1)
        self.coal.params.add_event('merge', T=0, src=1, dst=2)
models['M38'] = M

class M(ThreePop):
    """
    BR --> NA --> EU
    """
    def set_events(self):
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=2)
        self.coal.params.add_event('merge', T=0, src=2, dst=0)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=0)
        self.coal.params.add_event('merge', T=0, src=0, dst=1)
models['M39'] = M

class M(ThreePop):
    """
    BR --> EU --> NA
    """
    def set_events(self):
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=0)
        self.coal.params.add_event('merge', T=0, src=0, dst=2)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=2)
        self.coal.params.add_event('merge', T=0, src=2, dst=1)
models['M3A'] = M

class M(ThreePop):
    """
    ANC
     -->NA
     -->BR
     -->EU
    simultaneous split
    """
    def set_events(self):
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=0)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=1)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=2)
        self.coal.params.add_event('merge', T=0, src=1, dst=0)
        self.coal.params.add_event('merge', T=0, src=2, dst=0)
        self.coal.params.add_event('size', T=0, idx=0, N=1)

    def draw(self):
        super().draw()
        del self.params['T2']
        self.params['S3'] = Priors.normal_draw(0.1, 0.3, 0, 1)
        self.params['N_ANC'] = Priors.normal_draw(1, 1, 0.25, 4)

    def update(self):
        self.coal.params['N'] = [1, self.params['N_BR'], self.params['N_EU']]
        self.coal.params['migr_matrix'] = [[None, self.params['M_NA_BR'], self.params['M_NA_EU']],
                                           [self.params['M_BR_NA'], None, self.params['M_BR_EU']],
                                           [self.params['M_EU_NA'], self.params['M_EU_BR'], None]]
        self.coal.params['events'].update(0, T=self.params['T1'], S=self.params['S1'])
        self.coal.params['events'].update(1, T=self.params['T1'], S=self.params['S2'])
        self.coal.params['events'].update(2, T=self.params['T1'], S=self.params['S3'])
        self.coal.params['events'].update(3, T=self.params['T1']+1e-6)
        self.coal.params['events'].update(4, T=self.params['T1']+1e-6)
        self.coal.params['events'].update(5, T=self.params['T1']+1e-6, N=self.params['N_ANC'])
models['M3D'] = M

class FourPop(Model):
    """
    intermediate base class for models with pop pop (with a ghost
    population representing Mesoamerica)
    """

    def setup(self):
        self.coal = egglib.coalesce.Simulator(num_pop=4, num_chrom=[cfg['N_NA'], cfg['N_BR'], cfg['N_EU'], 0], num_mut=0)

    def draw(self):
        self.params = {
            'theta': Priors.loguniform_draw(0.00001, 0.001),
            'rho': Priors.loguniform_draw(0.00001, 0.001),
            'N_NA': Priors.normal_draw(1, 1, 0.25, 4),
            'N_BR': Priors.normal_draw(1, 1, 0.25, 4),
            'N_EU': Priors.normal_draw(1, 1, 0.25, 4),
            'T1': Priors.normal_draw(0.1, 0.2, 0, 1),
            'T2': Priors.normal_draw(0.1, 0.1, 0, 1),
            'T3': Priors.normal_draw(0.1, 0.1, 0, 1),
            'S1': Priors.normal_draw(0.1, 0.3, 0, 1),
            'S2': Priors.normal_draw(0.1, 0.3, 0, 1),
            'S3': Priors.normal_draw(0.1, 0.3, 0, 1),
            'M_MA_NA': Priors.normal_draw(0.1, 0.2, 0, 1.5),
            'M_NA_MA': Priors.normal_draw(0.1, 0.2, 0, 1.5),
            'M_MA_BR': Priors.normal_draw(0.1, 0.2, 0, 1.5),
            'M_BR_MA': Priors.normal_draw(0.1, 0.2, 0, 1.5),
            'M_NA_EU': Priors.normal_draw(0.1, 0.2, 0, 1.5),
            'M_EU_NA': Priors.normal_draw(0.1, 0.2, 0, 1.5),
            'M_BR_EU': Priors.normal_draw(0.1, 0.2, 0, 1.5),
            'M_EU_BR': Priors.normal_draw(0.1, 0.2, 0, 1.5),
            'm': Priors.normal_draw(0.1, 0.2, 0, 1)
        }

    def update(self):
        self.coal.params['N'] = [self.params['N_NA'], self.params['N_BR'], self.params['N_EU'], 1]
        self.coal.params['migr_matrix'] = [[None, 0, self.params['M_NA_EU'], self.params['M_NA_MA']],
                                           [0, None, self.params['M_BR_EU'], self.params['M_BR_MA']],
                                           [self.params['M_EU_NA'], self.params['M_EU_BR'], None, 0],
                                           [self.params['M_MA_NA'], self.params['M_MA_BR'], 0, None]]
        self.coal.params['events'].update(0, T=self.params['T1'], S=self.params['S1'])
        self.coal.params['events'].update(1, T=self.params['T1']+1e-6)
        self.coal.params['events'].update(2, T=self.params['T1']+self.params['T2']+2e-6, S=self.params['S2'])
        self.coal.params['events'].update(3, T=self.params['T1']+self.params['T2']+3e-6)
        self.coal.params['events'].update(4, T=self.params['T1']+self.params['T2']+self.params['T3']+4e-6, S=self.params['S3'])
        self.coal.params['events'].update(5, T=self.params['T1']+self.params['T2']+self.params['T3']+5e-6)

class M(FourPop):
    """
    MA
     -->NA
     -->BR
     -->EU
    """
    def set_events(self):
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=0)
        self.coal.params.add_event('merge', T=0, src=0, dst=3)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=1)
        self.coal.params.add_event('merge', T=0, src=1, dst=3)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=2)
        self.coal.params.add_event('merge', T=0, src=2, dst=3)

    def draw(self):
        super().draw()
        self.params['T2'] = 0
        self.params['T3'] = 0
models['M40'] = M

class M(FourPop):
    """
    MA-->NA
      ---->BR
      ------>EU
    """
    def set_events(self):
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=0)
        self.coal.params.add_event('merge', T=0, src=0, dst=3)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=1)
        self.coal.params.add_event('merge', T=0, src=1, dst=3)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=2)
        self.coal.params.add_event('merge', T=0, src=2, dst=3)

    def draw(self):
        super().draw()
        self.params['T2'] = 0
        self.params['T3'] = 0
models['M41'] = M

class M(FourPop):
    """
    MA-->NA-->BR
           ---->EU
    """
    def set_events(self):
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=2)
        self.coal.params.add_event('merge', T=0, src=2, dst=0)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=3)
        self.coal.params.add_event('merge', T=0, src=1, dst=0)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=0)
        self.coal.params.add_event('merge', T=0, src=0, dst=3)
models['M44'] = M


del M
if __name__ == '__main__':
    main()
