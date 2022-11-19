import json

from Core import Core
from app.controllers.Stations import Stations


def get_initial_state():
    with open("./../../data/test_scenarios/scenario_1/init.json", "r") as f:
        init_state = json.load(f)
    print(init_state)
    return init_state


def get_core_update():
    """
    This function is meant as a substitute for the actual online update function, it should return data in the form of:

    "state":
     - booked -> car is in use and we don't know where it will be dropped off
     - returning -> car is going to a charging station TODO here we recommend the optimal location
     - free -> car is parked at the charging station and is available for booking or charging
     - charging -> car is charging at the charging station and is actually charging
    :return:
    {
    "cars" {
        "car_id": {
            "latitude": <float latitude>,
            "longitude": <float longitude >,
            "battery_level": <int 0-100>,
            "station_id": <int id>,
            "state": "booked" / "returning" / "free" (meaning it is parked) / "charging"
            },
        0: {
            "latitude": 20.2,
            "longitude": 20.2,
            "battery_level": 50,
            "station_id": 0,
            "state": "booked"
        }
    }
    """
    # TODO make path relative
    with open("./../../data/test_scenarios/scenario_1/scenario_1.json", "r") as f:
        core_update = json.load(f)
    print(core_update)
    return core_update


def main():
    # TODO should keys be string or ints? determine later
    core = Core(10)

    initial_state = get_initial_state()
    # stations have to be initialized first, because cars will update their capacity
    core.initialize_stations(initial_state["stations"])
    core.initialize_fleet(initial_state["cars"])

    controller_stations = Stations()

    # get simulated data
    trip_history = get_core_update()

    # each time stamp corresponds to 1 hour
    total_sim_duration = core.get_total_simulation_duration()
    time_stamp = 0
    while core.get_current_simulation_step() > 0:
        print(f"\nSimulation step {total_sim_duration - core.get_current_simulation_step() + 1} / {total_sim_duration}")

        update_core = trip_history[str(time_stamp)] if len(trip_history) > time_stamp else trip_history["3"]  # get_core_update()
        core.update_fleet(update_core)

        # frontend stuff
        stations = core.get_stations()
        fleet = core.get_fleet()
        controller_stations.update(stations)
        time_stamp += 1


if __name__ == "__main__":
    main()
