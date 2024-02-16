import random


def get_calls(solution):
    vehicles = []
    route = []
    for i in range(len(solution)):
        if solution[i] == 0:
            route.append(solution[i])
            vehicles.append(route)
            route = []
        else:
            route.append(solution[i])
    vehicles.append(route)
    return vehicles


def rand_from_call(call):
    if call == [0]:
        return 0
    elif call[-1] == 0:
        return random.choice(call[:-1])
    else:
        return random.choice(call)


def shuffle_call(call):
    if call == [0] or call == []:
        return call
    elif call[-1] == 0:
        s = call[:-1]
        random.shuffle(s)
        return s + [0]
    else:
        random.shuffle(call)
        return call