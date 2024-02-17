
from pdp_utils import *


prob = load_problem('pdp_utils/data/pd_problem/Call_7_Vehicle_3.txt')

sol = [3, 3, 0, 5, 5, 2, 2, 0, 1, 1, 7, 7, 0, 4, 4, 6, 6]
print(prob.keys())

feasiblity, c = feasibility_check(sol, prob)

Cost = cost_function(sol, prob)

print(feasiblity)
print(c)
print(Cost)
