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
    total_sim_duration = core.get_total_simulation_duration()
    while core.get_current_simulation_step() > 0:
        print(f"Simulation step {total_sim_duration - core.get_current_simulation_step() + 1} / {total_sim_duration}")

        update_core = get_core_update()
        core.update_fleet(update_core)


if __name__ == "__main__":
    main()
