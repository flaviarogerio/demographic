"""
Perfom model choice and parameter fitting with the pyabcranger module.

requires: simuls/*, obs.txt
generates: ranger/*

Structure of output dir:
    - For each model choice directory:
        - results.txt with model choice (model/group, num votes, post prob for each sample size)
        - other files are output files of pyabcranger of the last sample size
"""

import pandas, numpy, pyabcranger, pathlib, yaml, simul

##############################
# import configuration files #
##############################

dst = pathlib.Path('ranger')
with open('params.yml') as f:
    cfg = yaml.load(f, yaml.Loader)
    models = simul.model_names
with open('obs.txt') as f:
    obs = {}
    for line in f:
        k, v = line.split()
        assert k not in obs
        obs[k] = float(v)
stats_names = list(obs)
statobs = numpy.array([obs[i] for i in stats_names])

#####################################################
# import all data in a single, big pandas.DataFrame #
#####################################################

df = []
models_start = {}
models_num = dict.fromkeys(models, 0)
models_params = {}
cur = 0
for m in models:
    files = sorted(pathlib.Path('simuls').glob(f'{m}-*.txt'))
    n = 0
    models_start[m] = cur
    for fname in files:
        bit = pandas.read_table(fname, dtype=float, sep=' ')
        models_num[m] += len(bit)
        df.append(bit)
        cur += len(bit)
        print(fname, models_num[m], cur)
        if m not in models_params:
            models_params[m] = set(bit.columns) - set(stats_names)
        if models_num[m] >= cfg['ranger']['nsam']: break
    if models_num[m] < cfg['ranger']['nsam']:
        raise ValueError(f'not enough replicates available for model {m}')
df = pandas.concat(df, axis=0, ignore_index=True)

# process list of parameters
params_outer = set().union(* models_params.values())
params_inner = list(params_outer.intersection(* models_params.values()))
assert params_outer == set(df.columns) - set(stats_names)
params_outer = list(params_outer)

################
# model choice #
################

overwrite_default = cfg['ranger']['modelchoice']['overwrite']
for key, config in cfg['ranger']['modelchoice']['analyses'].items():

    ### start a given analysis ###
    ###############################

    # skip if exist and should not be overwritten, overwise create
    path = dst / 'modelchoice' / key
    if path.is_dir() and config.get('overwrite', overwrite_default) == False:
        print(f'<<< {key} skipped >>>')
        continue
    path.mkdir(exist_ok=True, parents=True)

    # get list of models
    if 'models' in config and 'groups' in config:
        raise ValueError('`models` and `groups` should not be used both at the same time')
    if 'groups' in config:
        model_list = []
        group_mapping = {}
        group2index = []
        scen_list = []
        for i, (grp, pops) in enumerate(config['groups']):
            scen_list.append(grp)
            model_list.extend(pops)
            group_mapping.update(dict.fromkeys(pops, i + 1.0))
            group2index.append([model_list.index(p) for p in pops])
        assert len(model_list) == len(set(model_list))
    else:
        if config['models'] == []:
            model_list = list(models)
        else:
            model_list = config['models']
        group_mapping = None
        scen_list = model_list

    ### initialize output file ###
    ##############################
    fname = path / 'results.txt'
    with (fname).open('w') as f:
        f.write('repl. best ' + ' '.join(scen_list) + ' postp\n')

    ### process all numbers of samples ###
    ######################################
    nsams = config.get('nsam', cfg['ranger']['modelchoice']['nsam'])
    for nsam in nsams:
        print(f'\n<<<<<< analysis {key} {nsam} >>>>>>\n')

        ### subset of dataframe ###
        ###########################
        model_counts = []
        rng = []
        for m in model_list:
            n = min(nsam, models_num[m])
            rng.append((models_start[m], models_start[m]+n))
            model_counts.append(n)
        sub = pandas.concat([df[a:b] for (a,b) in rng], axis=0, ignore_index=True)

        ### data tables ####
        ####################
        stats = sub[stats_names].values
        params = sub[params_outer].values
        np = len(params_outer)
        nrec = len(stats)

        ### scenarios (models or groups) ###
        ####################################
        assert len(model_counts) == len(model_list)
        if group_mapping is None:
            scenarios = [i+1.0 for i,n in enumerate(model_counts) for _ in range(n)]
            nrecscen = model_counts
        else:
            scenarios = [group_mapping[model_list[i]] for i,n in enumerate(model_counts) for _ in range(n)]
            nrecscen = [sum(model_counts[i] for i in grp) for grp in group2index]

        ### create reference table ###
        ##############################
        rf = pyabcranger.reftable(
            nrec,
            nrecscen,
            [np] * len(scen_list),
            params_outer,
            stats_names,
            stats,
            params,
            scenarios
        )

        #### choose scenario  ###
        #########################
        postres = pyabcranger.modelchoice(rf, statobs, f"--ntree 500 --threads {cfg['nthreads']}", False)
        scen_index = postres.predicted_model[0]
        scenario = scen_index + 1
        scen_name = scen_list[scen_index]
        print('\n------> ' + scen_name + '\n')

        ### export results ###
        ######################
        votes = ' '.join(map(str, postres.votes[0]))
        postp = str(postres.post_proba[0])
        with (fname).open('a') as f:
            f.write(str(nsam))
            f.write(' ' + scen_name)
            f.write(' ' + votes)
            f.write(' ' + format(float(postp), '.4f') + '\n')

    ### save abcranger output files for last sample size ###
    ########################################################
    for ext in ['settings', 'importance', 'ooberror', 'confusion', 'lda', 'predictions']:
        pathlib.Path('modelchoice_out.' + ext).rename(path / ext)

########################
# parameter estimation #
########################

### process requested models ###
################################
for model in cfg['ranger']['estimparams']['models']:

    ### create reference table ###
    ##############################

    # parameters for this model
    params_names = list(models_params[model])

    # extract tables
    a = models_start[model]
    b = a + models_num[model]
    params = df[params_names][a:b].values
    stats = df[stats_names][a:b].values
    nrec = len(params)
    nrecscen = [nrec]

    # create reference table
    rf = pyabcranger.reftable(
        nrec,
        nrecscen,
        [len(params_names)],
        params_names,
        stats_names,
        stats,
        params,
        [1.0] * nrec
    )

    # as before, skip/create destination directory
    path = dst / 'estimparams' / model
    if path.is_dir() and cfg['ranger']['estimparams']['overwrite'] == False:
        print(f'<<< estimparams {model} skipped >>>')
        continue
    path.mkdir(exist_ok=True, parents=True)
    out = path / 'results.txt'
    with out.open('w') as f:
        f.write('param\texpect.\tmedian\tQ_0.05\tQ_0.95\tvariance\n')

    ### process all parameters for this model ###
    #############################################
    ntot = len(params_names)
    for ncur, param in enumerate(params_names):
        print(f'\n<<<<<< {model} parameter {param} ({ncur+1} of {ntot}) >>>>>>\n')

        ### run pyabcranger ###
        #######################
        param_dir = path / param
        param_dir.mkdir(exist_ok=True)
        cli_params = f"--ntree 500 --parameter {param} --threads {cfg['nthreads']} --noob 50 --chosenscen 1 --output {param_dir}/out"

        ### get results ###
        ###################
        res = pyabcranger.estimparam(rf, statobs, cli_params, False, False)
        pe = res.point_estimates[0]
        e = pe['Expectation']
        m = pe['Median']
        q5 = pe['Quantile_0.05']
        q95 = pe['Quantile_0.95']
        v = pe['Variance']
        with out.open('a') as f:
            f.write(f'{param}\t{e}\t{m}\t{q5}\t{q95}\t{v}\n')
            f.flush()
