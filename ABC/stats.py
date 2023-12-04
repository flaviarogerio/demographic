"""
Process the VCF file to compute observed values of statistics
"""

import pathlib, egglib, sys, re, yaml

with open('params.yml') as f:
    cfg = yaml.load(f, yaml.Loader)

# configurable parameters
N_NA = 46
N_BR = 20
N_EU = 141

# main function
def main():
    ds, ls = import_obs()
    cs = Cstats()
    cs.init()
    for aln, L in zip(ds, ls): cs.process(aln, L)
    stats = cs.compute()
    with open('obs.txt', 'w') as f:
        for k in sorted(stats):
            f.write(f'{k:>22}  {stats[k]:.4f}\n')
            print(f'{k:>22}  {stats[k]:.4f}')

# import windows from observed dataset
def import_obs():
    ds = []
    ls = []
    with open('windows.yml') as f:
        wins = yaml.load(f, yaml.Loader)
    n = wins['windows'][5]['num']
    for i in range(n):
        ds.append( egglib.io.from_fasta(f'windows/aln/{i+1:>03}.fas', alphabet=egglib.alphabets.DNA) )
        with open(f'windows/infos/{i+1:>03}.txt') as f:
            L = int(re.match('LG=contig_\d+ first=\d+ last=\d+ L=(\d+)', f.readline()).group(1))
            ls.append(L)
    return ds, ls

# class for computing stats from observed/simulated stats
class Cstats:
    def __init__(self):
        # create ComputeStats instances for all levels and scopes
        struct = egglib.struct_from_samplesizes([cfg['N_NA'], cfg['N_BR'], cfg['N_EU']], ploidy=1, outgroup=1)
        self.cs_dict = { 'sites': {}, 'regions': {} }
        self.cs_dict['sites']['all'] = egglib.stats.ComputeStats(struct=struct, multi=True)
        self.cs_dict['regions']['all'] = egglib.stats.ComputeStats(struct=struct, multi=False)
        self.cs_dict['sites']['pop:NA'] = egglib.stats.ComputeStats(struct=struct.subset(pops=['pop1']), multi=True)
        self.cs_dict['sites']['pop:BR'] = egglib.stats.ComputeStats(struct=struct.subset(pops=['pop2']), multi=True)
        self.cs_dict['sites']['pop:EU'] = egglib.stats.ComputeStats(struct=struct.subset(pops=['pop3']), multi=True)
        self.cs_dict['regions']['pop:NA'] = egglib.stats.ComputeStats(struct=struct.subset(pops=['pop1']), multi=False)
        self.cs_dict['regions']['pop:BR'] = egglib.stats.ComputeStats(struct=struct.subset(pops=['pop2']), multi=False)
        self.cs_dict['regions']['pop:EU'] = egglib.stats.ComputeStats(struct=struct.subset(pops=['pop3']), multi=False)
        self.cs_dict['sites']['pair:NA-BR'] = egglib.stats.ComputeStats(struct=struct.subset(pops=['pop1', 'pop2']), multi=True)
        self.cs_dict['sites']['pair:NA-EU'] = egglib.stats.ComputeStats(struct=struct.subset(pops=['pop1', 'pop3']), multi=True)
        self.cs_dict['sites']['pair:BR-EU'] = egglib.stats.ComputeStats(struct=struct.subset(pops=['pop2', 'pop3']), multi=True)

        # specify list of stats
        self.stats_R = 'Ki', 'R2', 'Ch'
        self.stats_S = 'thetaW', 'Pi', 'D', 'Hsd', 'S'
        self.stats_Spairwise = 'Dxy', 'Da', 'numSpd', 'numShA', 'numShP', 'FstWC', 'Dj'
        self.cs_dict['sites']['all'].add_stats('FstWC', 'Dj')
        for key in 'all', 'pop:NA', 'pop:BR', 'pop:EU':
            self.cs_dict['sites'][key].add_stats(*self.stats_S)
            self.cs_dict['regions'][key].add_stats(*self.stats_R)
            self.cs_dict['regions'][key].add_stats('S', 'Pi')
        for key in 'pair:NA-BR', 'pair:NA-EU', 'pair:BR-EU':
            self.cs_dict['sites'][key].add_stats(*self.stats_Spairwise)

    def init(self):
        # initialize per-region stats (will be incremented and average will be computed)
        self.results = {}
        self.counts = {}
        for key in 'all', 'pop:NA', 'pop:BR', 'pop:EU':
            for s in self.stats_R:
                self.results[f'{key}_{s}'] = 0
            self.results[f'{key}_KoS'] = 0
            self.results[f'{key}_KoP'] = 0
            self.counts[key] = 0

    def process(self, aln, L):
        # iterate over regions
        for cs in self.cs_dict['sites'].values():
            cs.process_align(aln, max_missing=1)
        for key, cs in self.cs_dict['regions'].items():
            stats = cs.process_align(aln, max_missing=1)
            if stats['S'] is None or stats['S'] == 0:
                continue
            self.counts[key] += 1
            for k, v in stats.items():
                if k not in {'S', 'Pi'}:
                    self.results[f'{key}_{k}'] += v
            self.results[f'{key}_KoS'] += stats['Ki'] / stats['S']
            self.results[f'{key}_KoP'] += stats['Ki'] / stats['Pi']

    def compute(self):
        ## finalize ##
        # compute  statistics per site
        for key, cs in self.cs_dict['sites'].items():
            for k, v in cs.results().items():
                if v is None: return None
                self.results[f'{key}_{k}'] = float(v)

        # compute per-region averages
        for lvl in 'all', 'pop:NA', 'pop:BR', 'pop:EU':
            for s in self.stats_R:
                self.results[f'{lvl}_{s}'] /= self.counts[lvl]
            self.results[f'{lvl}_KoS'] /= self.counts[lvl]
            self.results[f'{lvl}_KoP'] /= self.counts[lvl]

        return self.results

# trigger main function
if __name__ == '__main__':  main()
