

import config as cf
from ambiegen.utils.robot_map import Map
import matplotlib.pyplot as plt
from ambiegen.utils.a_star import AStarPlanner
from shapely.geometry import  LineString
import time
class RobotSolution:
    def __init__(self):

        self.map_points = []
        self.map_size = cf.robot_env["map_size"]
        self.states = []
        self.fitness = 0
        self.novelty = 0
        self.sx = 2.0  # [m]
        self.sy = 2.0  # [m]
        self.gx = cf.robot_env["map_size"] - 1  # [m]
        self.gy = cf.robot_env["map_size"] - 1  # [m]
        #self.map_builder = Map(cf.model["map_size"])

        self.grid_size = 2  # [m]
        self.robot_radius = 1  # [m]

    def eval_fitness(self):
        map_builder = Map(self.map_size)
        self.map_points = map_builder.get_points_from_states(self.states)

        ox = [t[0] for t in self.map_points]
        oy = [t[1] for t in self.map_points] 

        a_star = AStarPlanner(ox, oy, self.grid_size, self.robot_radius)  # noqa: E501
        rx, ry, _ = a_star.planning(self.sx, self.sy, self.gx, self.gy)

        self.robot_path_x = rx
        self.robot_path_y = ry
        path = zip(rx, ry)

        if len(rx) > 2:
            test_road = LineString([(t[0], t[1]) for t in path])
            self.fitness = -test_road.length
        else:
            self.fitness = 0

        return self.fitness

    def compare_states(self, state1, state2):
        similarity = 0
        if state1[0] == state2[0]:
            similarity += 1
            if abs(state1[1] - state2[1]) <= 5:
                similarity += 1
            if abs(state1[2] - state2[2]) <= 5:
                similarity += 1

        return similarity

    def calc_novelty(self, old, new):
        similarity = 0
        total_states = (len(old))*3

        if len(old) > len(new):
            for i in range(len(new)):
                similarity += self.compare_states(old[i], new[i])
        elif len(old) <= len(new):
            for i in range(len(old)):
                similarity += self.compare_states(old[i], new[i])
        novelty = 1 - (similarity/total_states)
        return -novelty


    def build_image(self, name = "test.png"):

        fig, ax = plt.subplots(figsize=(12, 12))

        map_builder = Map(self.map_size)
        map_points = map_builder.get_points_from_states(self.states)
        ox = [t[0] for t in map_points]
        oy = [t[1] for t in map_points]

        a_star = AStarPlanner(ox, oy, self.grid_size, self.robot_radius)  # noqa: E501
        rx, ry, _ = a_star.planning(self.sx, self.sy, self.gx, self.gy)

        road_x = []
        road_y = []
        for p in map_points:
            road_x.append(p[0])
            road_y.append(p[1])

        ax.plot(rx, ry, '-r', label="Robot path")
        ax.scatter(road_x, road_y, s=150, marker='s', color='k', label="Walls")

        top = self.map_size
        bottom = 0

        ax.tick_params(axis='both', which='major', labelsize=18)
        ax.set_ylim(bottom, top)
        ax.set_xlim(bottom, top)
        ax.legend(fontsize=22)

        top = self.map_size + 1
        bottom = - 1

        save_path = (name)

        fig.savefig(save_path)
    
        plt.close(fig)



