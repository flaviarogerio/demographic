"""
Utility script to monitor progress of simulation script.
"""

import yaml, click, pathlib, simul, subprocess
from threading import Event
import signal

# get configuration
with open('params.yml') as f:
    cfg = yaml.load(f, yaml.Loader)

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
    for it in range(stop):
        print(f'[{it+1}/{stop}]')
        res = subprocess.run(['wc', '-l'] + [str(p) for p in path.glob(f'*-*.txt')], stdout=subprocess.PIPE)
        if res.returncode != 0:
            break
        counts = {m: [] for m in models}
        for line in res.stdout.decode().split('\n'):
            n, name = line.split()
            if name == 'total': break
            n = int(n) - 1
            m = pathlib.Path(name).name.split('-')[0]
            counts[m].append(n)
        print(f'{"model":>8} {"files":>5}:{"repets":>7} + {"completed files":>15}')
        for m in models:
            nf1 = 0
            nf2 = 0
            nr1 = 0
            nr2 = 0
            for n in counts[m]:
                nf1 += 1
                nr1 += n
                if n == expect:
                    nf2 += 1
                    nr2 += n
            print(f'{m:>8} {nf1:>5}:{nr1:>7} | {nf2:>7}:{nr2:>7}')
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
