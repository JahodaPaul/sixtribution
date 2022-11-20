import json
import random

import numpy as np


def generate_scenario(n_of_cars, scenario_path):
    data_dict = dict()
    data_dict["cars"] = dict()
    munich_coords = (48.13743, 11.57549)

    for car_id in range(0, n_of_cars):
        data_dict["cars"][car_id] = dict()
        data_dict["cars"][car_id]["latitude"] = np.random.normal(0.0, 0.012, 1)[0] + munich_coords[0]
        data_dict["cars"][car_id]["longitude"] = np.random.normal(0.0, 0.018, 1)[0] + munich_coords[1]
        data_dict["cars"][car_id]["battery_level"] = random.randint(50, 80)
        data_dict["cars"][car_id]["station_id"] = None
        data_dict["cars"][car_id]["state"] = "booked"

    with open(scenario_path, "w") as f:
        json.dump(data_dict, f, indent=2)

    print(f"Generated scenario for {n_of_cars} cars, in file '{scenario_path}!'")


if __name__ == "__main__":
    generate_scenario(100, "./../../data/scenario_initializations/init_cars_scenario_3.json")