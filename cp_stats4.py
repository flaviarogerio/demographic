"""
Process the VCF file to compute observed values of statistics and
estimate misorientation rate
"""

import egglib

##### PARAMETERS AND CONFIGURATION #####################################

fname = '/home/flavia/flavia_data2/2023/demography/egglib/filtered_genotyped_combined_outgroup_208samples_pass_filter5_renamed.vcf'

NAM_list = ['A-50010-1', 'A-50010-3', 'A-50010-4', 'A-50036-2',
            'A-50201-1-1', 'A-50638-1', 'A-50652-1', 'A-52339-1',
            'A-52621-1', 'CA-CHAT-1', 'CA-CHAT-3', 'CA-N0L-1',
            'CA-N0L-3', 'CA-N0P-1', 'CA-N0P-3', 'CA-N8H', 'CA-N8H-2',
            'CA-N8H-3', 'CA-N8H-5', 'CA-N8H-7', 'CA-N8H-8', 'CA-NOL-11',
            'CA-NOP1-J0-1', 'CA-NOP_2CO', 'CA-NOP_2CO-12',
            'CA-NOP_2CO-5', 'CA-NOP_2CO-7', 'CA-NOP_2CO-9',
            'CA-NOR-1B0-6', 'I-61851', 'M2.001', 'M55901-1',
            'M9.001', 'MKy7', 'N-68735-17', 'N-68735-1',
            'NRRL13649', 'NRRL47509', 'NRRL47511', 'Cg151NY82']

BR_list = ['BR-19920-1', 'BR-40000-1', 'BR-73000-1', 'BR-73800-1',
           'BR-73850-1', 'BR-75800-1', 'BR-75900-1', 'BR-75960-1',
           'BR-76170-2', 'BR-76170-3', 'BR-79550-1', 'BR-85807-1',
           'BR-85925-1', 'BR-85925-2', 'BR-85955-2', 'BR-87120-1',
           'BR-98250-1', 'BR-98290-1', 'CG-1P_1M', 'JAB2', 'M5.001']

EUR_list = ['ARG-2301-11', 'ARG-2306-1', 'ARG-2349-1', 'ARG-2349-3',
            'ARG-2700-1', 'ARG-2700-2', 'ARG-2700-5', 'ARG-2700-6',
            'ARG-5133-12', 'ARG-5133-14', 'ARG-5133-2',
            'ARG-5133-21', 'ARG-5133-23', 'ARG-5133-25-1',
            'ARG-5133-27-1', 'ARG-5133-28-2', 'ARG-X5196-1',
            'ARG-X5196-4', 'CBS252.59',
            'CR-10342-4', 'CR-10342-7', 'CR-10344-2', 'CR-10360-1',
            'CR-10360-6', 'CR-10370-50', 'CR-10370-68',
            'CR-10370-75', 'CR-10370-81', 'CR-31511-1', 'CR-31511-8',
            'CR-34000-1', 'CR-34000-3', 'CR-34310-2', 'CR-34543-10',
            'CR-34543-1', 'CR-34543-4', 'CR-34543-5', 'CR-34550-2',
            'CR-35214-1', 'CR-35430-1', 'CR-35430-2', 'CR-42223-13',
            'CR-42223-3', 'CR-42230-1', 'CR-42230-5', 'CR-42230-9',
            'CR-43000-1', 'CR-43280-1', 'CR-43380-1', 'CR-43500-11',
            'CR-43500-13', 'CR-43500-2', 'CR-43500-4', 'CR-43500-9',
            'CR-43532-2', 'CR-49284-5', 'CRO-I-35', 'DMSZ-63127',
            'F-40300-1', 'F-40300-2', 'F-40400-1', 'F-40400-2',
            'F-40400-3', 'F-40400-5', 'F-40400-6', 'F-40400-8B',
            'F-40400-9', 'F-64330-1', 'F-64330-12', 'F-64330-13B',
            'F-64330-15', 'F-64330-17', 'F-64330-20', 'F-64330-21',
            'F-64330-4', 'F-64330-8', 'F-64330-9', 'F-64370-1',
            'F-64370-2', 'F-64410-1', 'F-64410-11', 'F-64410-18',
            'F-64410-20', 'F-64410-4', 'F-64410-7', 'F-64410-8',
            'FBH-76290', 'P-7565-072-1', 'P-7565-072-8', 'SI-9223-1',
            'SI-9223-3', 'SP-36820-5', 'SW-8046-1', 'SW-8046-11',
            'SW-8046-3B', 'SW-8046-6', 'SW-8046-8', 'SW-8046-9',
            'Sl-9000-1B', 'Sl-9253-1']

OUTGROUP = 'C_navitas'

#### OPEN VCF FILE AND DEFINE STRUCTURE OBJECT #########################

VCF = egglib.io.VCF(fname)
samples = VCF.get_samples() # extract list of sample names
def find_idx(names):
    res = []
    for name in names:
        if name in samples: res.append(samples.index(name))
        else: print('missing:', name)
    return res

NAM_idx = find_idx(NAM_list)
EUR_idx = find_idx(EUR_list)
BR_idx = find_idx(BR_list)
OTG_idx = samples.index(OUTGROUP)

log = open('results.txt', 'w')
log.write(f'NAM population: listed={len(NAM_list)} found={len(NAM_idx)}\n')
log.write(f'EUR population: listed={len(EUR_list)} found={len(EUR_idx)}\n')
log.write(f'BR population: listed={len(BR_list)} found={len(BR_idx)}\n')

struct = egglib.struct_from_dict(
    {None: { # ingroup with a single cluster
        'NAM': {f'NAM{i+1}': [idx] for [i, idx] in enumerate(NAM_idx)},
        'EUR': {f'EUR{i+1}': [idx] for [i, idx] in enumerate(EUR_idx)},
        'BR': {f'BR{i+1}': [idx] for [i, idx] in enumerate(BR_idx)}
    }},
    { 'OTG': [OTG_idx] } # outgroup with a single (haploid) individual
)

assert struct.get_populations() == ['NAM', 'EUR', 'BR']

##### CREATE COMPUTESTATS OBJECTS ######################################

cs_dict = {
    'all': egglib.stats.ComputeStats(struct=struct, multi=True, triconfig_min=10),
    'NAM': egglib.stats.ComputeStats(struct=struct.subset(pops=['NAM']), multi=True),
    'EUR': egglib.stats.ComputeStats(struct=struct.subset(pops=['EUR']), multi=True),
    'BR': egglib.stats.ComputeStats(struct=struct.subset(pops=['BR']), multi=True),
    'NAM-EUR': egglib.stats.ComputeStats(struct=struct.subset(pops=['NAM', 'EUR']), multi=True),
    'NAM-BR': egglib.stats.ComputeStats(struct=struct.subset(pops=['NAM', 'BR']), multi=True),
    'EUR-BR': egglib.stats.ComputeStats(struct=struct.subset(pops=['EUR', 'BR']), multi=True)}
cs_dict['all'].add_stats('triconfig')
for key in 'all', 'NAM', 'EUR', 'BR':
    cs_dict[key].add_stats('thetaW', 'Pi', 'D', 'Dfl', 'F', 'Hsd')
for key in 'all', 'NAM-EUR', 'NAM-BR', 'EUR-BR':
    cs_dict[key].add_stats('FstWC', 'Dj')
for key in 'NAM-EUR', 'NAM-BR', 'EUR-BR':
    cs_dict[key].add_stats('Dxy', 'Da', 'numSpd', 'numShA', 'numShP')
for cs in cs_dict.values():
    cs.add_stats('nseff', 'nseffo', 'lseff', 'lseffo', 'S', 'So')

##### COMPUTE STATISTICS FROM ALL SITES ################################
##### first, without filtering, then with filtering ####################

site = egglib.Site()
cs_site = egglib.stats.ComputeStats(struct=struct)
cs_site.add_stats('Atot', 'Aing', 'ns_site', 'ns_site_o')

for spacer in [0, 100000, 200000, 500000]:
    log.write(f'\n*** minimal spacer: {spacer} ***\n\n')
    VCF = egglib.io.VCF(fname)
    ctg = None

    n1 = 0
    n3 = 0
    n4 = 0
    while VCF.read():
        if VCF.get_chrom() != ctg:
            ctg = VCF.get_chrom()
            last = -spacer-1
        if VCF.get_pos() < last+spacer:
            continue
        last = VCF.get_pos()
        genos = ['N' if i in ([None], ['*']) else i[0] for i in VCF.get_genotypes()]
        site.from_list(genos, egglib.alphabets.DNA)
        for cs in cs_dict.values():
            cs.process_site(site)

        # computing misorientation rate
        res = cs_site.process_site(site)
        if res['Aing'] == 2 and res['Atot'] > 2:
            sys.exit('STOP! third allele in outgroup found!')
        if res['Aing'] == 3: n3 += 1
        if res['Aing'] == 4: n4 += 1
        if res['Aing'] == 1 and res['Atot'] == 2: n1 += 1

    stats = {}
    for key, cs in cs_dict.items():
        log.write(f'{key}\n')
        for stat, value in cs.results().items():
            log.write(f'    {stat}: {value}\n')
            stats[f'{key}_{stat}'] = value
    print('number of polymorphic sites:', stats['all_S'], 'three alleles:', n3, 'four alleles:', n4, 'fixed with mutation in outgroup:', n1)

    with open(f'obs_spacer_{spacer}.txt', 'w') as f:
        header = 'all_Dj all_Hsd all_F all_Pi all_D all_Dfl all_FstWC all_thetaW NAM_Hsd NAM_F NAM_Pi NAM_D NAM_Dfl NAM_thetaW EUR_Hsd EUR_F EUR_Pi EUR_D EUR_Dfl EUR_thetaW BR_Hsd BR_F BR_Pi BR_D BR_Dfl BR_thetaW NAM-EUR_numShP NAM-EUR_numSpd NAM-EUR_Da NAM-EUR_Dj NAM-EUR_Dxy NAM-EUR_numShA NAM-EUR_FstWC NAM-BR_numShP NAM-BR_numSpd NAM-BR_Da NAM-BR_Dj NAM-BR_Dxy NAM-BR_numShA NAM-BR_FstWC EUR-BR_numShP EUR-BR_numSpd EUR-BR_Da EUR-BR_Dj EUR-BR_Dxy EUR-BR_numShA EUR-BR_FstWC'
        plus = 'ABB ABA AAB PAA PAB APA APB AAP ABP PPA PAP APP PPP'
        f.write(header + ' ' + plus + '\n')
        obs = [str(stats[key]) for key in header.split()]
        obs.extend(map(str, stats['all_triconfig']))
        f.write(' '.join(obs) + '\n')

#####

log.close()




    
