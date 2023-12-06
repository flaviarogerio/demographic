import simul, stats, lzmp
import pathlib, yaml, random, math
from matplotlib import pyplot

"""
Performs posterior simulations based on the best model found in the
output file of abcranger.py and normal approximation of each parameter.
"""

with open('params.yml') as f:
    cfg = yaml.load(f, yaml.Loader)

# ensures the output dir exists
pathlib.Path('post').mkdir(exist_ok=True)

# import data for the best model
with open('abcranger.res') as f:

    # get table of model choice results, keep the last model
    for line in f:
        if line.strip() == 'max simulations model': break
    else: raise AssertionError
    for line in f:
        if line.strip() == '': break
        mod = line.split()[1]

    # get parameter estimates
    for line in f:
        if line.strip() == 'parameter	expectation	median	Q_0.05	Q_0.95	variance': break
    else: raise AssertionError
    pars = {}
    for line in f:
        if line.strip() == 'finished': break
        if line.strip() == '': break
        par, expect, median, q5, q95, var = line.split()
        pars[par] = {'e': float(expect), 'v': float(var),
                     'q5': float(q5), 'q95': float(q95),
                     'm': float(median)}

# get observed stats
obs = {}
with open('obs.txt') as f:
    for line in f:
        par, v = line.split()
        obs[par] = float(v)

# change draw() method of model
cls = simul.models[mod]
class Model(cls):
    def draw(self):
        while True:
            self.params = {
                p: random.normalvariate(d['e'], math.sqrt(d['v']))
                    for p, d in pars.items()}
            for v in self.params.values():
                if v < 0: break
            else: break

# run simulations
m = Model(mod)
jobs = []
for i in range(cfg['post']['nbatch']):
    if not pathlib.Path(f'post/simuls/simuls{i+1}_s.txt').is_file():
        jobs.append([f'post/simuls/simuls{i+1}', cfg['post']['szbatch'], cfg['post']['thin'], random.randint(1000000,9999999)])
lzmp.run(m.job, jobs, max_threads=cfg['post']['nthreads'], shuffle=False)

# import results
stats = {s: [] for s in obs}
for i in range(cfg['post']['nbatch']):
    with open(f'post/simuls/simuls{i+1}_s.txt') as f:
        h =  f.readline().split()
        for line in f:
            line = line.split()
            assert len(line) == len(h)
            d = dict(zip(h, line))
            for s in stats:
                stats[s].append(float(d[s]))

# plot each statistic
for stat in stats:
    print('plotting', stat)
    x = stats[stat]
    fig, ax = pyplot.subplots()
    ax.hist(x, bins=cfg['post']['nbins'], histtype='step', color='k', range=(min(x), max(x)))
    ax.set_xlabel(stat)
    ax.axvline(obs[stat], c='r')
    fig.savefig(f'post/stats:plot-{stat}.png')
    pyplot.close(fig)

# get prior distribution of parameters
m.draw()
params = {p: [] for p in m.params}
for fname in pathlib.Path('simuls/').glob(f'{mod}-*_p.txt'):
    with open(fname) as f:
        h = f.readline().split()
        for line in f:
            line = line.split()
            d = dict(zip(h, line))
            for p in params:
                params[p].append(float(d[p]))

# plot prior/posterior of parameters
for p in params:
    print('plotting', p)
    fig, ax = pyplot.subplots()
    ax.hist(params[p], bins=cfg['plot']['nbins'], histtype='step', color='k')
    ax.set_xlabel(p)
    ax.set_title(f'model {mod}')
    ax.axvline(pars[p]['m'], c='r')
    ax.axvline(pars[p]['q5'], c='r', ls=':')
    ax.axvline(pars[p]['q95'], c='r', ls=':')
    ax.axvline(pars[p]['e'], c='k')
    fig.savefig(f'post/params:{p}.png')
    pyplot.close(fig)
