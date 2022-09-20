import numpy as np
from pymoo.core.sampling import Sampling
from ambiegen.solutions import VehicleSolution

import config as cf
from ambiegen.utils.car_road import Map

def generate_random_road():
    map = Map(
        cf.vehicle_env["map_size"])

    actions = list(range(0, 3))
    lengths = list(range(cf.vehicle_env["min_len"], cf.vehicle_env["max_len"]))
    angles = list(range(cf.vehicle_env["min_angle"], cf.vehicle_env["max_angle"]))
    done = False

    while not done:
        action = np.random.choice(actions)
        if action == 0:
            length = np.random.choice(lengths)
            done = not(map.go_straight(length))
        elif action == 1:
            angle = np.random.choice(angles)
            done = not(map.turn_right(angle))
        elif action == 2:
            angle = np.random.choice(angles)
            done = not(map.turn_left(angle))
    scenario = map.scenario[:-1]

    return scenario

class VehicleSampling(Sampling):

    '''
    Module to generate the initial population
    '''
    def _do(self, problem, n_samples, **kwargs):

        X = np.full((n_samples, 1), None, dtype=np.object)

        for i in range(n_samples):
            states = generate_random_road()
            s = VehicleSolution()
            s.states = states
            X[i, 0] = s
        return X
