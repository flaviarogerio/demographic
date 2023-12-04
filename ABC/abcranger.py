import pandas, numpy, pyabcranger, pathlib, yaml
dst = 'abcranger.res'

# import configuration files
with open('params.yml') as f:
    cfg = yaml.load(f, yaml.Loader)
    models = list(cfg['models'])
with open('obs.txt') as f:
    obs = {}
    for line in f:
        k, v = line.split()
        assert k not in obs
        obs[k] = float(v)

# make a single, big pandas.DataFrame
df = []
models_start = {}
models_num = {}
models_params = {}
stats_names = None
cur = 0
for m in models:
    files = sorted(pathlib.Path('simuls').glob(f'{m}-*_p.txt'))
    n = 0
    for fname in files:
        t_params = pandas.read_table(fname, dtype=float, sep=' ')
        t_stats = pandas.read_table(str(fname)[:-6]+'_s.txt', dtype=float, sep=' ')
        bit = pandas.concat([t_params, t_stats], axis=1)
        params = list(t_params.columns.values)
        stats = list(t_stats.columns.values)
        if m not in models_start:
            models_start[m] = cur
            models_num[m] = len(bit)
            models_params[m] = params
        else:
            assert params == models_params[m]
            models_num[m] += len(bit)
        if stats_names is None:
            stats_names = stats
        else:
            assert stats == stats_names
        df.append(bit)
        cur += len(bit)
        print(fname, models_num[m], cur)
        if models_num[m] >= cfg['ranger']['lim'][-1]: break

df = pandas.concat(df, axis=0, ignore_index=True)

print('starts:', models_start)
print('num:', models_num)
print('num stats:', len(stats_names))
params_outer = set().union(* models_params.values())
params_inner = list(params_outer.intersection(* models_params.values()))
assert params_outer == set(df.columns) - set(stats_names)
params_outer = list(params_outer)
print('all params:', params_outer)
print('common params:', params_inner)
print('starts:', models_start)
print('num:', models_num)

out = open(dst, 'w')
out.write(f'num stats: {len(stats_names)}\n')
out.write(f'all params: ' + ' '.join(params_outer) + '\n')
out.write('common params ' + ' '.join(params_inner) + '\n')

# process all subsets
model_list = list(models)
model_choice = []
for lim in cfg['ranger']['lim']:
    print('limit:', lim)
    out.write(f'\n### max: {lim} ###\n\n')

    # make df subset
    nrecscen = []
    rng = []
    for m in model_list:
        n = min(lim, models_num[m])
        nrecscen.append(n)
        rng.append((models_start[m], models_start[m]+n))
    sub = pandas.concat([df[a:b] for (a,b) in rng], axis=0, ignore_index=True)

    # extract stats / params tables
    stats = sub[stats_names].values
    params = sub[params_outer].values
    np = len(params_outer)

    # import observed statistics
    statobs = numpy.array([obs[i] for i in stats_names])
    nrec = len(stats)
    scenarios = [i+1.0 for i,n in enumerate(nrecscen) for _ in range(n)]

    # create reference table
    print('making ref table...')
    print('nrec:', nrec)
    print('nrecscen:', nrecscen)
    print('nparams:', [np] * len(models))
    print('params:', len(params_outer))
    print('stats:', len(stats_names))
    print('stats:', stats.shape)
    print('params:', len(params_outer))
    print('scenarios:', len(scenarios))
    print('observed:', len(statobs))

    rf = pyabcranger.reftable(
        nrec,
        nrecscen,
        [np] * len(models),
        params_outer,
        stats_names,
        stats,
        params,
        scenarios
    )

    # grow random forest
    postres = pyabcranger.modelchoice(rf, statobs, f"--ntree 500 --threads {cfg['ranger']['nthreads']}", False)

    # pick up selected model
    mod_index = postres.predicted_model[0]
    selected_model = mod_index + 1
    model_choice.append((lim, model_list[mod_index]))

    # export
    out.write(f'selected model: {models[postres.predicted_model[0]]}\n')
    out.write('votes: ' + ' '.join(str(v) for v in postres.votes[0]) + '\n')
    out.write(f'proba: {postres.post_proba[0]}\n')
    for res in ['settings', 'importance' , 'predictions', 'confusion']:
        p = pathlib.Path(f'modelchoice_out.{res}')
        with open(p) as f:
            out.write(f'\n# modelchoice_out.{res} #\n\n{f.read()}')
        p.unlink()
    for res in ['lda', 'ooberror']:
        pathlib.Path(f'modelchoice_out.{res}').unlink()
    out.flush()

# select valid params for the selected model
model = model_list[mod_index]
params_names = models_params[model]
np = len(params)

# fit parameters on selected model
a = models_start[model]
b = a + models_num[model]
params = df[params_names][a:b].values
stats = df[stats_names][a:b].values
nrec = len(params)
nrecscen = [nrec]

rf = pyabcranger.reftable(
    nrec,
    nrecscen,
    [np],
    params_names,
    stats_names,
    stats,
    params,
    [selected_model] * nrec
)

# process parameters
estimated_params = {}
for param in params_names:
    print("Estimating parameter " + param)
    out.write(f'### fit {param} ###\n')
    cli_params = f"--ntree 500 --parameter {param} --threads {cfg['ranger']['nthreads']} --noob 50 --chosenscen {selected_model}"
    res = pyabcranger.estimparam(rf, statobs, cli_params, False, False)
    estimated_params[param] = res.point_estimates[0]

    # export
    for res in ['settings', 'importance' , 'predictions', 'oobstats']:
        p = pathlib.Path(f'estimparam_out.{res}')
        with open(p) as f:
            out.write(f'\n# estimparam_out.{res} #\n\n{f.read()}')
        p.unlink()
    for res in ['predweights', 'plsweights', 'plsvar', 'ooberror']:
        pathlib.Path(f'estimparam_out.{res}').unlink()
    out.flush()

# export final tables
out.write('### model choice table ###\n\nmax simulations model\n')
for lim, m in model_choice:
    out.write(f'{lim:>15} {m}\n')

out.write('\n### parameter estimation table ###\n\nparameter\texpectation\tmedia\tQ_0.05\tQ_0.95\tvariance\n')
for param in params_names:
    res = estimated_params[param]
    out.write(f'{param}\t{res["Expectation"]}\t{res["Median"]}\t{res["Quantile_0.05"]}\t{res["Quantile_0.95"]}\t{res["Variance"]}\n')
    out.flush()

out.write('finished\n')
out.close()
