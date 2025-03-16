import json
import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming, solve_tsp_branch_and_bound


import  sys
# resource.setrlimit(resource.RLIMIT_STACK, (2**29-1))
sys.setrecursionlimit(10**6)


distance_matrix = np.array([
    [0,  5, 4, 10],
    [5,  0, 8,  5],
    [4,  8, 0,  3],
    [10, 5, 3,  0]
])
permutation, distance = solve_tsp_branch_and_bound(distance_matrix)




def get_distance(coord1, coord2):
    return abs(coord2["X"] - coord1["X"]) + abs(coord2["Y"] - coord1["Y"])

with open("day_2.json", "r") as file:
    day_data = json.load(file)

with open("las_brickas.json", "r") as file:
    map_data = json.load(file)

nCustomers = len(day_data["Customers"])

distance_map = {}
distance_matrix = np.zeros((nCustomers, nCustomers))
for cx1 in day_data["Customers"]:
    for cx2 in day_data["Customers"]:
        coords1 = map_data["Customers"][cx1["Id"]]["Coordinates"]
        coords2 = map_data["Customers"][cx2["Id"]]["Coordinates"]
        distance_matrix[cx1["Id"], cx2["Id"]] = get_distance(coords1, coords2)

        # key = tuple(sorted((cx1["Id"], cx2["Id"])))
        # if key not in distance_map:
            # distance_map[key] = get_distance(coords1, coords2)



permutation, distance = solve_tsp_branch_and_bound(distance_matrix)
print(permutation)


def format_solution_day2(permutation):
    steps = []
    for i in range(100):
        steps.append(f"load truck=0 quantity=13000 lego={i}")

    for stop in permutation:
        steps.append(f"move_to_customer truck=0 customer={stop}")
        steps.append("deliver truck=0 quantity=1 lego=0")