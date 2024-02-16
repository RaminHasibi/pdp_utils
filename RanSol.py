import time
from pdp_utils import *
import random 


file = 'pdp_utils/data/pd_problem/Call_7_Vehicle_3.txt'
initial_sol = []
prob = load_problem(file)

for x in range( prob["n_vehicles"] ):
    initial_sol.append(0)
for y in range(prob["n_calls"]):
    y+=1
    initial_sol.append(y)
    initial_sol.append(y)


print(initial_sol)
print('\n')



feasible_sol = initial_sol
start_time = time.time()
for x in range(10000):
    
    random_sol = []
    prob = load_problem(file)
    num_vehicles = prob["n_vehicles"] 
    num_calls = prob["n_calls"]

    for _ in range( num_vehicles +1):
        random_sol.append([])

    for y in range(num_calls):
        y+=1
        place = random.randint(0,num_vehicles)
        random_sol[place].append(y)
        random_sol[place].append(y)

        random.shuffle(random_sol[place])

    for i in range(len(random_sol)):
        if(i == len(random_sol)-1):
            break  
        random_sol[i].insert(0,0)


    new_sol=[]

    for x in random_sol:
        new_sol += x

    feasiblity, c = feasibility_check(new_sol, prob)
    if(feasiblity):
        feasible_sol = new_sol


end_time = time.time()




feasiblity, c = feasibility_check(feasible_sol, prob)

Cost = cost_function(feasible_sol, prob)
print(feasible_sol)
print(feasiblity)
print(c)
print('Cost', Cost)
print('elapsed time', end_time - start_time)