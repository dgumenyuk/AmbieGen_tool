
from pymoo.optimize import minimize
import config as cf
from ambiegen import ALRGORITHMS 
from ambiegen.problems import PROBLEMS
from ambiegen.samplers import SAMPLERS
from ambiegen.search_operators import OPERATORS
from ambiegen.duplicate_elimination.duplicate_rem import DuplicateElimination
from ambiegen.utils.random_seed import get_random_seed
from pymoo.termination import get_termination   

def main(problem, algo, runs_number):
    print("Hello World") 

    algorithm =  ALRGORITHMS[algo](
        n_offsprings=cf.ga["n_offsprings"],
        pop_size=cf.ga["pop_size"],
        sampling = SAMPLERS[problem](),
        crossover = OPERATORS[problem + "_crossover"](cf.ga["cross_rate"]),
        mutation = OPERATORS[problem + "_mutation"](cf.ga["mut_rate"]),
        eliminate_duplicates = DuplicateElimination()      
    )  

    termination = get_termination("n_gen", cf.ga["n_gen"])
    seed = get_random_seed()

    res = minimize(
            PROBLEMS[problem](),
            algorithm,
            termination,
            seed=seed,
            verbose=True,
            save_history=True,
            eliminate_duplicates=True,
        )

    print("time", res.exec_time)
    print("time, sec ", res.exec_time)
    

################################## MAIN ########################################
problem = "vehicle"
algo = "nsga2"
runs_number = 1
if __name__ == '__main__':
    main(problem, algo, runs_number)