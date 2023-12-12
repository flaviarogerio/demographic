"""
After simulations have been performed, create a plot for each parameter
and each statistic with the histogram from every model.

requires: obs.txt, simul.py, simuls/*
generates: plots/*
"""

from matplotlib import pyplot
import pathlib, simul, yaml

# load configuration
with open('params.yml') as f:
    cfg = yaml.load(f, yaml.Loader)

# directories
src = 'simuls'
dst = 'plots'

# output directory
pathlib.Path(dst).mkdir(exist_ok=True)

# get observed statistics
with open('obs.txt') as f:
    obs = {key: float(val) for (key, val) in map(str.split, f)}

#  table for statistics
data_s = {k: {m: [] for m in simul.model_names} for k in obs}

# create table for parameters (by inspecting simul module)
data_p = {}
for model in simul.models_map.values():
    print(model.__name__)
    m = model()
    for p in m.params:
        if p not in data_p: data_p[p] = {}
        data_p[p][model.__name__] = []

# open all simulation files in directory simuls
src = pathlib.Path(src)
for model in simul.model_names:
    n = 0

    # open all files
    for fname in sorted(src.glob(f'{model}-*.txt')):
        with open(fname) as f:
            h = f.readline().split()
            for line in f:
                line = line.split()
                assert len(line) == len(h)
                d = dict(zip(h, map(float, line)))
                for s in data_s:
                    data_s[s][model].append(d[s])
                for p in data_p:
                    if model in data_p[p]:
                        data_p[p][model].append(d[p])
                n += 1
                if n >= cfg['plot']['stop']: break
        if n >= cfg['plot']['stop']: break
    if n == 0:
        for p in data_p:
            if model in data_p[p]:
                del data_p[p][model]
        for s in data_s:
            del data_s[s][model]
    print(model, n)

# generate plots
for p in data_p:
    if len(data_p[p]) == 0: continue
    mini = min(map(min, data_p[p].values()))
    maxi = max(map(max, data_p[p].values()))
    print(p, format(mini, '.2f'), format(maxi, '.2f'), end=' ', flush=True)
    for mod in data_p[p]:
        print(mod, flush=True, end='')
        col, symb = cfg['models'][mod]
        pyplot.hist(data_p[p][mod], bins=cfg['plot']['bins'], histtype='step', color=col, range=(mini, maxi), label=mod)
    print()
    pyplot.xlabel(p)
    pyplot.legend(bbox_to_anchor=(1.2, 1))
    pyplot.tight_layout()
    pyplot.savefig(f'{dst}/param:{p}.png')
    pyplot.clf()

tests = []
i = 0
for s in data_s:
    mini = min(map(min, data_s[s].values()))
    maxi = max(map(max, data_s[s].values()))
    print(i:=i+1, 'of', len(data_s), s, format(mini, '.2f'), format(maxi, '.2f'), end=' ', flush=True)
    for mod in simul.model_names:
        if mod in data_s[s]:
            print(mod, flush=True, end='')
            col, symb = cfg['models'][mod]
            pyplot.hist(data_s[s][mod], bins=cfg['plot']['bins'], histtype='step', color=col, range=(mini, maxi), label=mod)
    print()
    pyplot.axvline(obs[s], ls=':', c='k')
    pyplot.plot([], [], 'k:', label='obs')
    pyplot.xlabel(s)
    pyplot.legend(bbox_to_anchor=(1.2, 1))
    pyplot.tight_layout()
    pyplot.savefig(f'{dst}/stat:{s}.png')
    pyplot.clf()
    for m in simul.model_names:
        if m in data_s[s]:
            p1 = sum(obs[s] <= i for i in data_s[s][m])/len(data_s[s][m])
            p2 = sum(obs[s] >= i for i in data_s[s][m])/len(data_s[s][m])
            if p1 < 0.05: tests.append(f'{s} > {m} {p1:.2f}')
            elif p2 < 0.05: tests.append(f'{s} < {m} {p2:.2f}')

print('significant excess:')
for test in tests:
    print('    '+test)
