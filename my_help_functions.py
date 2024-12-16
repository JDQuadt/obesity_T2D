from my_parameters import *
from my_model import *
from scipy.integrate import solve_ivp as sivp

# generate a selection of initial parameters and check for physiological bounds
def generate_initial_patients(n_patients, parameter_names, spread, tspan, physiological_bounds):
    t_eval = list(range(tspan[0], tspan[1] +1))
    parameter_sets = []
    for i in range(n_patients):
        parameter_set = get_initial_parameters(parameter_names, spread)
        parameter_sets.append(parameter_set)
    initial_state = get_normal_state()

    physiological_patients = []
    # run model with initial state and parameters
    for i, parameter_set in enumerate(parameter_sets):
        # run model with initial state and parameters
        sol = sivp(odde,tspan,initial_state,method='LSODA',args=[parameter_set], t_eval=t_eval)
        end_states = sol.y[:,-1]
        relevant_end_states = end_states[0:6]

        # check if end states are within physiological bounds
        if check_physiological_baseline(relevant_end_states, physiological_bounds):
            physiological_patients.append([parameter_set, end_states])
        if i % 100 == 0:
            print(f'Generated {i} patients')

    return physiological_patients

def generate_progressions(patients, DEi_range, DEi_initial ,tspan_1, tspan_2, tspan_3, tstep):
    # define the evaluation times on which to return the ode solves
    t_eval_1 = list(range(tspan_1[0],tspan_1[1] +1, tstep))
    t_eval_2 = list(range(tspan_2[0],tspan_2[1] +1, tstep))
    t_eval_3 = list(range(tspan_3[0],tspan_3[1] +1, tstep))

    # 
    full_states = []
    full_time = np.concatenate((t_eval_1, t_eval_2, t_eval_3))
    for i, patient in enumerate(patients):
        # run the first solve region
        parameters = patient[0]
        initial_state = patient[1]
        sol_1 = sivp(odde,tspan_1,initial_state,method='LSODA',args=[parameters], t_eval=t_eval_1)

        # define new parameters for second region
        final_state_1 = sol_1.y[:,-1]
        DEi_2  = np.random.uniform(DEi_range[0], DEi_range[1]) * DEi_initial
        parameters[76] = DEi_2
        sol_2 = sivp(odde,tspan_2,final_state_1,method='LSODA',args=[parameters], t_eval=t_eval_2)

        # define new parameters for third region
        final_state_2 = sol_2.y[:,-1]
        parameters[76] = DEi_initial
        sol_3 = sivp(odde, tspan_3, final_state_2, method='LSODA',args=[parameters], t_eval=t_eval_3)

        # combine solutions
        states_combined = np.hstack((sol_1.y, sol_2.y, sol_3.y))
        full_states.append(states_combined)
    return full_states, full_time






        

# check if end states are within physiological bounds
def check_physiological_baseline(states, baselines):
    if len(states) != len(baselines):
        raise ValueError('The number of states and baselines must be the same.')
    for i, state in enumerate(states):
        # check if state is within ith bounds of baselines
        if state < baselines[i][0] or state > baselines[i][1]:
            return False
    return True






