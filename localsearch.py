from click import progressbar
from oneInsert import one_insert

from pdp_utils.Utils import cost_function, feasibility_check, initSol, load_problem
file = 'pdp_utils/data/pd_problem/Call_7_Vehicle_3.txt'
prob = load_problem(file)

initial_solution = initSol(file)



def local_search(s_0, prob, operator):
    best_s = [s_0, cost_function(s_0, prob)]


    for i in range(1, 10001):
        
        current = operator(best_s, prob)
        curr_feasiblity, c = feasibility_check(current, prob)
        if curr_feasiblity:
            curr_cost = cost_function(current, prob)
            if curr_cost < best_s[1]:
                best_s = [current, curr_cost]

   
    return best_s

local_search(initial_solution, prob, one_insert)