"""
- Generate plots comparing prior/posterior distributions of parameters
  according to a given list of models
- Generate LDA plot from ABC analysis
- Performs posterior simulations based on the best model found in the
  output files of abcranger.py and normal approximation of each
  parameter.

* requires simul.py, simuls/*
* generates post/*
"""

import simul
import pathlib, yaml, random, math, lzmp, numpy, re
from scipy import stats
from matplotlib import pyplot

# load configuration
with open('params.yml') as f:
    cfg = yaml.load(f, yaml.Loader)
post_path = pathlib.Path('post')
post_path.mkdir(exist_ok=True)

# get model renaming mapping
mp = cfg['model_mapping']

# get observed stats
obs = {}
with open('obs.txt') as f:
    for line in f:
        par, v = line.split()
        obs[par] = float(v)

### process model comparisons ###
#################################

for name, pars in cfg['modelchoice']['analyses'].items():
    if 'models' in pars: groups = pars['models']
    else: groups = pars['groups']
    n = []
    votes = {g: [] for g in groups}
    P = []
    with open(pathlib.Path('ranger') / 'modelchoice' / name / 'results.txt') as f:
        for line in f:
            line = line.split()
            n.append(int(line[0]))
            for i, g in enumerate(groups):
                votes[g].append(int(line[2+i]))
            P.append(float(line[-1]))
    fig, axes = pyplot.subplots(2, 1, figsize=(6.4, 2*4.8))
    axes[1].plot(n, P, 'ko-', mfc='w')
    axes[1].set_ylabel('Posterior probability')
    axes[1].set_ylim(0, 1)
    axes[1].set_xticks([100000,200000,300000,400000,500000])
    axes[1].set_xticklabels(['100K','200K','300K','400K','500K'])

    # sort models based on new model code
    # just before plotting
    # only if models are plotted
    if 'models' in pars:
        groups.sort(key=lambda m: int(mp[m][1:]))

    for g in groups:
        lbl = mp.get(g, g) # used recoded model number if it is a model
        c, symb = cfg['models'][g]
        axes[0].plot(n, votes[g], label=lbl, c=c, mfc='w', ls='-', marker=symb)
    axes[0].set_ylabel('Number of votes')
    axes[0].legend(bbox_to_anchor=(1.05, 1))
    axes[0].set_xticks([100000,200000,300000,400000,500000])
    axes[0].set_xticklabels(['100K','200K','300K','400K','500K'])
    axes[0].plot([100000],[0], 'w,', zorder=-1000)
    axes[0].set_title(pars['label'])
    fig.tight_layout()
    fig.savefig((pathlib.Path('post') / ('votes-' + name)).with_suffix('.png'))
    pyplot.close(fig)

### process all models ###
##########################

kernels = {}

path = pathlib.Path('simuls')
for model in cfg['post']['models']:

    # ensures the output dir exists
    dst = pathlib.Path('post') / model
    dst.mkdir(exist_ok=True)
    (dst / 'params').mkdir(exist_ok=True)
    (dst / 'stats').mkdir(exist_ok=True)
    kernels[model] = {}

    ### process all parameters ###
    ##############################

    m = simul.models_map[model]()

    for param in m.params:

        # skip if posterior data not available
        post = pathlib.Path('ranger') / 'estimparams' / model / param / 'out.predweights'
        if not post.is_file(): continue
        print(f'importing posterior of {model}:{param}')

        ### import posterior ###
        ########################
        pred = []
        weights = []
        n = 0
        with open(post) as f:
            f.readline()
            for line in f:
                v, w  = map(float, line.split(','))
                pred.append(v)
                weights.append(w)
                n += 1

        # smooth posterior with KDE
        kernels[model][param] = stats.gaussian_kde(pred, weights=weights)

        ### prior/posterior plot ###
        ############################

        # skip figure if already present
        param_f = dst / 'params' / f'{param}.png'
        if not param_f.is_file():

            # initialize prior/posterior picture
            fig, ax = pyplot.subplots()

            # pick paramer values from simulations (prior)
            values = []
            for file in path.glob(f'{model}-*.txt'):
                with open(file) as f:
                    idx = f.readline().split().index(param)
                    for line in f:
                        values.append(float(line.split()[idx]))
                if len(values) >= cfg['post']['prior']:
                    break

            # smooth prior with KDE and plot it
            kernel1 = stats.gaussian_kde(values, weights=None)
            xmin = min(values)
            xmax = max(values)
            x = [xmin+(xmax-xmin)*i/50 for i in range(51)]
            y = list(map(kernel1, x))
            ax.plot(x, y, 'b-', label='prior')

            # plot posterior
            y = list(map(kernels[model][param], x))
            ax.plot(x, y, 'r-', label='posterior')

            # finalize picture
            ax.legend(bbox_to_anchor=(1.4, 1))
            ax.set_title(f'[{model}] {param}')
            ax.set_xlabel(param)
            fig.tight_layout()
            fig.savefig(param_f)
            pyplot.close(fig)

    ### perform posterior simulations ###
    #####################################

    # reimplement model methods to use kernels for drawing
    cls = simul.models_map[model]
    class Model(cls):

        # replace code to return parameter values (use resample from kernel)
        # only positive values
        def draw(self):
            pars = {}
            for p in self.params:
                while True:
                    if p not in kernels[self.model]:
                        raise RuntimeError(f'posterior distribution not found for: {self.model}')
                    if (v := kernels[self.model][p].resample(1, random.randint(1000000,9999999))[0][0]) > 0:
                        pars[p] = v
                        break
            return pars

    # run simulations
    print(f'posterior simulations for model {model}')
    m = Model()
    m.model = model
    jobs = []

    sim_path = pathlib.Path('post') / model / 'simuls'
    sim_path.mkdir(exist_ok = True)
    for i in range(cfg['post']['sim_n']):
        fname = sim_path / f'{i+1:>03}.txt'
        if fname.is_file() and not cfg['post']['sim_overwrite']:
            pass#print(f'{fname} already exists - skipped')
        else:
            jobs.append([fname, cfg['post']['sim_sz'], cfg['post']['sim_thin'], random.randint(1000000,9999999)])
    lzmp.run(m.job, jobs, max_threads=cfg['nthreads'], shuffle=False)

    # import results
    sim_stats = {s: [] for s in obs}
    for i in range(cfg['post']['sim_n']):
        with open(sim_path / f'{i+1:>03}.txt') as f:
            h =  f.readline().split()
            n = 0
            for line in f:
                line = line.split()
                assert len(line) == len(h)
                d = dict(zip(h, line))
                for s in sim_stats:
                    sim_stats[s].append(float(d[s]))
                n += 1
            if n != cfg['post']['sim_sz'] :
                raise ValueError(f'invalid number of simulations in {f.name}: {n}')

    # plot each statistic
    for stat in sim_stats:
        print(f'plotting {model}:{stat}')
        x = sim_stats[stat]
        fig, ax = pyplot.subplots()
        ax.hist(x, bins=cfg['post']['bins'], histtype='step', color='k', range=(min(x), max(x)), label='simuls')
        ax.set_xlabel(stat)
        ax.axvline(obs[stat], c='r', label='obs')
        ax.legend()
        fig.savefig(dst / 'stats' / f'{stat}.png')
        pyplot.close(fig)

### LDA ###
###########

def lda_split(path, n):
    """
    function to split LDA file into per-group files (to speed up access
    of data)
    """

    print(f'splitting file {path}')
    f_map = {i+1: open(pathlib.Path(f'{ldaf}.{i+1}'), 'w') for i in range(n)}
    counts = dict.fromkeys(f_map, 0)
    with open(path) as f:
        for line in f:
            if line[0] == '#': continue
            k = int(re.search('([0-9]+)$', line, re.MULTILINE).group(1))
            if k == 0: continue
            counts[k] += 1
            f_map[k].write(line)
            if counts[k] == 1:
                print(f'    model #{k}')
    print('    done')

def plot(ax, d1, d2, data):
    """
    plot all groups points of two given LDA dimensions (including
    KDE-smoothed contour lines)
    """
    xmin = min([min(data[g][:,d1]) for g in data])
    xmax = max([max(data[g][:,d1]) for g in data])
    ymin = min([min(data[g][:,d2]) for g in data])
    ymax = max([max(data[g][:,d2]) for g in data])
    X, Y = numpy.mgrid[xmin:xmax:100j, ymin:ymax:100j]
    grid_pos = numpy.vstack([X.ravel(), Y.ravel()])

    for g in data:
        col, symb = cfg['models'][g]
        xvalues = data[g][:,d1]
        yvalues = data[g][:,d2]
        ax.plot(xvalues, yvalues, ls='None', mec=col, mfc='None', marker=symb, alpha=0.2, ms=2)
        ax.plot([], [], c=col, label=g)

        # KDE
        values = numpy.vstack([xvalues, yvalues])
        krn = stats.gaussian_kde(values)
        Z = krn(values)
        Z = numpy.reshape(krn(grid_pos).T, X.shape)
        ax.contour(X, Y, Z, colors=col, levels=3, zorder=5)
    ax.plot(obs[d1], obs[d2], ls='None', mec='k', marker='*', mfc='w', label='obs', ms=10, zorder=10)
    ax.set_title(f'LDA {d1+1}-{d2+1} {sub.name}')

path = pathlib.Path('ranger') / 'modelchoice'
for sub in path.iterdir():
    ldaf = sub / str(cfg['modelchoice']['nsam'][-1]) / 'out.lda'

    ### process all completed analyses ###
    ######################################

    if ldaf.is_file():
        print(f'plotting LDA for {sub.name}')

        # determine list of group/model names
        if 'groups' in cfg['modelchoice']['analyses'][sub.name]:
            groups = cfg['modelchoice']['analyses'][sub.name]['groups']
        else:
            groups = cfg['modelchoice']['analyses'][sub.name]['models']

        # split the LDA file into sub-files (per model) if not done already
        T = ldaf.stat().st_mtime
        for i in range(len(groups)):
            file = pathlib.Path(f'{ldaf}.{i+1}')
            if not file.is_file() or T >= file.stat().st_mtime:
                lda_split(ldaf, len(groups))
                break

        # import observed data
        with open(ldaf) as f:
            for line in f:
                if line[0] == '#': continue
                bits = line.split()
                assert bits[-1] == '0'
                obs = [float(v) for v in bits[:-1]]
                break

        # import model/group data
        data = {}
        for i, g in enumerate(groups):
            data[g] = []
            with open(pathlib.Path(f'{ldaf}.{i+1}')) as f:
                for i in range(cfg['post']['lda']):
                    line = f.readline().split()
                    data[g].append([float(v) for v in line[:-1]])
            data[g] = numpy.array(data[g])

        # determine the number of dimensions
        nd = len(groups)-1

        # if only one dimension, plot a standard smoothed histogram
        fname = (post_path / ('lda-' + sub.name)).with_suffix('.png')
        if nd == 1:
            fig, ax = pyplot.subplots()
            for g in groups:
                values = data[g][:,0]
                krn = stats.gaussian_kde(values, weights=None)
                xmin = min(values)
                xmax = max(values)
                x = [xmin+(xmax-xmin)*i/50 for i in range(51)]
                y = list(map(krn, x))
                ax.plot(x, y, ls='-', c=cfg['models'][g][0], marker=None, label=g)
            ax.axvline(obs[0], ls=':', c='k', label='obs')
            ax.set_title(f'LDA {sub.name}')
            ax.legend()
            fig.tight_layout()
            fig.savefig(fname)
            pyplot.close(fig)

        # two dimensions: scatter plot
        elif nd == 2:
            fig, ax = pyplot.subplots()
            plot(ax, 0, 1, data)
            ax.legend()
            fig.tight_layout()
            fig.savefig(fname)
            pyplot.close(fig)

        # more than two dimensions, plot the first two pairs
        # two dimensions: scatter plot
        else:
            fig, axes = pyplot.subplots(2, 1, figsize=(6.4, 2*4.8))
            plot(axes[0], 0, 1, data)
            plot(axes[1], 2, 3, data)
            axes[0].legend(bbox_to_anchor=(1.1,1))
            fig.tight_layout()
            fig.savefig(fname)
            pyplot.close(fig)
