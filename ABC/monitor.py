"""
Utility script to monitor progress of simulation script.
"""

import yaml, click, pathlib, simul, subprocess
from threading import Event
import signal

# get configuration
with open('params.yml') as f:
    cfg = yaml.load(f, yaml.Loader)
cachef = pathlib.Path('monitor.yml')

# main function
def monitor(delay, stop):

    # stuff to allow quitting immediately when 'q' is pressed
    exit_event = Event()
    def quit(signo, _frame):
        print('\b\b', end='')
        exit_event.set()
    signal.signal(signal.SIGTERM, quit)
    signal.signal(signal.SIGHUP, quit)
    signal.signal(signal.SIGINT, quit)

    # check arguments and collect more parameters
    if delay < 1:
        raise click.ClickException(f'delay too small: {delay}')
    expect = cfg['simul']['szbatch']
    if cfg['simul']['models'] == []:
        models = simul.model_names
    else:
        models = cfg['simul']['models']
    path = pathlib.Path('simuls')

    # enter iteration
    for it in range(stop):
        print(f'[{it+1}/{stop}]', end='', flush=True)

        # load cached data
        if cachef.is_file():
            with open(cachef) as f:
                cache = yaml.load(f, yaml.Loader)
        else:
            cache = dict()

        # process all files found in simuls/ dict, and check number of lines if file has changed
        for p in sorted(path.glob(f'*-*.txt')):
            sz = p.stat().st_size
            if p in cache:
                assert sz >= cache[p][0]
            if p not in cache: cache[p] = [0, 0, 0]
            if sz != cache[p][0]:
                res = subprocess.run(['wc', '-l', str(p)], stdout=subprocess.PIPE).stdout
                ln = int(res.split()[0])
                if ln > 0: ln -= 1
                print('.', end='', flush=True)
                cache[p] = [sz, ln, ln-cache[p][2]]
            else:
                cache[p][2] = 0
        print()

        # save data
        with open(cachef, 'w') as f:
            yaml.dump(cache, f)

        # sort data per models
        counts = {m: [[], 0] for m in models}
        for (p, (sz, ln, diff)) in cache.items():
            m, idx = p.stem.split('-')
            counts[m][0].append(ln)
            counts[m][1] += diff

        print(f'{"model":>8} | {"files":>5} | {"repets":>7} | {"completed files":>17} |    diff')
        for m in models:
            nf1 = 0
            nf2 = 0
            nr1 = 0
            nr2 = 0
            cnt, diff = counts[m]
            for n in cnt:
                nf1 += 1
                nr1 += n
                if n == expect:
                    nf2 += 1
                    nr2 += n
            print(f'{m:>8} | {nf1:>5} | {nr1:>7} | {nf2:>7} | {nr2:>7} | {diff:+7d}')
        else:
            # loop control
            if it == stop - 1: break
            print(f'(waiting {delay}s)')
            exit_event.wait(delay)
            if exit_event.is_set(): break
            continue
        break # break if models loop was broken

# add program documentation
monitor.__doc__ = __doc__

# add click interface
monitor = click.command(no_args_is_help=True)(
    click.option('-d', '--delay', type=int, default=1, show_default=True, help='delay between updates') (
    click.option('-s', '--stop', type=int, default=1000, show_default=True, help='maximum number of iterations')
        (monitor)))

# call program method
monitor()
