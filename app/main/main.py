import os

import pickle
import time

from app.main.Core import Core
from app.controllers.Stations import Stations


def main(n_time_steps):
    """
    Main entry point of the simulation. The function create a Core instance and populates it with the necessary data.
    It then simulates car movement/charging/booking for n_time_steps.
    """
    root_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../")
    core = Core(n_time_steps)

    # stations have to be initialized first, because cars will update their capacity
    core.initialize_stations(root_path + "./data/stations.txt")
    core.initialize_fleet(root_path + "./data/scenario_initializations/init_cars_scenario_1.json")

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
    main(100)
