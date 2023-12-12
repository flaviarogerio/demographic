"""
If executed: perform simulations. If imported: expose prior generators
(in the dictionary priors) and models (in the dictionary models).

* requires:
    * sites.txt, sites.yml
    * stats.py (class Cstats)
* generates (if executed):
    * simuls/*
    * error-* files in case an exception is caught
"""

import egglib, lzmp, math, stats, re, random, pathlib, yaml

src = 'sites.txt'
dst = 'simuls'

### load configuration #################################################
with open('params.yml') as f:
    cfg = yaml.load(f, yaml.Loader)
with open('sites.yml') as f:
    ns = yaml.load(f, yaml.Loader)['ns']

# initialize the dictionary of models ##################################
def load():
    global models_list, models_map, model_names
    models_list = [M31, M3B, M32, M33,
                   M34, M3C, M35, M36,
                   M37, M38, M39, M3A,
                   M3D, M40, M41, M44]
    models_map = {m.__name__: m for m in models_list}
    model_names = [m.__name__ for m in models_list]

# main function (run only if the module is executed) ###################
def main():
    pool = lzmp.Pool(max_threads=cfg['nthreads'])
    seed = egglib.random.get_seed() # master seed
    mlist = cfg['simul']['models'] # list of models to run
    if len(mlist) == 0: mlist = model_names
    t = 0
    c = 0
    pathlib.Path(dst).mkdir(exist_ok=True) # ensures the output dir exists
    for rep in range(cfg['simul']['first_batch'], cfg['simul']['first_batch']+cfg['simul']['nbatch']+1):
        for name in mlist:
            t += 1
            fname = f'{dst}/{name}-{rep:03d}.txt'
            p = pathlib.Path(fname)
            if cfg['simul']['overwrite'] or not p.is_file(): # doesn't run a chunk that has been started (unless overwrite is on)
                seed += 1
                m = models_map[name]() # create an instance of model
                pool.add(m.job, [(fname, cfg['simul']['szbatch'], cfg['simul']['thin'], seed)])
                c += 1
    print(f'total: {t} - skipped: {t-c} - to do: {c}')
    pool.run(shuffle=False)

# dictionary of prior generators #######################################
class Uniform:
    def __init__(self, mini, maxi):
        self.mini = mini
        self.maxi = maxi
    def __call__(self):
        return egglib.random.uniform_closed()*(self.maxi-self.mini)+self.mini

class Loguniform:
    def __init__(self, mini, maxi):
        self.mini = math.log(mini)
        self.maxi = math.log(maxi)
    def __call__(self):
        return math.exp(egglib.random.uniform_open()*(self.maxi-self.mini)+self.mini)

class Normal:
    def __init__(self, mean, stdev, mini, maxi):
        self.m = mean
        self.sd = stdev
        self.mn = mini
        self.mx = maxi
    def __call__(self):
        return egglib.random.normal_bounded(self.m, self.sd, self.mn, self.mx)

class Lognormal:
    def __init__(self, mean, stdev):
        self.m = mean
        self.sd = stdev
    def __call__(self):
        return math.exp(egglib.random.normal()*self.sd + self.m)

class Zero:
    def __call__(self):
        return 0

priors = {
    'uniform': Uniform,
    'loguniform': Loguniform,
    'normal': Normal,
    'zognormal': Lognormal,
    'zero': Zero
}
def get_prior(args):
    return priors[args[0]](*args[1:])

# hierarchy of classes implementing models #############################
class Model:
    """
    Base of simulating classes. All methods are defined here although
    some are implemented or reimplemented in sub-classes. In addition,
    all model classes must have a params attribute as a dictionary
    mapping parameter names to generators.

    The constructor import site configuration from sites.txt.
    """
    def __init__(self):
        self.sites = []
        with open(src) as f:
            for line in f:
                ctg, pos, NA, BR, EU, site = line.split()
                self.sites.append((int(NA), int(BR), int(EU)))
        self.alph = egglib.Alphabet('int', [0, 1], [-1])
        self.cstats = stats.Cstats()

    def job(self, dest, num, thin, seed):
        """
        Run one simulation batch. Return the number of skipped.
        """
        keys_pars = list(self.params)
        keys_stats = list(stats.Cstats().results())
        egglib.random.set_seed(seed)

        # run simulations
        with open(dest, 'w') as f:
            f.write(' '.join(keys_pars) + ' ' + ' '.join(keys_stats) + '\n')
            for _ in range(num):
                try:
                    params, res = self.simul()
                except Exception as e:
                    if not cfg['simul']['intercept']:
                        raise
                    with open(f'error-{type(self).__name__}-{seed}.txt', 'w') as errf:
                        errf.write('EXCEPTION OCCURRED\n')
                        errf.write(f'type: {type(e)}\n')
                        errf.write(f'message: {e}\n')
                        errf.write(f'model: {type(self).__name__}\n')
                        errf.write(f'seed: {seed}\n')
                        errf.write(self.coal.params.summary())
                    return

                if (_+1)%thin==0:
                    print(f'{dest}: {_+1}/{num}')
                    f.flush()
                res = {k: (0 if v is None else v) for k,v in res.items()}
                f.write(' '.join(map(str, (params[k] for k in keys_pars))) + ' ' +
                        ' '.join(map(str, (res[k] for k in keys_stats))) + '\n')

    def simul(self):
        """
        perform a single simulation round
        """
        params = self.draw()
        self.update(params)
        site = egglib.Site()
        for NA, BR, EU in self.sites:
            self.coal.params['num_chrom'][0] = NA
            self.coal.params['num_chrom'][1] = BR
            self.coal.params['num_chrom'][2] = EU
            while True:
                for aln in self.coal.iter_simul(1):
                    # ensure the maf is sufficient
                    array = aln.column(0)
                    if min(array.count(0), array.count(1))/sum([NA, BR, EU]) < cfg['maf']:
                        break
                else:
                    # add an outgroup sample
                    array = (array[:NA] + [-1] * (ns['NA']-+NA) +
                            array[NA:NA+BR] + [-1] * (ns['BR']-BR) +
                            array[NA+BR:] + [-1] * (ns['EU']-EU))
                    array.append(int(egglib.random.bernoulli(params['m'])))
                    site.from_list(array, self.alph)
                    self.cstats.process(site)
                    break
        return params, self.cstats.results()

    def draw(self):
        """
        draw parameters
        """
        return {par: gen() for (par, gen) in self.params.items()}

    def update(self, pars):
        """
        apply parameters (must be defined in subclasses)
        """
        raise NotImplemented

class ThreePop(Model):
    """
    intermediate base class for models with three pop (no ghost
    Mesoamerica population)
    """

    def __init__(self):
        super().__init__()
        self.coal = egglib.coalesce.Simulator(num_pop=3, num_chrom=[0, 0, 0], num_mut=1)
        self.params = {
            'N_BR': get_prior(cfg['simul']['priors']['N']),
            'N_EU': get_prior(cfg['simul']['priors']['N']),
            'T1': get_prior(cfg['simul']['priors']['T']),
            'T2': get_prior(cfg['simul']['priors']['T']),
            'S1': get_prior(cfg['simul']['priors']['S']),
            'S2': get_prior(cfg['simul']['priors']['S']),
            'M_NA_BR': get_prior(cfg['simul']['priors']['M']),
            'M_BR_NA': get_prior(cfg['simul']['priors']['M']),
            'M_NA_EU': get_prior(cfg['simul']['priors']['M']),
            'M_EU_NA': get_prior(cfg['simul']['priors']['M']),
            'M_BR_EU': get_prior(cfg['simul']['priors']['M']),
            'M_EU_BR': get_prior(cfg['simul']['priors']['M']),
            'm': get_prior(cfg['simul']['priors']['m'])
            # note: in M3D: delete T2 and draw S3 and N_AN
        }

    def update(self, pars):
        # overruled in M3D
        self.coal.params['N'] = [1, pars['N_BR'], pars['N_EU']]
        self.coal.params['migr_matrix'] = [[None, pars['M_NA_BR'], pars['M_NA_EU']],
                                           [pars['M_BR_NA'], None, pars['M_BR_EU']],
                                           [pars['M_EU_NA'], pars['M_EU_BR'], None]]
        self.coal.params['events'].update(0, T=pars['T1'], S=pars['S1'])
        self.coal.params['events'].update(1, T=pars['T1']+1e-6)
        self.coal.params['events'].update(2, T=pars['T1']+pars['T2']+2e-6, S=pars['S2'])
        self.coal.params['events'].update(3, T=pars['T1']+pars['T2']+3e-6)

class M31(ThreePop):
    """
    EU-->NA
      -->BR
    """
    def __init__(self):
        super().__init__()
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=1)
        self.coal.params.add_event('merge', T=0, src=1, dst=2)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=0)
        self.coal.params.add_event('merge', T=0, src=0, dst=2)

class M3B(ThreePop):
    """
    EU-->BR
      -->NA
    """
    def __init__(self):
        super().__init__()
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=0)
        self.coal.params.add_event('merge', T=0, src=0, dst=2)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=1)
        self.coal.params.add_event('merge', T=0, src=1, dst=2)

class M32(ThreePop):
    """
    NA-->EU
      -->BR
    """
    def __init__(self):
        super().__init__()
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=1)
        self.coal.params.add_event('merge', T=0, src=1, dst=0)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=2)
        self.coal.params.add_event('merge', T=0, src=2, dst=0)

class M33(ThreePop):
    """
    NA-->BR
      -->EU
    """
    def __init__(self):
        super().__init__()
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=2)
        self.coal.params.add_event('merge', T=0, src=2, dst=0)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=1)
        self.coal.params.add_event('merge', T=0, src=1, dst=0)

class M34(ThreePop):
    """
    BR-->NA
      -->EU
    """
    def __init__(self):
        super().__init__()
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=2)
        self.coal.params.add_event('merge', T=0, src=2, dst=1)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=0)
        self.coal.params.add_event('merge', T=0, src=0, dst=1)

class M3C(ThreePop):
    """
    BR-->EU
      -->NA
    """
    def __init__(self):
        super().__init__()
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=0)
        self.coal.params.add_event('merge', T=0, src=0, dst=1)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=2)
        self.coal.params.add_event('merge', T=0, src=2, dst=1)

class M35(ThreePop):
    """
    NA --> EU --> BR
    """
    def __init__(self):
        super().__init__()
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=1)
        self.coal.params.add_event('merge', T=0, src=1, dst=2)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=2)
        self.coal.params.add_event('merge', T=0, src=2, dst=0)

class M36(ThreePop):
    """
    NA --> BR --> EU
    """
    def __init__(self):
        super().__init__()
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=2)
        self.coal.params.add_event('merge', T=0, src=2, dst=1)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=1)
        self.coal.params.add_event('merge', T=0, src=1, dst=0)

class M37(ThreePop):
    """
    EU --> NA --> BR
    """
    def __init__(self):
        super().__init__()
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=1)
        self.coal.params.add_event('merge', T=0, src=1, dst=0)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=0)
        self.coal.params.add_event('merge', T=0, src=0, dst=2)

class M38(ThreePop):
    """
    EU --> BR --> NA
    """
    def __init__(self):
        super().__init__()
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=0)
        self.coal.params.add_event('merge', T=0, src=0, dst=1)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=1)
        self.coal.params.add_event('merge', T=0, src=1, dst=2)

class M39(ThreePop):
    """
    BR --> NA --> EU
    """
    def __init__(self):
        super().__init__()
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=2)
        self.coal.params.add_event('merge', T=0, src=2, dst=0)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=0)
        self.coal.params.add_event('merge', T=0, src=0, dst=1)

class M3A(ThreePop):
    """
    BR --> EU --> NA
    """
    def __init__(self):
        super().__init__()
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=0)
        self.coal.params.add_event('merge', T=0, src=0, dst=2)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=2)
        self.coal.params.add_event('merge', T=0, src=2, dst=1)

class M3D(ThreePop):
    """
    ANC
     -->NA
     -->BR
     -->EU
    simultaneous split
    """
    def __init__(self):
        super().__init__()
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=0)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=1)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=2)
        self.coal.params.add_event('merge', T=0, src=1, dst=0)
        self.coal.params.add_event('merge', T=0, src=2, dst=0)
        self.coal.params.add_event('size', T=0, idx=0, N=1)
        del self.params['T2']
        self.params['N_AN'] = get_prior(cfg['simul']['priors']['N'])
        self.params['S3'] = get_prior(cfg['simul']['priors']['S'])

    def update(self, pars):
        self.coal.params['N'] = [1, pars['N_BR'], pars['N_EU']]
        self.coal.params['migr_matrix'] = [[None, pars['M_NA_BR'], pars['M_NA_EU']],
                                           [pars['M_BR_NA'], None, pars['M_BR_EU']],
                                           [pars['M_EU_NA'], pars['M_EU_BR'], None]]
        self.coal.params['events'].update(0, T=pars['T1'], S=pars['S1'])
        self.coal.params['events'].update(1, T=pars['T1'], S=pars['S2'])
        self.coal.params['events'].update(2, T=pars['T1'], S=pars['S3'])
        self.coal.params['events'].update(3, T=pars['T1']+1e-6)
        self.coal.params['events'].update(4, T=pars['T1']+1e-6)
        self.coal.params['events'].update(5, T=pars['T1']+1e-6, N=pars['N_AN'])

class FourPop(Model):
    """
    intermediate base class for models with pop pop (with a ghost
    population representing Mesoamerica)
    """

    def __init__(self):
        super().__init__()
        self.coal = egglib.coalesce.Simulator(num_pop=4, num_chrom=[0, 0, 0, 0], num_mut=1)
        self.params = {
            'N_NA': get_prior(cfg['simul']['priors']['N']),
            'N_BR': get_prior(cfg['simul']['priors']['N']),
            'N_EU': get_prior(cfg['simul']['priors']['N']),
            'T1': get_prior(cfg['simul']['priors']['T']),
            'T2': get_prior(cfg['simul']['priors']['T']),
            'T3': get_prior(cfg['simul']['priors']['T']),
            'S1': get_prior(cfg['simul']['priors']['S']),
            'S2': get_prior(cfg['simul']['priors']['S']),
            'S3': get_prior(cfg['simul']['priors']['S']),
            'M_MA_NA': get_prior(cfg['simul']['priors']['M']),
            'M_NA_MA': get_prior(cfg['simul']['priors']['M']),
            'M_MA_BR': get_prior(cfg['simul']['priors']['M']),
            'M_BR_MA': get_prior(cfg['simul']['priors']['M']),
            'M_MA_EU': get_prior(cfg['simul']['priors']['M']),
            'M_EU_MA': get_prior(cfg['simul']['priors']['M']),
            'M_NA_BR': get_prior(cfg['simul']['priors']['M']),
            'M_BR_NA': get_prior(cfg['simul']['priors']['M']),
            'M_NA_EU': get_prior(cfg['simul']['priors']['M']),
            'M_EU_NA': get_prior(cfg['simul']['priors']['M']),
            'M_BR_EU': get_prior(cfg['simul']['priors']['M']),
            'M_EU_BR': get_prior(cfg['simul']['priors']['M']),
            'm': get_prior(cfg['simul']['priors']['m'])
        }

    def update(self, pars):
        self.coal.params['N'] = [pars['N_NA'], pars['N_BR'], pars['N_EU'], 1]
        self.coal.params['migr_matrix'] = [[None, pars['M_NA_BR'], pars['M_NA_EU'], pars['M_NA_MA']],
                                           [pars['M_BR_NA'], None, pars['M_BR_EU'], pars['M_BR_MA']],
                                           [pars['M_EU_NA'], pars['M_EU_BR'], None, pars['M_EU_MA']],
                                           [pars['M_MA_NA'], pars['M_MA_BR'], pars['M_MA_EU'], None]]
        self.coal.params['events'].update(0, T=pars['T1'], S=pars['S1'])
        self.coal.params['events'].update(1, T=pars['T1']+1e-6)
        self.coal.params['events'].update(2, T=pars['T1']+pars['T2']+2e-6, S=pars['S2'])
        self.coal.params['events'].update(3, T=pars['T1']+pars['T2']+3e-6)
        self.coal.params['events'].update(4, T=pars['T1']+pars['T2']+pars['T3']+4e-6, S=pars['S3'])
        self.coal.params['events'].update(5, T=pars['T1']+pars['T2']+pars['T3']+5e-6)

class M40(FourPop):
    """
    MA
     -->NA
     -->BR
     -->EU
    """
    def __init__(self):
        super().__init__()
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=0)
        self.coal.params.add_event('merge', T=0, src=0, dst=3)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=1)
        self.coal.params.add_event('merge', T=0, src=1, dst=3)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=2)
        self.coal.params.add_event('merge', T=0, src=2, dst=3)
        self.params['T2'] = Zero()
        self.params['T3'] = Zero()

class M41(FourPop):
    """
    MA-->NA
      ---->BR
      ------>EU
    """
    def __init__(self):
        super().__init__()
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=0)
        self.coal.params.add_event('merge', T=0, src=0, dst=3)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=1)
        self.coal.params.add_event('merge', T=0, src=1, dst=3)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=2)
        self.coal.params.add_event('merge', T=0, src=2, dst=3)

class M44(FourPop):
    """
    MA-->NA-->BR
           ---->EU
    """
    def __init__(self):
        super().__init__()
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=2)
        self.coal.params.add_event('merge', T=0, src=2, dst=0)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=3)
        self.coal.params.add_event('merge', T=0, src=1, dst=0)
        self.coal.params.add_event('bottleneck', T=0, S=0, idx=0)
        self.coal.params.add_event('merge', T=0, src=0, dst=3)

########################################################################

load()
if __name__ == '__main__':
    main()
