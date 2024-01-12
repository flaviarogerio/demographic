"""
Get simulations from simuls/* and performs a LDA.

requires: simuls/*, obs.txt, simul.py (if list of models not specified)
generates: lda/*
"""

import pathlib, numpy, sklearn.discriminant_analysis, yaml, math, operator, scipy
from matplotlib import pyplot
import simul

# configuation
src = 'simuls'
dst = pathlib.Path('lda')
dst.mkdir(exist_ok=True)
obs_f = 'obs.txt'
with open('params.yml') as f:
    cfg = yaml.load(f, yaml.Loader)

# get list of models
models = cfg['lda']['models']
if len(models) == 0:
    models = simul.model_names
else:
    assert len(models) == len(set(models))
    assert len(models) > 2

# get user-specified plot structure
plan = cfg['lda']['struct']
nrow = len(plan)
ncol = set(map(len, plan))
assert len(ncol) == 1
ncol = ncol.pop()
print('dimensions:', nrow, ncol)

# get observed stats
with open(obs_f) as f:
    obs = {k: float(v) for k,v in map(str.split, f)}
stat_names = list(obs)
print(stat_names)

# import data
stats = []
counts = []

for mod in models:
    c = 0
    for fname in sorted(pathlib.Path(src).glob(f'{mod}-*.txt')):
        with open(fname) as f:
            h = f.readline().split()
            for line in f:
                line = list(map(float, line.split()))
                assert len(line) == len(h)
                d = dict(zip(h, line))
                stats.append([d[s] for s in stat_names])
                c += 1
                if c == cfg['lda']['stop']: break
        if c == cfg['lda']['stop']: break
    print(mod, c)
    counts.append(c)

# create tables for analysis
X = numpy.array(stats)
y = numpy.array([i+1 for i,c in enumerate(counts) for _ in range(c)])
print(len(y))

# perform discriminant analysis
lda = sklearn.discriminant_analysis.LinearDiscriminantAnalysis()
lda.fit(X, y)
examples = []
acc = 0
for c in counts:
    examples.append(stats[acc])
    acc += c
print(lda.predict(examples))

# predict observed dataset position
obs_v = [obs[s] for s in stat_names]
pred = lda.predict([obs_v])[0]
print(models[pred-1])

# transform data and obs
Xn = lda.transform(X)
obs_proj = lda.transform([obs_v])

# make 2D plots
fig, axes = pyplot.subplots(nrow, ncol, figsize=((ncol+0.25)*6.4, nrow*4.8), squeeze=False)
for i in range(nrow):
    for j in range(ncol):
        if  plan[i][j] == 0:
            axes[i][j].set_visible(False)
        else:
            d1, d2 = plan[i][j]
            d1 -= 1
            d2 -= 1
            var1 = lda.explained_variance_ratio_[d1] * 100
            var2 = lda.explained_variance_ratio_[d2] * 100
            acc = 0
            #xmin = min(Xn[:,d1])
            #xmax = max(Xn[:,d1])
            #ymin = min(Xn[:,d2])
            #ymax = max(Xn[:,d2])
            #X, Y = numpy.mgrid[xmin:xmax:100j, ymin:ymax:100j]
            #grid_pos = numpy.vstack([X.ravel(), Y.ravel()])

            for mod, cnt in zip(models, counts):
                print(d1+1, d2+1, mod)
                col, symb = cfg['models'][mod]
                Z1 = Xn[acc:acc+cnt,d1]
                Z2 = Xn[acc:acc+cnt,d2]
                # plot part of the points
                axes[i][j].plot(Z1[::cfg['lda']['step']],
                                Z2[::cfg['lda']['step']],
                                mec=col, marker=symb, mfc='None', ls='None', alpha=0.2, zorder=-1, ms=2)

                # place the average point
                mX = sum(Z1)/cnt
                mY = sum(Z2)/cnt
                axes[i][j].plot([mX], [mY], mec=col, marker=symb, mfc='None', ls='None', ms=8)

                # KDE
                #values = numpy.vstack([Z1, Z2])
                #krn = scipy.stats.gaussian_kde(values)
                #Z = krn(values)
                #Z = numpy.reshape(krn(grid_pos).T, X.shape)
                #axes[i][j].contour(X, Y, Z, colors=col, levels=3, zorder=-1)
                # filled contour
                #axes[i][j].imshow(numpy.rot90(Z), cmap=pyplot.cm.gist_earth_r,
                #        extent=[-10, 10, -10, 10])
                acc += cnt
            # finalize panel
            axes[i][j].set_xlabel(f'LD{d1+1} var: {var1:.2f}%')
            axes[i][j].set_ylabel(f'LD{d2+1} var: {var2:.2f}%')
            axes[i][j].axvline(0, ls='-', c='0.5', zorder=-100)
            axes[i][j].axhline(0, ls='-', c='0.5', zorder=-100)
            axes[i][j].set_title(f'Variance explained: {var1+var2:.2f}%')
            axes[i][j].plot([obs_proj[0,d1]], [obs_proj[0,d2]], marker='*', ms=10, mfc='w', mec='k')
            #axes[i][j].set_xlim(-5, 5)
            #axes[i][j].set_ylim(-5, 5)

for mod in models:
    col, symb = cfg['models'][mod]
    axes[0][-1].plot([], [], mec=col, marker=symb, mfc='None', ls='None', label=mod)
axes[0][j].plot([], [], marker='*', ls='None', ms=10, mfc='w', mec='k', label='obs')
fig.legend(loc='center right', bbox_to_anchor=(0.95, 0.5))
fig.tight_layout(rect=(0, 0, 0.8, 1))  #pad=cfg['lda']['pad']
fig.savefig(dst / 'lda.png')
pyplot.close(fig)

# make 1D plots
for i in range(len(models)-1):
    print(f'LDA{i+1}')
    fig, ax = pyplot.subplots()
    acc = 0
    mini = min(Xn[:,i])
    maxi = max(Xn[:,i])
    for mod, cnt in zip(models, counts):
        col, symb = cfg['models'][mod]
        Z = Xn[acc:acc+cnt,i]
        acc += cnt
        kernel = scipy.stats.gaussian_kde(Z)
        x = [mini+(maxi-mini)*i/50 for i in range(51)]
        y = kernel(x)
        ax.plot(x, y, c=col, ls='-', marker='None', label=mod)
        ax.set_yticks([])
        #ax2 = ax.twinx()
        #ax2.hist(Z, bins=cfg['lda']['bins'], histtype='step', color=col, range=(mini, maxi), label=mod)
        #ax2.set_yticks([])
    ax.axvline(obs_proj[0,i], c='k')
    ax.set_title(f'LDA{i+1} variance explained: {lda.explained_variance_ratio_[i] * 100:.2f}%')
    ax.legend(bbox_to_anchor=(1.2, 1))
    pyplot.tight_layout()
    fig.savefig(dst / f'LDA{i+1}.png')
    pyplot.close(fig)
