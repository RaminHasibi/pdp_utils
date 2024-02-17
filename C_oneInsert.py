import random
from x_Helpers import *
from pdp_utils import *
from x_Helpers import *

file = 'pdp_utils/data/pd_problem/Call_7_Vehicle_3.txt'
prob = load_problem(file)

initial_solution = initSol(file)

def one_insert(solution, prob):
    x= find_compatible_calls(prob)
    y= find_compatible_vehicles(prob)
    rand = weightedRandom(x)
    return rand
    
    
print(one_insert(initial_solution,prob))
