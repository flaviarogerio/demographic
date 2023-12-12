"""
Extract sites from VCF.

* Requires: VCF file and YAML file with samples per population
* Generates:
    * sites.yml with values:
        * total: total number of sites in VCF
        * maf: sites excluded / maf filter
        * missing: sites excluded / missing data filter
        * multi: sites excluded / more than 2 alleles
        * excl: total number of sites excluded
        * pass: sites passing filters (before thinning)
        * final: number of sites exported
    * sites.txt with, for each site:
        * contig name
        * position in contig
        * non-missing samples in NA
        * non-missing samples in BR
        * non-missing samples in EU
        * site string
"""

import yaml, egglib, re

dst = 'sites.txt'
yml = 'sites.yml'

# import parameters
with open('params.yml') as f:
    cfg = yaml.load(f, yaml.Loader)

# read manually VCF file to get list of contigs and their length
contigs = []
with open(cfg['fname']) as f:
    for line in f:
        if line[:2] != '##': break
        if mo := re.match('##contig=<ID=(.+),length=(\d+)>', line):
            ctg, ln = mo.groups()
            ln = int(ln)
            contigs.append((ctg, ln))

# open VCF
vcf = egglib.io.VCF(cfg['fname'])

# create structure
with open(cfg['samples']) as f:
    samples = yaml.load(f, yaml.Loader)
pops = {pop: len(samples[pop]) for pop in samples}
vcf_samples = vcf.get_samples()
struct1 = {None: {g: {n: [vcf_samples.index(n)] for n in lst} for g,lst in samples.items()}}
struct1 = egglib.struct_from_dict(struct1, {cfg['outgroup']: [vcf_samples.index(cfg['outgroup'])]})
assert set(struct1.get_populations()) == set(samples)

# create second structure with the individuals in grouped by population
struct2 = egglib.struct_from_samplesizes([len(samples[p]) for p in ['NA', 'BR', 'EU']], ploidy=1, outgroup=1)

# prepare ComputeStats
cs_dict = {}
cs_dict['all'] = egglib.stats.ComputeStats(struct=struct1)
cs_dict['all'].add_stats('maf', 'Aing')
for pop in samples:
    cs_dict[pop] = egglib.stats.ComputeStats(struct=struct1.subset(pops=[pop]))
for cs in cs_dict.values():
    cs.add_stats('ns_site')

# process all sites of the VCF
counts = {'total': 0, 'maf': 0, 'missing': 0, 'multi': 0, 'excl': 0, 'pass': 0, 'final': 0}
print('      ', end='')
with open(dst, 'w') as f:
    while vcf.read():
        counts['total'] += 1

        # get site
        site = ['N' if i in ([None], ['*']) else i[0] for i in vcf.get_genotypes()]
        site = egglib.site_from_list(site, egglib.alphabets.DNA)

        # check that all populations have enough samples
        good = True
        ns = {}
        for pop, lst in samples.items():
            stats = cs_dict[pop].process_site(site)
            avail_prop = stats['ns_site'] / len(lst)
            if avail_prop < cfg['sites']['min_avail_prop']:
                good = False
                counts['missing'] += 1
                break
            else:
                ns[pop] = stats['ns_site']

        # check that minor allele frequency is above MAF filter
        stats = cs_dict['all'].process_site(site)
        if stats['Aing'] > 2:
            good = False
            counts['multi'] += 1
        elif stats['maf'] < cfg['maf']:
            good = False
            counts['maf'] += 1

        # skip if not passing filters
        if not good:
            counts['excl'] += 1
            continue
        else:
            counts['pass'] += 1

            # save site
            if counts['pass'] % cfg['sites']['thin'] == 0:
                counts['final'] += 1
                print('\b'*6 + format(counts['final'], '>6'), end='', flush=True)

                # save site in the order corresponding to struct2
                site_lst = []
                ing, otg = struct1.as_dict()
                for p in ['NA', 'BR', 'EU']:
                    for idx in ing[None][p].values():
                        site_lst.append(site[idx[0]])
                site_lst.append(site[otg[cfg['outgroup']][0]])
                f.write(f'{vcf.get_chrom()} {vcf.get_pos()+1} {ns["NA"]} {ns["BR"]} {ns["EU"]} {"".join(site_lst)}\n')
 
with open(yml, 'w') as f:
    report = {'struct': struct2.as_dict(), 'counts': counts, 'ns': pops}
    yaml.dump(report, f, yaml.Dumper)

print('\b'*6, end='')
print(counts)
