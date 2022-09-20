
from ambiegen.utils.vehicle2 import Car
import config as cf
from ambiegen.utils.car_road import Map

class VehicleSolution:

    '''
    This is a class to represent one individual of the genetic algorithm
    '''
    def __init__(self):

        self.road_points = []
        self.states = []
        speed = 9
        steer_ang = 12
        self.map_size = cf.vehicle_env["map_size"]
        self.car = Car(speed, steer_ang, self.map_size)
        self.road_builder = Map(self.map_size)
        self.fitness = 0
        self.car_path = []
        self.novelty = 0
        self.intp_points = []
        self.too_sharp = 0
        self.just_fitness = 0

    def eval_fitness(self):
        road = self.road_points
        if not road:  # if no road points were calculated yet
            self.get_points_from_states()
            road = self.road_points

        if len(self.road_points) <= 2:
            self.fitness = 0
        else:
            self.intp_points = self.car.interpolate_road(road)
            self.fitness, self.car_path = self.car.execute_road(self.intp_points) #evaluate(self.intp_points)#

        return self.fitness

    def compare_states(self, state1, state2):
        similarity = 0
        if state1[0] == state2[0]:
            similarity += 1
            if state1[0] == 0:
                if abs(state1[1] - state2[1]) <= 10:
                    similarity += 1
            else:
                if abs(state1[2] - state2[2]) <= 10:
                    similarity += 1

        return similarity

    def calc_novelty(self, old, new):
        similarity = 0
        total_states = (len(old) + len(new))*2

        if len(old) > len(new):
            for i in range(len(new)):
                similarity += self.compare_states(old[i], new[i])
        elif len(old) <= len(new):
            for i in range(len(old)):
                similarity += self.compare_states(old[i], new[i])
        novelty = 1 - (similarity/total_states)
        return -novelty


    def get_points_from_states(self):
        states = self.states
        map = Map(self.map_size)
        tc = states
        for state in tc:
            action = state[0]
            if action == 0:
                done = map.go_straight(state[1])
                if not(done):
                    break
            elif action == 2:
                done = map.turn_left(state[2])
                if not(done):
                    break
            elif action == 1:
                done = map.turn_right(state[2])
                if not(done):
                    break
            else:
                print("ERROR, invalid action")

            

        points = map.road_points_list[:-1]
        self.road_points  = points
        return points
 
    @property
    def n_states(self):
        return len(self.states)
