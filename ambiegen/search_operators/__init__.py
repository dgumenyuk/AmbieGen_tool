from vehicle_crossover import VehicleCrossover
from vehicle_mutation import VehicleMutation
from robot_crossover import RobotCrossover
from robot_mutation import RobotMutation

OPERATORS = {
    'vehicle_crossover': VehicleCrossover,
    'vehicle_mutation': VehicleMutation,
    'robot_crossover': RobotCrossover,
    'robot_mutation': RobotMutation
}