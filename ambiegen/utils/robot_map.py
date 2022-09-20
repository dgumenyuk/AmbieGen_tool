 
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import matplotlib.pyplot as plt
import time
class Map:
    """Class that conducts transformations to vectors automatically,
    using the commads "go straight", "turn left", "turn right".
    As a result it produces a set of points corresponding to a road
    """

    def __init__(self, map_size):
        self.map_size = map_size
        self.max_x = map_size
        self.max_y = map_size
        self.min_x = 0
        self.min_y = 0

        self.init_pos = [0, 1]

        self.map_points = []

        # self.current_pos = [self.init_pos, self.init_end]
        self.all_map_points = []
        self.current_level = 1

        self.create_init_box()

    def create_init_box(self):
        """select a random initial position from the middle of
        one of the boundaries
        """
        pos = [0, 0]

        for y in range(self.max_y):
            self.all_map_points.append([pos[0], y])
        pos = [0, self.max_y ]

        for x in range(self.max_x):
            self.all_map_points.append([x, pos[1]])
        pos = [self.max_x , self.max_y ]

        for y in range(self.max_y):
            self.all_map_points.append([pos[0], self.max_y - y])

        pos = [self.max_x, 0]

        for x in range(self.max_x):
            self.all_map_points.append([self.max_x - x, pos[1]])

        return



    def horizontal(self, distance, position):

        new_points = []

        init_pos = [position, self.current_level]
        if self.point_valid(init_pos):
            self.all_map_points.append(init_pos)
            new_points.append(init_pos)
        for i in range(1, round(distance / 2)):
            point_left = [init_pos[0] - i, init_pos[1]]
            point_right = [init_pos[0] + i, init_pos[1]]
            if self.point_valid(point_left):
                self.all_map_points.append(point_left)
                new_points.append(point_left)
            if self.point_valid(point_right):
                self.all_map_points.append(point_right)
                new_points.append(point_right)

        self.current_level += 1

        return new_points

    def vertical(self, distance, position):

        new_points = []

        init_pos = [position, self.current_level]
        if self.point_valid(init_pos):
            self.all_map_points.append(init_pos)
            new_points.append(init_pos)
        for i in range(1, round(distance / 2)):
            point_down = [init_pos[0], init_pos[1] - i]
            point_up = [init_pos[0], init_pos[1] + i]
            if self.point_valid(point_down):
                self.all_map_points.append(point_down)
                new_points.append(point_down)
            if self.point_valid(point_up):
                self.all_map_points.append(point_up)
                new_points.append(point_up)

        self.current_level += 1

        return new_points, self.discount

    def point_valid(self, point):
        if (point in self.all_map_points) or (self.in_polygon(point)) or self.point_out_of_bounds(point):
            self.discount += 1
            return False
        else:
            return True


    def point_out_of_bounds(self, a): 
        if (0 < a[0] and a[0] < self.max_x) and (0 < a[1] and a[1] < self.max_y):
            return False
        else:
            return True


    

    '''

    def point_out_of_bounds(self, a):
        if (0 < a[0] and a[0] < self.max_x ) and (0 < a[1] and a[1] < self.max_y - 4):
            return False
        else:
            return True
    '''


    def in_polygon(self, a):
        """checks whether a point lies within a polygon
        between current and previous vector"""
        f = 3
        finish = [self.max_x, self.max_y]
        f1 = [self.max_x, self.max_y - f]
        f2 = [self.max_x - f, self.max_y - f]
        f3 = [self.max_x - f, self.max_y]

        s = 3
        start = [self.min_x, self.min_y]
        s1 = [self.min_x, self.min_y + s]
        s2 = [self.min_x + s, self.min_y + s]
        s3 = [self.min_x + s, self.min_y]




        point = Point(a[0], a[1])
        polygon1 = Polygon(
            [finish, f1, f2, f3]
        )
        polygon2 = Polygon(
            [start, s1, s2, s3]
        )

        result = (polygon1.contains(point)) or (polygon2.contains(point))
        return result   

    def get_points_from_states(self, states):


        self.init_pos = [0, 1]

        self.map_points = []

        self.all_map_points = []
        self.current_level = 1

        self.create_init_box()

        self.map_lists = [self.all_map_points]

        self.discount = 0



        tc = states
        for state in tc:
            #self.build_tc(self.all_map_points)
            action = state[0]
            if action == 0:
                new_points = self.horizontal(state[1], state[2])
                self.map_lists.append(new_points)
            elif action == 1:
                new_points = self.vertical(state[1], state[2])
                self.map_lists.append(new_points)
            else:
                print("ERROR")

        #print("OBTAINED POINTS", points)
        return self.all_map_points, self.discount




    def build_tc(self, points):


        #time_ = str(int(time.time()))

        fig, ax = plt.subplots(figsize=(12, 12))
        # , nodes[closest_index][0], nodes[closest_index][1], 'go'
        road_x = []
        road_y = []
        for p in points:
            road_x.append(p[0])
            road_y.append(p[1])

        ax.plot(road_x, road_y, 'yo--', label="Road")

        top = self.map_size
        bottom = 0

        ax.set_title("Test case fitenss ", fontsize=17)

        ax.set_ylim(bottom, top)
        
        ax.set_xlim(bottom, top)

        #fig.savefig(".\\Test\\"+ time_+ "+test.jpg")
        fig.savefig("test_inside.png")

        ax.legend()
        plt.close(fig)




def read_schedule(tc, size):
    time_ = str(int(time.time()))
    fig, ax1 = plt.subplots(figsize=(12, 12))
    car_map = Map(size)
    for state in tc:
        action = tc[state]["state"]
        print("location:", car_map.current_pos)
        if action == "straight":
            car_map.go_straight(tc[state]["value"])
            print(tc[state]["value"])
            x, y = car_map.position_to_line(car_map.current_pos)
            ax1.plot(x, y, "o--y")
        elif action == "left":
            car_map.turn_left(tc[state]["value"])
            print(tc[state]["value"])
            x, y = car_map.position_to_line(car_map.current_pos)
            ax1.plot(x, y, "o--y")
        elif action == "right":
            car_map.turn_right(tc[state]["value"])
            print(tc[state]["value"])
            x, y = car_map.position_to_line(car_map.current_pos)
            ax1.plot(x, y, "o--y")
        else:
            print("Wrong value")

    top = size
    bottom = 0
    ax1.set_ylim(bottom, top)
    ax1.set_xlim(bottom, top)
    #plt.yticks(np.arange(bottom, top + 1, 1.0), fontsize=12)
    #plt.grid(b=True, which="major", axis="both")

    #ax1.legend(fontsize=14)
    fig.savefig(".\\Test\\"+ time_+ "+test2.jpg")
    plt.close(fig)






if __name__ == "__main__":


    my_map = Map(200)
    points = my_map.all_map_points


    ox = [t[0] for t in points]
    oy = [t[1] for t in points]

    plt.plot(ox, oy, ".k")
    plt.grid(True)
    plt.axis("equal")
    plt.show()

