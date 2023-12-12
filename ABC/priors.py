"""
This script is designed to generate plots for prior distributions.

requires: simuls.py
generates: priors/*
"""

from matplotlib import pyplot
import simul, yaml, pathlib

# ensure destination directory exists
pathlib.Path('priors').mkdir(exist_ok=True)

# load configuration
with open('params.yml') as f:
    cfg = yaml.load(f, yaml.Loader)

# performs draws from priors
draws = {}
for mod, Model in simul.models_map.items():
    print(mod)
    m = Model()
    for par, gen in m.params.items():
        if type(gen).__name__ == 'Zero': continue
        if par not in draws: draws[par] = {}
        draws[par][mod] = [gen() for _ in range(cfg['priors']['num'])]
        

# make histogram for each parameter
for p in draws:
    print(p)
    mini = min(map(min, draws[p].values()))
    maxi = max(map(max, draws[p].values()))
    for mod in draws[p]:
        col, symb = cfg['models'][mod]
        pyplot.hist(draws[p][mod], bins=cfg['priors']['bins'],
            histtype='step', color=col, range=(mini, maxi), label=mod)
    pyplot.xlabel(p)
    pyplot.legend(bbox_to_anchor=(1.2, 1))
    pyplot.tight_layout()
    pyplot.savefig(f'priors/{p}.png')
    pyplot.clf()



