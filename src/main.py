from Core import Core


def get_core_update():
    core_update = {
        "cars": {
            0: {
                "latitude": 0,
                "longitude": 0,
                "battery_level": 0,
                "locked": True,
                "is_charging": False,
                "wants_to_return": False,
                "charging_station_id": None
            },
            1: {

            }
        },
    }
    return core_update


def main():
    core = Core(10)

    # TODO initialize cars and stations
    core.initialize_fleet(10)
    core.initialize_stations(5)

    # each time stamp corresponds to 1 hour
    while core.get_current_simulation_step() > 0:
        print(f"Simulation step {core.get_current_simulation_step()}")
        update_core = get_core_update()
        core.update_fleet(update_core)


if __name__ == "__main__":
    main()
