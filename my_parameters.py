import numpy as np

def get_initial_parameters(parameter_names, spread):
    normal_pars = get_normal_parameters()
    pars_changed = {}
    for key in parameter_names:
        pars_changed[key] = np.random.uniform(1-spread, 1+spread) *  normal_pars[key] 
    
    for key in normal_pars:
        if key in pars_changed:
            normal_pars[key] = pars_changed[key]
    # make into a list
    normal_pars = list(normal_pars.values())
    return normal_pars


def get_normal_parameters():
    pars={} 
    pars['eg0']=24.48
    pars['k']=700
    pars['bv']=5
    pars['mmax']=1
    pars['alpha_m']=140
    pars['km']=2
    pars['alpha_isr']=1.2
    pars['kisr']=2
    pars['pmax']=4.55
    pars['kp']=4
    pars['alpha_p']=35
    pars['p_b']=0
    pars['amax']=5
    pars['alpha_a']=0.37
    pars['ka']=6
    pars['a_b']=0.9
    pars['tau_b']=1800
    pars['height']=1.8
    pars['age_b']=30
    pars['sex']=1
    pars['cage']=0
    pars['target_si']=1.4
    pars['tau_si']=1
    pars['bmi_h']=25
    pars['mffa']=0.8
    pars['ksi_infl']=1.8
    pars['ksi_ffa']=400
    pars['nsi_ffa']=6
    pars['sw11']=1
    pars['inc_i1']=0
    pars['inc_i2']=0
    pars['inc_i3']=0
    pars['it1']=0
    pars['it2']=100000
    pars['it3']=100000
    pars['tau_w']=1.5
    pars['k_infl']=40
    pars['n_infl']=6
    pars['infl_b']=0
    pars['tau_infl']=1
    pars['hgp_bas']=2000
    pars['hepa_max']=3000
    pars['hepa_sic']=1
    pars['a_hgp']=4
    pars['gcg']=0.1
    pars['k_gcg']=0
    pars['s']=0.0002
    pars['png']=350
    pars['sigma_b']=536
    pars['sgmu']=1.5
    pars['sgmd']=1
    pars['sfm']=1.2
    pars['sim']=0.25
    pars['sgku']=81
    pars['sgkd']=137
    pars['sfk']=357
    pars['sik']=0.6
    pars['nsgku']=6
    pars['nsgkd']=6
    pars['nsfk']=6
    pars['nsik']=4
    pars['tau_sigma']=1
    pars['sci']=1
    pars['gclamp']=0
    pars['iclamp']=0
    pars['maxinfl']=1
    pars['l0']=170
    pars['l2']=8.1
    pars['cf']=2
    pars['ksif']=11
    pars['aa']=2
    pars['sif']=1
    pars['ffa_ramax']=1.106
    pars['lp1']=100
    pars['lp2']=125
    pars['tau_wsc']=1
    pars['DEi']=2500
    return pars


def get_normal_state():
    initial_BW = 81 # [kg]
    initial_G = 94.1 # [mg/dL]
    initial_I = 9.6 # [microU/mL]
    initial_FFA = 404 # [micromol/L]
    initial_Si = 0.8 # [ml/microU/day]
    initial_beta = 1000 # [mg]
    initial_sigma = 530 # [microU/mg/day]
    initial_theta = 0.56 # systematic inflammation index
    initial_state = [initial_G, initial_I, initial_FFA, initial_Si, initial_beta, initial_sigma, initial_theta, initial_BW]
    return initial_state