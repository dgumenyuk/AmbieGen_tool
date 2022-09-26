
from ambiegen.solutions.robot_solution import RobotSolution
from ambiegen.solutions.vehicle_solution import VehicleSolution
import os
import config as cf
def save_tcs_images(test_suite, problem, run):
    """
    It takes a test suite, a problem, and a run number, and then it saves the images of the test suite
    in the images folder
    
    Args:
      test_suite: a dictionary of solutions, where the key is the solution number and the value is the
    solution itself
      problem: the problem to be solved. Can be "robot" or "vehicle"
      run: the number of the runs
    """

    if not(os.path.exists(cf.files["images_path"])):
        os.makedirs(cf.files["images_path"])
    if not(os.path.exists(os.path.join(cf.files["images_path"], "run"+str(run)))):
        os.makedirs(os.path.join(cf.files["images_path"], "run"+str(run)))

    for i in range(len(test_suite)):

        path = os.path.join(cf.files["images_path"], "run"+str(run), str(i)+".png")
        if problem == "robot":
            RobotSolution.build_image(test_suite[str(i)], path)

        elif problem == "vehicle":
            VehicleSolution.build_image(test_suite[str(i)], path)
    print("Images saved in %s" % os.path.join(cf.files["images_path"], "run"+str(run)))
