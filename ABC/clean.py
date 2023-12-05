import pathlib, sys

if len(sys.argv) != 3:
    sys.exit(f'usage: {sys.argv[0]} <NUM SIMULS> <GO|DRY>')
NUM = int(sys.argv[1])
if sys.argv[2] == 'GO': GO = True
elif sys.argv[2] == 'DRY': GO = False
else: sys.exit(f'usage: {sys.argv[0]} <NUM SIMULS> <GO|DRY>')

c = 0
simuls = pathlib.Path('simuls')
for fname1 in sorted(simuls.glob('M*-*_p.txt')):
    with open(fname1) as f:
        f.readline() # ignore header
        n1 = 0
        for line in f:
            n1 += 1
            if n1 == NUM: break
    fname2 = pathlib.Path(str(fname1)[:-5] + 's.txt')
    with open(fname2) as f:
        f.readline() # ignore header
        n2 = 0
        for line in f:
            n2 += 1
            if n2 == NUM: break
    print(fname1, n1, n2)
    if n1 < NUM or n2 < NUM:
        c += 1
        if GO:
            fname1.unlink()
            fname2.unlink()

if GO: print('number of deleted files:', c)
else: print('number of files that would be deleted:', c)
