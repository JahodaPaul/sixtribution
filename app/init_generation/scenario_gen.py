import json
import random

import numpy as np


def generate_scenario(n_of_cars, scenario_path):
    """
    Function generates a json scenario file with n_of_cars cars, which get assigned to a random coordinates close to
    the center of Munich. All cars are initialized with a random battery level between 0 and 100 and a random state
    "booked" since we then don't have to the link the car to a station.

    :param n_of_cars: Int. Number of cars to be generated.
    :param scenario_path: String. Path to the scenario file.
    """
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