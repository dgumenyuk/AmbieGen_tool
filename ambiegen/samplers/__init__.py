
from ambiegen.samplers.robot_sampling import RobotSampling
from ambiegen.samplers.vehicle_sampling import VehicleSampling


SAMPLERS = {
    "vehicle": RobotSampling,
    "robot": VehicleSampling,

}