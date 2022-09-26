from ambiegen.solutions import VehicleSolution
from ambiegen.solutions import RobotSolution
import config as cf
def calc_novelty(state1, state2, problem):
    """
    > The function takes two states and a problem type as input and returns the novelty of the two
    states
    
    Args:
      state1: the first state to compare
      state2: the state to compare to
      problem: the problem we're solving, either "vehicle" or "robot"
    
    Returns:
      The novelty of the solution relative to the other solutions in the test suite.
    """
    '''
    similarity = 0
    state_num = min(len(state1), len(state2))
    
    if problem == "vehicle":
        total_states = state_num*cf.vehicle_env["elem_types"]
        for i in range(state_num):
            similarity += VehicleSolution.compare_states(state1[i], state2[i])
    elif problem == "robot":
        total_states = state_num*cf.robot_env["elem_types"]
        for i in range(state_num):
            similarity += RobotSolution.compare_states(state1[i], state2[i])
    novelty = 1 - (similarity/total_states)
    '''
    if problem == "vehicle":
        novelty = abs(VehicleSolution().calculate_novelty(state1, state2))
    elif problem == "robot":
        novelty = abs(RobotSolution().calculate_novelty(state1, state2))
        
    return novelty