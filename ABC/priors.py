from matplotlib import pyplot
import simul, yaml, pathlib

pathlib.Path('priors').mkdir(exist_ok=True)
with open('params.yml') as f:
    cfg = yaml.load(f, yaml.Loader)

draws = {}
for model in [simul.Model31, simul.Model32, simul.Model33,
              simul.Model34, simul.Model35, simul.Model36,
              simul.Model37, simul.Model38, simul.Model39,
              simul.Model3A, simul.Model3B, simul.Model3C,
              simul.Model3D]:
    m = model()
    print(m.name)
    m.draw()
    draws[m.name] = {k: [None] * cfg['priors']['nr'] for k in m.params}
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
    for mod, col in cfg['models'].items():
        if p in draws[mod]:
            pyplot.hist(draws[mod][p], bins=cfg['priors']['nbins'], histtype='step', color=col, label=mod, range=(mini, maxi))
    pyplot.xlabel(p)
    pyplot.legend()
    pyplot.savefig(f'priors/{p}.png')
    pyplot.clf()



