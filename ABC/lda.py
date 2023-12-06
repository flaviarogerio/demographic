import pathlib, numpy, sklearn.discriminant_analysis
from matplotlib import pyplot
import yaml

src = 'simuls'
dst = 'lda.png'

with open('params.yml') as f:
    cfg = yaml.load(f, yaml.Loader)

models = cfg['lda']['models']
if len(models) == 0:
    import simul
    models = sorted(simul.models)
else:
    assert len(models) == len(set(models))
    assert len(models) > 2

# get user-specified plot structure
plan = cfg['lda']['struct']
nrow = len(plan)
ncol = set(map(len, plan))
assert len(ncol) == 1
ncol = ncol.pop()
print(nrow, ncol)

# import data
stats = []
mods = []

header = None

for i, mod in enumerate(models):
    c = 0
    for fname in sorted(pathlib.Path(src).glob(f'{mod}-*_s.txt')):
        print(fname)
        with open(fname) as f:
            params_f = open(str(fname)[:-5]+'p.txt')
            params_h = params_f.readline().split()
            h = f.readline().split()
            if header is None: header = h
            else: assert h == header
            for line in f:
                params_ln = params_f.readline()
                if params_ln == '': continue
                assert params_ln != ''
                params_ln = params_ln.split()
                assert len(params_ln) == len(params_h)
                params_d = dict(zip(params_h, params_ln))
                line = list(map(float, line.split()))
                assert len(line) == len(h)
                stats.append(line)
                mods.append(i+1)
                c += 1
                if c == cfg['lda']['maxi']: break
        if c == cfg['lda']['maxi']: break

X = numpy.array(stats)
y = numpy.array(mods)

counts = {mod: mods.count(i+1) for i,mod in enumerate(models)}
print(counts)

lda = sklearn.discriminant_analysis.LinearDiscriminantAnalysis()
lda.fit(X, y)
examples = []
acc = 0
for mod in models:
    acc += counts[mod]
    examples.append(stats[acc - 1])
print(lda.predict(examples))

obs_h = []
obs_v = []
with open('obs.txt') as f:
    for line in f:
        h, v = line.split()
        obs_h.append(h)
        obs_v.append(float(v))
print(lda.predict([obs_v]))

i = 0
for s in obs_h:
    if max(abs(lda.coef_[:,i])) >= 10:
        coefs = lda.coef_[:,i]
        print(f'{s:<10s} {coefs}')
    i += 1

Xn = lda.transform(X)
obs_proj = lda.transform([obs_v])

fig, axes = pyplot.subplots(nrow, ncol, figsize=(ncol*6.4, nrow*4.8))

for i in range(nrow):
    for j in range(ncol):
        if  plan[i][j] == 0:
            axes[i][j].set_visible(False)
        else:
            d1, d2 = plan[i][j]
            d1 -= 1
            d2 -= 1
            acc = 0
            for mod in models:
                col, symb = cfg['models'][mod]
                cnt = counts[mod]
                axes[i][j].plot(Xn[acc:acc+cnt,d1][::cfg['lda']['thin']],
                                Xn[acc:acc+cnt,d2][::cfg['lda']['thin']],
                                mec=col, marker=symb, mfc='None', ls='None')
                acc += cnt
                axes[i][j].set_xlabel(f'Dimension {d1+1}')
                axes[i][j].set_ylabel(f'Dimension {d2+1}')
                axes[i][j].axvline(0, ls='-', c='0.5', zorder=-100)
                axes[i][j].axhline(0, ls='-', c='0.5', zorder=-100)
            axes[i][j].plot([obs_proj[0,d1]], [obs_proj[0,d2]], 'k*', ms=10, label='obs')

for mod in models:
    col, symb = cfg['models'][mod]
    axes[0][-1].plot([], [], mec=col, marker=symb, mfc='None', ls='None', label=mod)
axes[0][-1].legend(bbox_to_anchor=(1,1))

fig.suptitle('Linear Discriminant Analysis')

fig.savefig(dst)
