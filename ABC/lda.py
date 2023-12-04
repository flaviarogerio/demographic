import pathlib, numpy, sklearn.discriminant_analysis
from matplotlib import pyplot
import yaml

with open('params.yml') as f:
    cfg = yaml.load(f, yaml.Loader)
models = cfg['models']

src = 'simuls'
dst = 'lda.png'

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
counts = [mods.count(i+1) for i in range(len(models))]
print(counts)

lda = sklearn.discriminant_analysis.LinearDiscriminantAnalysis()
lda.fit(X, y)
examples = []
acc = 0
for i in range(len(models)):
    acc += counts[i]
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

fig, axes = pyplot.subplots(3, 2, figsize=(2*6.4, 3*4.8))

acc = 0
for (model, col), cnt in zip(models.items(), counts):
    print(model, col, cnt)
    axes[0][0].plot(Xn[acc:acc+cnt,0][::cfg['lda']['thin']], Xn[acc:acc+cnt,1][::cfg['lda']['thin']], mec=col, marker='o', mfc='None', ls='None')
    axes[0][1].plot(Xn[acc:acc+cnt,2][::cfg['lda']['thin']], Xn[acc:acc+cnt,3][::cfg['lda']['thin']], mec=col, marker='o', mfc='None', ls='None')
    axes[1][0].plot(Xn[acc:acc+cnt,4][::cfg['lda']['thin']], Xn[acc:acc+cnt,5][::cfg['lda']['thin']], mec=col, marker='o', mfc='None', ls='None')
    axes[1][1].plot(Xn[acc:acc+cnt,6][::cfg['lda']['thin']], Xn[acc:acc+cnt,7][::cfg['lda']['thin']], mec=col, marker='o', mfc='None', ls='None')
    axes[2][0].plot(Xn[acc:acc+cnt,8][::cfg['lda']['thin']], Xn[acc:acc+cnt,9][::cfg['lda']['thin']], mec=col, marker='o', mfc='None', ls='None')
    axes[2][1].plot(Xn[acc:acc+cnt,8][::cfg['lda']['thin']], Xn[acc:acc+cnt,10][::cfg['lda']['thin']], mec=col, marker='o', mfc='None', ls='None')
    acc += cnt
axes[2][1].set_visible(0)
axes[0][0].plot([obs_proj[0,0]], [obs_proj[0,1]], 'k*', ms=10, label='obs')
axes[0][1].plot([obs_proj[0,2]], [obs_proj[0,3]], 'k*', ms=10, label='obs')
axes[1][0].plot([obs_proj[0,4]], [obs_proj[0,5]], 'k*', ms=10, label='obs')
axes[1][1].plot([obs_proj[0,6]], [obs_proj[0,7]], 'k*', ms=10, label='obs')
axes[2][0].plot([obs_proj[0,8]], [obs_proj[0,9]], 'k*', ms=10, label='obs')
axes[2][1].plot([obs_proj[0,8]], [obs_proj[0,10]], 'k*', ms=10, label='obs')
axes[0][0].set_xlabel('Axis 1')
axes[0][0].set_ylabel('Axis 2')
axes[0][1].set_xlabel('Axis 3')
axes[0][1].set_ylabel('Axis 4')
axes[1][0].set_xlabel('Axis 5')
axes[1][0].set_ylabel('Axis 6')
axes[1][1].set_xlabel('Axis 7')
axes[1][1].set_ylabel('Axis 8')
axes[2][0].set_xlabel('Axis 8')
axes[2][0].set_ylabel('Axis 9')
axes[2][1].set_xlabel('Axis 8')
axes[2][1].set_ylabel('Axis 10')

for row in axes:
    for ax in row:
        ax.axvline(0, ls='-', c='0.5', zorder=-100)
        ax.axhline(0, ls='-', c='0.5', zorder=-100)

for (model, col) in models.items():
    axes[2][0].plot([], [], mec=col, marker='s', mfc=col, ls='None', label=model)
axes[2][0].legend()

fig.suptitle('Linear Discriminant Analysis')

fig.savefig(dst)
