import numpy as np
from pymoo.core.sampling import Sampling
from ambiegen.solutions import RobotSolution

import config as cf

def generate_random_solution():

    map_size = cf.robot_env["map_size"]
    min_len = cf.robot_env["min_len"]
    max_len = cf.robot_env["max_len"]

    min_pos = 1
    max_pos = map_size - 1

    len_values = [
        i for i in range(min_len, max_len + 1, 1)
    ]  # a list of distance to go forward
    pos_values = [
        i for i in range(min_pos, max_pos + 1, 1)
    ]  # a list of angles to turn

    states = []
    
    init_states = [0, 1]

    state = np.random.choice(init_states)
    value = np.random.choice(len_values)
    position = np.random.choice(pos_values)


    for i in range(0, map_size - 1):

        state = np.random.choice(init_states)
        value = np.random.choice(len_values)
        position = np.random.choice(pos_values)
        states.append([state, value, position])

    return states

class RobotSampling(Sampling):
    def _do(self, problem, n_samples, **kwargs):

        X = np.full((n_samples, 1), None, dtype=np.object)

        for i in range(n_samples):
            states = generate_random_solution()
            s = RobotSolution()
            s.states = states
            X[i, 0] = s

        return X
 