

class Core:
    def __init__(self, simulation_length):
        self.simulation_length = simulation_length
        self.fleet = []
        self.stations = []

    def initialize_fleet(self, n_cars):
        for i in range(0, n_cars):
            car = Car(i)
            self.fleet.append(car)

    def update_fleet(self):
        pass

    def initialize_stations(self, n_stations):
        for i in range(0, n_stations):
            station = Station(i)
            self.stations.append(station)