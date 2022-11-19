from Core import Core

def main():
    core = Core(500)
    core.GenerateFleet()
    # each time stamp corresponds to 1 hour
    while True:
        core.MoveFleet()



if __name__ == "__main__":
    main()
