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
        par, expect, median, q005, q095, var = line.split()
        pars[par] = float(expect), float(var)

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
                p: random.normalvariate(e, math.sqrt(v))
                    for p, (e, v) in pars.items()}
            for v in self.params.values():
                if v < 0: break
            else: break

# run simulations
m = Model(mod)
jobs = []
for i in range(cfg['post']['nbatch']):
    if not pathlib.Path(f'post/simuls{i+1}_s.txt').is_file():
        jobs.append([f'post/simuls{i+1}', cfg['post']['szbatch'], cfg['post']['thin'], random.randint(1000000,9999999)])
lzmp.run(m.job, jobs, max_threads=cfg['post']['nthreads'], shuffle=False)

# import results
stats = {s: [] for s in obs}
for i in range(cfg['post']['nbatch']):
    with open(f'post/simuls{i+1}_s.txt') as f:
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
    fig.savefig(f'post/plot-{stat}.png')
    pyplot.close(fig)
