"""
Perfom model choice and parameter fitting with the pyabcranger module.

requires: simuls/*, obs.txt
generates: ranger/*
"""

import pandas, numpy, pyabcranger, pathlib, yaml, click, sys, os

@click.command(no_args_is_help=True)
@click.option('-d', '--dry-run', is_flag=True, default=False, help='List the analyses that would be performed.')
@click.option('-m', '--modelchoice', 'task', flag_value='mc', default=True)
@click.option('-e', '--estimparams', 'task', flag_value='ep')
@click.argument('tasks', nargs=-1)
def main(dry_run, task, tasks):
    """
    Perform RF analyses.

    Arguments: for modelchoice: which of the analyses to perform among
               those defined in params.yml (default: all of them); for
               estimparams: list of models to process (default: list
               in param.yml).
    """

    config() # load configuration

    # modelchoice
    if task == 'mc':
        # edit list of analyses
        if len(tasks) != 0:
            if (set(tasks) <= set(cfg['modelchoice']['analyses'])) == False:
                raise ValueError('invalid tasks')
            cfg['modelchoice']['analyses'] = {k: v for k, v in cfg['modelchoice']['analyses'].items() if k in tasks}

        # find maximum number of requested samples
        nsam = max(cfg['modelchoice']['nsam'])

        # find list of requested models
        models = set()
        for pars in cfg['modelchoice']['analyses'].values():
            try: models.update(pars['models'])
            except KeyError:
                for grp in pars['groups']: models.update(pars[grp])

        # load data in a big pandas.DataFrame
        if not dry_run: load(nsam, models)

        # call method
        modelchoice(dry_run)

    # estimparams
    else:

        # edit list of analyses
        if len(tasks) == 0:
            tasks = cfg['estimparams']['models']

        # process models
        for model in tasks:
            print(f'- model: {model}')
            estimparams(dry_run, model)

#######################
# configuration files #
#######################

def config():
    global destination_path, cfg, stats_names, stats_obs
    destination_path = pathlib.Path('ranger')
    with open('params.yml') as f:
        cfg = yaml.load(f, yaml.Loader)
    with open('obs.txt') as f:
        obs = {}
        for line in f:
            k, v = line.split()
            assert k not in obs
            obs[k] = float(v)
    stats_names = list(obs)
    stats_obs = numpy.array([obs[i] for i in stats_names])

#####################################################
# import all data in a single, big pandas.DataFrame #
#####################################################

def load(nsam, models):
    global df, models_start, params_outer
    df = []
    models_start = {}
    models_num = dict.fromkeys(models, 0)
    models_params = {}
    cur = 0
    print('loading:', end='', flush=True)
    for m in sorted(models):
        print(' ' + m, end='', flush=True)
        files = sorted(pathlib.Path('simuls').glob(f'{m}-*.txt'))
        models_start[m] = cur
        for fname in files:
            bit = pandas.read_table(fname, dtype=float, sep=' ')
            models_num[m] += len(bit)
            df.append(bit)
            cur += len(bit)
            if m not in models_params:
                models_params[m] = set(bit.columns) - set(stats_names)
            if models_num[m] >= nsam: break
        if models_num[m] < nsam:
            raise ValueError(f'not enough replicates available for model {m}')
    df = pandas.concat(df, axis=0, ignore_index=True)
    print(f' done ({len(df)} samples)')

    # process list of parameters
    params_outer = set().union(* models_params.values())
    params_inner = list(params_outer.intersection(* models_params.values()))
    assert params_outer == set(df.columns) - set(stats_names)
    params_outer = list(params_outer)

################
# model choice #
################

def modelchoice(dry_run):

    # dictionary of main output files
    output = {}
    for key in cfg['modelchoice']['analyses']:
        output[key] = destination_path / 'modelchoice' / key / 'results.txt'

    # iterate over sample sizes first
    for nsam in cfg['modelchoice']['nsam']:

        # process all analyses for this sample size
        for key, pars in cfg['modelchoice']['analyses'].items():
            if 'models' in pars and 'groups' in pars: raise ValueError('models and groups are mutually exclusive!')

            # skip analysis if directory already present
            dst = destination_path / 'modelchoice' / key / str(nsam)
            if dst.is_dir() and not cfg['modelchoice']['overwrite']:
                print(f'{dst}; skipped')
                continue
            print(f'- {dst}')

            # skip anyway if dry run
            if dry_run: continue

            # create directory
            dst.mkdir(exist_ok=True, parents=True)

            # get list of groups
            if 'groups' in pars:
                model_list = [] # flat list of models
                group_list = [] # list of groups (to ensure order is respected
                group_codes = {} # scenario ID for each model (identify which group
                for i, grp in enumerate(pars['groups']):
                    group_list.append(grp)
                    model_list.extend(pars[grp])
                    for model in pars[grp]: group_codes[model] = float(i+1)
            else: # each model is treated as a group
                model_list = pars['models']
                group_list = model_list
                group_codes = {model: float(i+1) for i, model in enumerate(model_list)}
            assert len(model_list) == len(set(model_list)) # check that all models are used once

            # subset of dataframe
            subset = []
            scenarios = []
            for m in model_list:
                subset.append(df[models_start[m]:models_start[m]+nsam])
                scenarios.extend([group_codes[m]] * nsam)
            subset = pandas.concat(subset, axis=0, ignore_index=True)

            # extract data tables
            stats = subset[stats_names].values
            params = subset[params_outer].values
            np = len(params_outer)
            nrec = len(stats)

            # scenario counts
            nrecscen = [scenarios.count(code) for code in sorted(set(scenarios))]

            # create reference table
            rf = pyabcranger.reftable(
                nrec,
                nrecscen,
                [np] * len(group_list),
                params_outer,
                stats_names,
                stats,
                params,
                scenarios
            )

            # disable stdout
            stdout = sys.stdout
            sys.stdout = open(os.devnull, "w")

            # choose scenario
            postres = pyabcranger.modelchoice(rf, stats_obs, f"--ntree 500 --threads {cfg['nthreads']} --output {dst / 'out'}", False)
            sys.stdout = stdout

            best = postres.predicted_model[0]
            best_name = group_list[best]

            # export results
            votes = ' '.join(map(str, postres.votes[0]))
            postp = str(postres.post_proba[0])
            with output[key].open('a') as f:
                f.write(str(nsam))
                f.write(' ' + best_name)
                f.write(' ' + votes)
                f.write(' ' + format(float(postp), '.4f') + '\n')

########################
# parameter estimation #
########################

def estimparams(dry_run, model):

    path = pathlib.Path('ranger') / 'estimparams' / model
    if path.is_dir() and cfg['estimparams']['overwrite'] == False:
        print('    skipped')
        return
    if dry_run:
        return

    # load dataframe
    files = sorted(pathlib.Path('simuls').glob(f'{model}-*.txt'))
    df = []
    c = 0
    for fname in files:
        df.append(pandas.read_table(fname, dtype=float, sep=' '))
        c += len(df[-1])
        if c >= cfg['estimparams']['nsam']: break
    if c < cfg['estimparams']['nsam']:
        raise ValueError(f'not enough replicates available for model {model}')
    df = pandas.concat(df, axis=0, ignore_index=True)
    print(f'    {len(df)} samples')

    # create reference table
    params_names = list(set(df.columns) - set(stats_names))

    # extract tables
    params = df[params_names].values
    stats = df[stats_names].values
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

    # create destination directory and create output file
    path.mkdir(exist_ok=True, parents=True)
    with (path / 'results.txt').open('w') as f:
        f.write('param\texpect.\tmedian\tQ_0.05\tQ_0.95\tvariance\n')

        # process all parameters for this model
        ntot = len(params_names)
        print('    [' + ' ' * ntot + ']' + '\b' * (ntot+1), end='', flush=True)
        for ncur, param in enumerate(params_names):
            dst = path / param
            dst.mkdir(exist_ok=True)

            # run pyabcranger
            param_dir = path / param
            param_dir.mkdir(exist_ok=True)
            cli_params = f"--ntree 500 --parameter {param} --threads {cfg['nthreads']} --noob 50 --chosenscen 1 --output {dst / 'out'}"
            stdout = sys.stdout
            sys.stdout = open(os.devnull, "w")
            res = pyabcranger.estimparam(rf, stats_obs, cli_params, False, False)
            sys.stdout = stdout

            # get results
            pe = res.point_estimates[0]
            e = pe['Expectation']
            m = pe['Median']
            q5 = pe['Quantile_0.05']
            q95 = pe['Quantile_0.95']
            v = pe['Variance']
            f.write(f'{param}\t{e}\t{m}\t{q5}\t{q95}\t{v}\n')
            f.flush()
            print('+', end='', flush=True)
    print('] done')

# launch main function
main()
