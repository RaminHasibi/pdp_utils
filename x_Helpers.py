import numpy as np
import random
from pdp_utils import *
file = 'pdp_utils/data/pd_problem/Call_7_Vehicle_3.txt'
prob = load_problem(file)

import numpy as np
import random

def find_compatible_vehicles(problem):
    compatible_calls = {}
    for vehicle_index in range(problem['n_vehicles']):
        # Get the indices of calls that this vehicle can transport
        call_indices = np.where(problem['VesselCargo'][vehicle_index] == 1)[0]
        # Adjusting for 1-based indexing of calls in your problem description
        compatible_calls[vehicle_index + 1] = list(call_indices + 1)
    return compatible_calls

def find_compatible_calls(problem):
    compatible_vehicles = {i+1: [] for i in range(problem['n_calls'])}
    for vehicle_index, vehicle in enumerate(problem['VesselCargo']):
        for call_index, can_transport in enumerate(vehicle):
            if can_transport == 1:
                # Adjusting for 1-based indexing
                compatible_vehicles[call_index + 1].append(vehicle_index + 1)
    return compatible_vehicles


problem = load_problem(file)
data = find_compatible_vehicles(problem)




def weightedRandom(data):
    weights = {key: len(value) for key, value in data.items()}

    # Normalize weights
    total_weight = sum(weights.values())
    normalized_weights = {key: weight / total_weight for key, weight in weights.items()}

    # Sample a random number based on the weights
    random_number = random.choices(list(normalized_weights.keys()), list(normalized_weights.values()))[0]

    return random_number

