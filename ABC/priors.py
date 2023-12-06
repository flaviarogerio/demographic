from matplotlib import pyplot
import simul, yaml, pathlib

pathlib.Path('priors').mkdir(exist_ok=True)
with open('params.yml') as f:
    cfg = yaml.load(f, yaml.Loader)

draws = {}
for name, Model in simul.models.items():
    m = Model(name)
    print(name)
    m.draw()
    draws[name] = {k: [None] * cfg['priors']['nr'] for k in m.params}
    for i in range(cfg['priors']['nr']):
        m.draw()
        for k in draws[m.name]: draws[m.name][k][i] = m.params[k]

pars = set()
for d in draws.values(): pars.update(d)
for p in pars:
    print(p)
    mini = 0
    maxi = 0
    for draw in draws.values():
        if p in draw and min(draw[p]) < mini: mini = min(draw[p])
        if p in draw and max(draw[p]) > maxi: maxi = max(draw[p])
    for mod in draws:
        col, symb = cfg['models'][mod]
        if p in draws[mod]:
            n, bins, patches = pyplot.hist(draws[mod][p], bins=cfg['priors']['nbins'], histtype='step', color=col, range=(mini, maxi))
            x = [(bins[i]+bins[i+1])/2 for i in range(len(n))]
            pyplot.plot(x, n, marker=symb, mec=col, mfc='None', ls='None', label=mod)
    pyplot.xlabel(p)
    pyplot.legend()
    pyplot.savefig(f'priors/{p}.png')
    pyplot.clf()



