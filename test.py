import json
import numpy as np
from pprint import pprint


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



# pprint(distance_map)
