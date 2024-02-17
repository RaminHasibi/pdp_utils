import time
from pdp_utils import *
import random 
file = 'pdp_utils/data/pd_problem/Call_7_Vehicle_3.txt'
prob = load_problem(file)



start_time = time.time()
for _ in range(10):
    initial_sol = [0] * prob["n_vehicles"] + [i for i in range(1, prob["n_calls"] + 1)] * 2


    feasible_sol = initial_sol
    
    
    total_cost = cost_function(feasible_sol, prob)
    counter = 1

    for _ in range(10000):
        
        random_sol = [[] for _ in range(prob["n_vehicles"] + 1)]

        for call in range(1, prob["n_calls"] + 1):

            place = random.randint(0, prob["n_vehicles"])
            random_sol[place].extend([call, call])
            random.shuffle(random_sol[place])

        for i in range(len(random_sol) - 1):
            random_sol[i].insert(0, 0)

        new_sol = [x for sublist in random_sol for x in sublist]

        feasiblity, c = feasibility_check(new_sol, prob)
        if feasiblity:
            new_cost = cost_function(new_sol,prob)
            old_cost = cost_function(feasible_sol,prob)
            if(new_cost<old_cost):
                feasible_sol = new_sol
                total_cost += cost_function(feasible_sol, prob)
                counter+=1
                

   

    feasiblity, c = feasibility_check(feasible_sol, prob)

    Cost_fes = cost_function(feasible_sol, prob)
    Cost_init = cost_function(initial_sol, prob)
    print(feasible_sol)
    print('Feasibility:', feasiblity)
    print('Best Cost', Cost_fes)
    print('Average cost:', total_cost/counter)
    print('Improvement',((Cost_init-Cost_fes)/Cost_init)*100)
    
    
end_time = time.time()
print('Average Elapsed time', (end_time - start_time)/10)