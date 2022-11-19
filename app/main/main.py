from app.main.Core import Core
import pickle
import time

def get_initial_state():
    return {
        "cars": {
            0: {
                "latitude": 20.2,
                "longitude": 22.2,
                "battery_level": 50,
                "station_id": None,
                "state": "booked"
            },
            1: {
                "latitude": 20.2,
                "longitude": 55.2,
                "battery_level": 50,
                "station_id": 0,
                "state": "free"
            },
            2: {
                "latitude": 20.2,
                "longitude": 43.2,
                "battery_level": 50,
                "station_id": 0,
                "state": "returning"
            },
            3: {
                "latitude": 20.2,
                "longitude": 43.2,
                "battery_level": 50,
                "station_id": 0,
                "state": "charging"
            }
        },
        "stations": {
            0: {
                "latitude": 20.2,
                "longitude": 43.2,
                "capacity": 3
            },
            1: {
                "latitude": 20.2,
                "longitude": 43.2,
                "capacity": 1
            }
        }
    }


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

    core_update = {
        "cars": {
            0: {
                "latitude": 20.2,
                "longitude": 22.2,
                "battery_level": 50,
                "station_id": None,
                "state": "booked"
            },
            1: {
                "latitude": 20.2,
                "longitude": 55.2,
                "battery_level": 50,
                "station_id": 0,
                "state": "free"
            },
            2: {
                "latitude": 20.2,
                "longitude": 43.2,
                "battery_level": 50,
                "station_id": 0,
                "state": "returning"
            },
            3: {
                "latitude": 20.2,
                "longitude": 43.2,
                "battery_level": 50,
                "station_id": 0,
                "state": "charging"
            }
        },
    }
    return core_update


def main():
    core = Core(1000)

    initial_state = get_initial_state()
    # stations have to be initialized first, because cars will update their capacity
    core.initialize_stations(initial_state["stations"])
    core.initialize_fleet(initial_state["cars"])

    # each time stamp corresponds to 1 hour
    total_sim_duration = core.get_total_simulation_duration()
    while core.get_current_simulation_step() > 0:
        print(f"Simulation step {total_sim_duration - core.get_current_simulation_step() + 1} / {total_sim_duration}")

        update_core = get_core_update()
        core.update_fleet(update_core)

        # frontend stuff
        stations = core.get_stations()
        fleet = core.get_fleet()

        with open('data/stations_current.pickle', 'wb') as outfile:
            pickle.dump(stations, outfile)

        with open('data/fleet_current.pickle', 'wb') as outfile:
            pickle.dump(fleet, outfile)

        time.sleep(1)



if __name__ == "__main__":
    main()
