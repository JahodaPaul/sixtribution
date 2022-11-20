import os

from app.main.Core import Core
import pickle
import time
import json

from Core import Core
from app.controllers.Stations import Stations


def get_initial_state(file_name):
    with open(file_name, "r") as f:
        init_state = json.load(f)

    return init_state


def main():
    root_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../")
    core = Core(200)
    initial_state = get_initial_state(root_path + "./data/scenario_initializations/init_cars_scenario_1.json")
    # stations have to be initialized first, because cars will update their capacity
    core.initialize_stations(root_path + "./data/stations.txt")
    core.initialize_fleet(initial_state["cars"])

    controller_stations = Stations()

    # each time stamp corresponds to 1 hour
    total_sim_duration = core.get_total_simulation_duration()
    core.pretty_print_car_states()
    while core.get_current_simulation_step() > 0:
        print(f"\rSimulation step {total_sim_duration - core.get_current_simulation_step() + 1} / {total_sim_duration}")

        # only update needed
        core.update_fleet()

        # frontend stuff
        stations = core.get_stations()
        fleet = core.get_fleet()

        with open(root_path + "data/stations_current.pickle", "wb") as outfile:
            pickle.dump(stations, outfile)

        with open(root_path + "data/fleet_current.pickle", "wb") as outfile:
            pickle.dump(fleet, outfile)

        core.pretty_print_car_states()
        # time.sleep(1)
        #
        # TODO update stations
        # controller_stations.update(stations)


if __name__ == "__main__":
    main()
