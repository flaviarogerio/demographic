"""
Process the specified VCF file, applies the structure defined in the
sample list file and filter sites based on a set of criteria based on
parameters set in params.yaml.

Sites are counted as follows:

* excl: excluded because of missing data
* incl: included (complement)
* disc: discarded based on MAF
* mini: discarded based in missing data per population
* used: remaining sites

Used sites are grouped following the criterion:

* Same chromosome
* Site further than max_dist bp away from previous site of the window.
* Site further than max_width bp away from previous site of the window.

The windows (called "bags" in the script) are then filtered based on the
number of sites in each windows. The number of windows according to a
hardcoded set of thresholds are reported, and a given value is used to
export data in the windows/ directory. Fasta alignments are generated
by the concatenated of retained SNPs in each windows, and an info file
is exported with counters and the list of missing data proportion of
each sample.
"""

import egglib, math, yaml, pathlib
from matplotlib import pyplot

with open('params.yml') as f:
    cfg = yaml.load(f, yaml.Loader)
POPS = ['NA', 'BR', 'EU']

with open(cfg['samples']) as f:
    groups = yaml.load(f, yaml.Loader)

# open VCF
vcf = egglib.io.VCF(cfg['fname'])
samples = vcf.get_samples()

# create structure
struct = {None: {g: {n: [samples.index(n)] for n in groups[g]} for g in groups}}
struct = egglib.struct_from_dict(struct, {'OTG': [samples.index(cfg['outgroup'])]})
assert struct.get_populations() == POPS

# prepare ComputeStats
cs_dict = {}
cs_dict['all'] = egglib.stats.ComputeStats(struct=struct)
for p in POPS:
    cs_dict[p] = egglib.stats.ComputeStats(struct=struct.subset(pops=[p]))
for cs in cs_dict.values():
    cs.add_stats('maf', 'ns_site')

# process sites and create windows (or bags)
chrom = None
bags = []
excl = 0 # excluded (missing data)
incl = 0 # included (complement)
disc = 0 # discarded (MAF)
mini = 0 # discarded (missing data per pop)
used = 0 # used (complement)
while vcf.read():
    # create site
    site = ['N' if i in ([None], ['*']) else i[0] for i in vcf.get_genotypes()]
    site = egglib.site_from_list(site, egglib.alphabets.DNA)
    if site.num_missing > 100:
        excl += 1
        continue
    incl += 1

    # compute stats and skip if needed
    stats = {k: cs.process_site(site) for (k, cs) in cs_dict.items()}
    if stats['all']['maf'] < cfg['MAF']:
        disc += 1
        continue
    if min(stats[k]['ns_site'] for k in POPS) < 10:
        mini += 1
        continue

    if vcf.get_chrom() != chrom or vcf.get_pos() - pos > cfg['windows']['max_dist'] or vcf.get_pos() - bags[-1][0][1] > cfg['windows']['max_width']:
        chrom = vcf.get_chrom()
        pos = vcf.get_pos()
        bags.append([])
    pos = vcf.get_pos()
    bags[-1].append((chrom, pos, site, stats))
    used += 1

# report
report = {
    'excl': excl,
    'incl': incl,
    'disc': disc,
    'mini': mini,
    'used': used,
    'windows': {}
}
for x in 1, 2, 5, 10, 20:
    n = 0
    t = 0
    for b in bags:
        if len(b) >= x:
            n+= 1
            t += len(b)
    report['windows'][x] = {'num': n, 'tot': t}
with open('windows.yml', 'w') as f:
    yaml.dump(report, f)

# get the index of samples (to export alignments in canonical order)
d1, d2 = struct.as_dict()
idx = []
for p in POPS:
    for i in d1[None][p].values():
        idx.append(i[0])
idx.append(d2['OTG'][0])

# export windows as fasta files and mask
(pathlib.Path('windows') / 'aln').mkdir(parents=True, exist_ok=True)
(pathlib.Path('windows') / 'infos').mkdir(parents=True, exist_ok=True)
cur = 0
for win in bags:
    if len(win) >= params['windows']['min_sites']:
        cur += 1

        # create alignment
        seqs = list(map(''.join, zip(*[i[2].as_list() for i in win])))
        seqs = [seqs[i] for i in idx] # reorder samples
        with open(f'windows/aln/{cur:>03}.fas', 'w') as f:
            for seq in seqs:
                f.write(f'>\n{seq}\n')

        # export window info
        with open(f'windows/infos/{cur:>03}.txt', 'w') as f:
            f.write(f'LG={win[0][0]} first={win[0][1]+1} last={win[-1][1]+1} L={win[-1][1]-win[0][1]+1}\n')
            for seq in seqs:
                N = seq.count('N') / len(seq)
                f.write(str(N) + '\n')

