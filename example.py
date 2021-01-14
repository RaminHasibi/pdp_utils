
from pdp_utils import *


prob = load_problem('pdp_utils/data/pd_problem/Call_7_Vehicle_3.txt')

sol = [7, 7, 5, 5, 0, 2, 2, 0, 3, 4, 4, 3, 1, 1, 0, 6, 6]

print(prob.keys())


feasiblity,c = feasibility_check(sol,prob)

Cost = cost_function(sol,prob)

print(feasiblity)
print(c)
print(Cost)
