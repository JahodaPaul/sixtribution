from Core import Core


def main():
    core = Core(500)

    # TODO initialize cars and stations
    core.initialize_fleet()
    core.initialize_stations()
    # each time stamp corresponds to 1 hour
    while True:
        core.update_fleet()




if __name__ == "__main__":
    main()
