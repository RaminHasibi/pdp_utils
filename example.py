
from pdp_utils import *


prob = load_problem('pdp_utils/data/pd_problem/Call_7_Vehicle_3.txt')

sol = [0, 2, 2, 0, 1, 5, 5, 3, 1, 3, 0, 7, 4, 6, 7, 4, 6]

print(prob.keys())

feasiblity, c = feasibility_check(sol, prob)

Cost = cost_function(sol, prob)

print(feasiblity)
print(c)
print(Cost)
