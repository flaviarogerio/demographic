import egglib, lzmp, math

# fixed parameters
S = 256
So = 187 #sites present on outgroup right

n_NAM = 31
n_E = 90
n_BR = 16

m = 0 # the proportion of oriented polymorphisms where there was an error due to a second mutation on the branch leading to the outgroup
MAF = 0.05

param_list = ['modindex', 'N_NAM', 'N_EUR', 'N_BR', 'T1', 'T2', 'Tb', 'S']  #FR: is it correct?

stat_list = [
    'all_Dj', 'all_Hsd', 'all_F', 'all_Pi', 'all_D',
    'all_FstWC', 'NAM_Hsd', 'NAM_F', 'NAM_Pi', 'NAM_D',
    'NAM_Dfl', 'NAM_thetaW', 'EUR_Hsd', 'EUR_F', 'EUR_Pi', 'EUR_D',
    'EUR_Dfl', 'EUR_thetaW', 'BR_Hsd', 'BR_F', 'BR_Pi', 'BR_D',
    'BR_Dfl', 'BR_thetaW', 'NAM-EUR_numShP', 'NAM-EUR_numSpd',
    'NAM-EUR_Da', 'NAM-EUR_Dj', 'NAM-EUR_Dxy', 'NAM-EUR_numShA',
    'NAM-EUR_FstWC', 'NAM-BR_numShP', 'NAM-BR_numSpd', 'NAM-BR_Da',
    'NAM-BR_Dj', 'NAM-BR_Dxy', 'NAM-BR_numShA', 'NAM-BR_FstWC',
    'EUR-BR_numShP', 'EUR-BR_numSpd', 'EUR-BR_Da', 'EUR-BR_Dj',
    'EUR-BR_Dxy', 'EUR-BR_numShA', 'EUR-BR_FstWC']
    
    #FR: Should I updated the name of theses stats too to match with stats names on line 106?
triconfig_stats = [
    'ABB', 'ABA', 'AAB', 'PAA', 'PAB', 'APA', 'APB', 'AAP', 'ABP',
    'PPA', 'PAP', 'APP', 'PPP']

# functions to draw parameters from priors
def uniform_draw(mini, maxi):
    return egglib.random.uniform_closed()*(maxi-mini)+mini

def loguniform_draw(mini, maxi):
    mini = math.log(mini)
    maxi = math.log(maxi)
    return math.exp(egglib.random.uniform_open()*(maxi-mini)+mini)

def normal_draw(mean, stdev, mini, maxi):
    return egglib.random.normal_bounded(mean, stdev, mini, maxi)

def lognormal_draw(mean, stdev):
    return math.exp(egglib.random.normal()*stdev + mean)

# function running a given number of simulations
def job(seed, model, num):
    """
    :param seed: pseudorandom number generator seed
    :param model: integer (1, 2, or 3)
    :param num: number of simulations
    :return: a list of lines ready to be dumpy into an output file
    All simulations for which at least one statistics is None are
    skipped. Simulations are performed until the requested number is
    reached.
    """

    # set seed
    egglib.random.set_seed(seed)

    # create model (common backbone for all models)
    coal = egglib.coalesce.Simulator(num_pop=3, num_chrom=[n_NAM, n_E, n_BR], num_mut=1) 
if model == 7:  #EUR as ancestral
            coal.params.add_event('merge', T=0, src=2, dst=1])
            coal.params.add_event('merge', T=0, src=0, dst=1)
            coal.params.add_event('bottleneck', T=0, S=0)
            coal.params.add_event('bottleneck', T=0, S=0)

if model == 8: #NAM as ancestral and BR merge with NAM before than EUR
            coal.params.add_event('merge', T=0, src=2, dst=0)
            coal.params.add_event('merge', T=0, src=1, dst=0)
            coal.params.add_event('bottleneck', T=0, S=0)
            coal.params.add_event('bottleneck', T=0, S=0)

if model == 9: #NAM as ancestral and EUR merge with NAM before than BR
            coal.params.add_event('merge', T=0, src=1, dst=0)
            coal.params.add_event('merge', T=0, src=2, dst=0)
            coal.params.add_event('bottleneck', T=0, S=0)
            coal.params.add_event('bottleneck', T=0, S=0)

if model == 10: #BR as ancestral
            coal.params.add_event('merge', T=0, src=1, dst=2)
            coal.params.add_event('merge', T=0, src=0, dst=2)
            coal.params.add_event('bottleneck', T=0, S=0)
            coal.params.add_event('bottleneck', T=0, S=0)

    coal.simul() # make one simulation to make the "align" object available
    coal.align.alphabet.add_missing(-1) # enable the possibility of using missing data

    # create set of ComputeStats objects
    struct = egglib.struct_from_samplesizes([n_NAM, n_E, n_BR], outgroup=1)
    cs_maf = egglib.stats.ComputeStats(struct=struct)
    cs_dict = {
        'all': egglib.stats.ComputeStats(struct=struct, multi=True),
        'NAM': egglib.stats.ComputeStats(struct=struct.subset(pops=['pop1']), multi=True),
        'EUR': egglib.stats.ComputeStats(struct=struct.subset(pops=['pop2']), multi=True),
        'BR': egglib.stats.ComputeStats(struct=struct.subset(pops=['pop3']), multi=True),
        'NAM-EUR': egglib.stats.ComputeStats(struct=struct.subset(pops=['pop1', 'pop2']), multi=True),
        'NAM-BR': egglib.stats.ComputeStats(struct=struct.subset(pops=['pop1', 'pop2']), multi=True),
        'EUR-BR': egglib.stats.ComputeStats(struct=struct.subset(pops=['pop2', 'pop3']), multi=True)}
    cs_maf.add_stats('maf')
    cs_dict['all'].add_stats('triconfig')
    for key in 'NAM', 'EUR', 'BR':
        cs_dict[key].add_stats('thetaW', 'Dfl', 'F', 'D*', 'F*')
    for key in 'all', 'NAM', 'EUR', 'BR':
        cs_dict[key].add_stats('Pi', 'D', 'Hsd')
    for key in 'all', 'NAM-EUR', 'NAM-BR', 'EUR-BR':
        cs_dict[key].add_stats('FstWC', 'Dj')
    for key in 'NAM-EUR', 'NAM-BR', 'EUR-BR':
        cs_dict[key].add_stats('Dxy', 'Da', 'numSpd', 'numShA', 'numShP')

    # initialize counters
    done = 0
    output_lines = []
    
     # perform simulations
    while done < num:

        # draw parameters common
        N_NAM = loguniform_draw(0.1, 10)
        N_EUR = loguniform_draw(0.1, 10)
        N_BR = loguniform_draw(0.1, 10)
        T1 = lognormal_draw(math.log(0.1), math.log(3))
        T2 = lognormal_draw(math.log(0.1), math.log(3))
        Tb = loguniform_draw(0.1, 10)   #FR: can I name the Bottleneck time of Tb? and after update it? 
        S = loguniform_draw(0.1, 10)    #FR: Can I use loguniform function?
    
    
        # update parameters
        coal.params['N'] = [N_NAM, N_EUR, N_BR] 
        
        #FR: How should I refer to Time of bottleneck, to differentiate from split time?
        #FR: you told something about add a “small values” for T to avoid overlap with split size, for instance use +1e6? How effectively do that? ) 
        
        
        if model ==7:  #EUR as ancestral
            coal.params['events'].update(0, T=T1)
            coal.params['events'].update(1, T=T1+T2)
            coal.params['events'].update(2, T=Tb, S=S)     	 #how update the bottleneck event??? should I add "2" for representate this event?
            coal.params['events'].update(3, T=Tb, S=S)     	 #how update the bottleneck event??? should I add "3" for representate this event?

        elif model == 8:  #NAM as ancestral and BR merge with NAM before than EUR
            coal.params['events'].update(0, T=T1)
            coal.params['events'].update(1, T=T1+T2)
            coal.params['events'].update(2, T=Tb, S=S)     	 #how update the bottleneck event??? should I add "2" for representate this event?
            coal.params['events'].update(3, T=Tb, S=S)     	 #how update the bottleneck event??? should I add "3" for representate this event?

        elif model == 9:  #NAM as ancestral and EUR merge with NAM before than BR
            coal.params['events'].update(0, T=T1)
            coal.params['events'].update(1, T=T1+T2)
            coal.params['events'].update(2, T=Tb, S=S)     	 #how update the bottleneck event??? should I add "2" for representate this event?
            coal.params['events'].update(3, T=Tb, S=S)     	 #how update the bottleneck event??? should I add "3" for representate this event?
          
        elif model == 10:  #BR as ancestral
            coal.params['events'].update(0, T=T1)
            coal.params['events'].update(1, T=T1+T2)
            coal.params['events'].update(2, T=Tb, S=S)     	 #how update the bottleneck event??? should I add "2" for representate this event?
            coal.params['events'].update(3, T=Tb, S=S)     	 #how update the bottleneck event??? should I add "3" for representate this event?
        
        
        # run simulations
        c = 0
        while c < S:
            for aln in coal.iter_simul(10): # run a batch of 10 simulations
                # here aln contains 1 simulated SNP
                if c < So:
                    aln.add_sample('outgroup', [0]) # add an outgroup sample
                else:
                    aln.add_sample('outgroup', [-1]) # set outgroup missing

                # check MAF
                if cs_maf.process_align(aln)['maf'] < MAF:
                    continue

                for cs in cs_dict.values():
                    cs.process_align(aln)
                c += 1
                if c == S: break

        # pack the results in a single dictionary
        results = {} # SDM: remove modindex from here
        for key, cs in cs_dict.items():
            stats = cs.results()
            stats = {key + '_' + str(stat_name): value for stat_name, value in stats.items()}
            results.update(stats)

        # skip simulation if there is at least one None in results
        if None in results.values():
            continue

        # generate the line for the output file
        output_lines.append(
                f'{model} {N_NAM} {N_EUR} {N_BR} {N_ANC1} {T1} {T2} {Tb} {S} {mNAM_EUR} {mEUR_NAM} {mNAM_BR} {mBR_NAM} {mEUR_BR} {mBR_EUR} {mANC1_BR} {mBR_ANC1} {mEUR_ANC1} {mANC1_EUR} {mANC1_NAM} {mNAM_ANC1} ' +
                ' '.join(str(results[stat]) for stat in stat_list) + ' ' +
                ' '.join(map(str, results['all_triconfig'])) + '\n')
 
         done += 1
    return output_lines

# function to write down results in the output file
def export(lines, ID):
    global f
    print(f'model:{lines[0][0]} ID={ID}')
    f.writelines(lines)
    f.flush()

# main function to run simulations in batches
def run(nbatch, szbatch, fname):
    """
    nbatch: number of jobs to run in parallel
    szbatch: number of simulations per batch
    fname: output file name
    """
    seed = egglib.random.integer(100000) + 100000
    jobs = []
    global f
    f = open(fname, 'w')
    f.write(' '.join(param_list) + ' ' + ' '.join(stat_list) + ' ' +
        ' '.join(triconfig_stats) + '\n')
    f.flush()
    for model in [3,4,5,6]:
        for i in range(nbatch):
            jobs.append([seed+i, model, szbatch])
        seed += nbatch

    lzmp.run(job, jobs, post=export, shuffle=False)

# start of iteration 
run(nbatch=1, szbatch=10, fname='1_results_simulations_model7~10.txt')
