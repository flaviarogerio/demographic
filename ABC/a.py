import simul, yaml

with open('params.yml') as f:
    cfg = yaml.load(f, yaml.Loader)
models = simul.model_names
mp = cfg['model_mapping']
models.sort(key=lambda m: int(mp[m][1:]))

print('model code np, npT npS npN npM')
for mod in models:
    M = simul.models_map[mod]()
    pars = M.params
    np = len(pars)
    np_T = len([p for p in pars if p[0] == 'T'])
    np_M = len([p for p in pars if p[0] == 'M'])
    np_N = len([p for p in pars if p[0] == 'N'])
    np_S = len([p for p in pars if p[0] == 'S'])
    print(mod, mp[mod], np, np_T, np_S, np_N, np_M)
