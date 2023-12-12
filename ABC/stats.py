"""
By default (if executed), process the sites in sites.txt, compute stats
and export results in obs.txt.

If imported, expose a Cstats class which can be used to process
simulated datasets.

* always:
    * requires sites.yml
* only if executed:
    * requires sites.txt
    * generates obs.txt
"""

import pathlib, egglib, sys, re, yaml

# configuration
sites_txt = 'sites.txt'
sites_yml = 'sites.yml'
dst = 'obs.txt'

# load parameters
with open('params.yml') as f:
    cfg = yaml.load(f, yaml.Loader)

# main function (which is run only if the script is executed)
def main():
    cs = Cstats()
    for site in import_obs():
        cs.process(site)
    results = cs.results()
    with open(dst, 'w') as f:
        for k in sorted(results):
            f.write(f'{k:>22}  {results[k]:.5f}\n')
            print(f'{k:>22}  {results[k]:.5f}')

# import sites from observed dataset, as an iterable yielding Site instances
def import_obs():
    static_site = egglib.Site()
    with open(sites_txt) as f:
        for line in f:
            ctg, pos, NA, BR, EU, site = line.split()
            static_site.from_list(site, alphabet=egglib.alphabets.DNA)
            yield static_site

# module API
class Cstats:
    """
    To use this class:
        - create an instance: cs = stats.Cstats()
            - the structure is read from sites.yml
        - pass any number of sites matching the structure: cs.load(site)
        - get the statistics: cs.results()
    """

    def __init__(self):
        # load structure
        with open(sites_yml) as f:
            cfg = yaml.load(f, yaml.Loader)
            struct = egglib.struct_from_dict(*cfg['struct'])

        # create ComputeStats instances for all levels and scopes
        self.cs_dict = {
            'all': egglib.stats.ComputeStats(struct=struct, multi=True),
            'pop:NA': egglib.stats.ComputeStats(struct=struct.subset(pops=['pop1']), multi=True),
            'pop:BR': egglib.stats.ComputeStats(struct=struct.subset(pops=['pop2']), multi=True),
            'pop:EU': egglib.stats.ComputeStats(struct=struct.subset(pops=['pop3']), multi=True),
            'pair:NA-BR': egglib.stats.ComputeStats(struct=struct.subset(pops=['pop1', 'pop2']), multi=True),
            'pair:NA-EU': egglib.stats.ComputeStats(struct=struct.subset(pops=['pop1', 'pop3']), multi=True),
            'pair:BR-EU': egglib.stats.ComputeStats(struct=struct.subset(pops=['pop2', 'pop3']), multi=True)
        }

        # specify lists of stats
        self.cs_dict['all'].add_stats('thetaW', 'Pi', 'D', 'Hsd', 'FstWC', 'Dj')
        for key in 'pop:NA', 'pop:BR', 'pop:EU':
            self.cs_dict[key].add_stats('thetaW', 'Pi', 'D', 'Hsd')
        for key in 'pair:NA-BR', 'pair:NA-EU', 'pair:BR-EU':
            self.cs_dict[key].add_stats('Dxy', 'Da', 'numSpd', 'numShA', 'numShP', 'FstWC', 'Dj')

    def process(self, site):
        for cs in self.cs_dict.values():
            cs.process_site(site)

    def results(self):
        return {f'{key}:{stat}': val for key, cs in self.cs_dict.items() for stat, val in cs.results().items() }

# trigger main function
if __name__ == '__main__':  main()
