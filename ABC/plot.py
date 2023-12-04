from matplotlib import pyplot
import pathlib, simul, yaml

with open('params.yml') as f:
    cfg = yaml.load(f, yaml.Loader)
models = cfg['models']

pathlib.Path('plots').mkdir(exist_ok=True)
src = 'simuls'
dst = 'plots'

# get list of params/stats
m31 = simul.Model31()
m31.draw()
m3D = simul.Model3D()
m3D.draw()
keys_p = sorted(set(list(m31.params) + list(m3D.params)))
obs = {}
with open('obs.txt') as f:
    keys_s = []
    for line in f:
        key, v = line.split()
        keys_s.append(key)
        obs[key] = float(v)

# initialize tables
data_p = {k: {m: [] for m in models} for k in keys_p}
data_s = {k: {m: [] for m in models} for k in keys_s}

# open all simulation files in directory simuls
src = pathlib.Path(src)
for model in models:

    # open all statistic files
    for fname in sorted(src.glob(f'{model}-*_s.txt')):
        root = str(fname)[:-6] # identify root to locate parameter file
        if len(data_p[keys_p[0]][model]) >= cfg['plot']['maxi']: continue
        print(root) # feedback

        # import statistics
        with open(fname) as f:
            assert f.readline().split() == keys_s
            for line in f:
                d = dict(zip(keys_s, map(float, line.split())))
                for k in data_s: data_s[k][model].append(d[k])

        # import parameters
        with open(root+'_p.txt') as f:
            h = f.readline().split()
            for line in f:
                d = dict(zip(h, line.split(), strict=True))
                for k in d: data_p[k][model].append(float(d[k]))

    # delete empty parameter lists
    for p in data_p:
        if len(data_p[p][model]) == 0:
            del data_p[p][model]

# generate plots
for p in keys_p:
    mini = min(map(min, data_p[p].values()))
    maxi = max(map(max, data_p[p].values()))
    print(p, format(mini, '.2f'), format(maxi, '.2f'), end=' ', flush=True)
    for k, c in models.items():
        if k not in data_p[p]: continue # skipping models without this param
        print(k[-1], flush=True, end='')
        pyplot.hist(data_p[p][k], bins=cfg['plot']['nbins'], histtype='step', color=c, label=k, range=(mini, maxi))
    print()
    pyplot.xlabel(p)
    pyplot.legend()
    pyplot.savefig(f'{dst}/param-{p}.png')
    pyplot.clf()

tests = []
for i, s in enumerate(keys_s):
    mini = min(map(min, data_s[s].values()))
    maxi = max(map(max, data_s[s].values()))
    print(i+1, 'of', len(keys_s), s, format(mini, '.2f'), format(maxi, '.2f'), end=' ', flush=True)
    for k, c in models.items():
        print(k[-1], flush=True, end='')
        pyplot.hist(data_s[s][k], bins=cfg['plot']['nbins'], histtype='step', color=c, label=k, range=(mini, maxi))
    print()
    pyplot.axvline(obs[s], ls='-', c='r')
    pyplot.plot([], [], 'r-', label='obs')
    pyplot.xlabel(s)
    pyplot.legend()
    pyplot.savefig(f'{dst}/stat-{s}.png')
    pyplot.clf()
    for m in models:
        p1 = sum(obs[s] <= i for i in data_s[s][m])/len(data_s[s][m])
        p2 = sum(obs[s] >= i for i in data_s[s][m])/len(data_s[s][m])
        if p1 < 0.05: tests.append(f'{s} > {m} {p1:.2f}')
        elif p2 < 0.05: tests.append(f'{s} < {m} {p2:.2f}')

print('significant excess:')
for test in tests:
    print('    '+test)
