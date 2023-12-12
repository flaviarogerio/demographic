"""
Remove simulation files that are smaller than the specified size.
"""

import pathlib, sys

if len(sys.argv) != 3:
    sys.exit(f'usage: {sys.argv[0]} <NUM SIMULS> <GO|DRY>')
NUM = int(sys.argv[1])
if sys.argv[2] == 'GO': GO = True
elif sys.argv[2] == 'DRY': GO = False
else: sys.exit(f'usage: {sys.argv[0]} <NUM SIMULS> <GO|DRY>')

c = 0
simuls = pathlib.Path('simuls')
for fname in sorted(simuls.glob('M*-*.txt')):
    with open(fname) as f:
        f.readline() # ignore header
        n = 0
        for line in f:
            n += 1
            if n == NUM: break
    if n < NUM:
        c += 1
        if GO:
            fname.unlink()

if GO: print('number of deleted files:', c)
else: print('number of files that would be deleted:', c)
