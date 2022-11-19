import os

from app.main.Car import Car
from app.main.StationDatabase import Station


class Core:
    def __init__(self, simulation_length):
        self.simulation_duration = simulation_length
        self.current_simulation_step = self.simulation_duration
        self.fleet = {}
        self.stations = {}

    def get_fleet(self):
        return self.fleet

    def get_stations(self):
        return self.stations

    def initialize_fleet(self, initial_state_dict):
        for car_id, car_dict in initial_state_dict.items():
            self.fleet[car_id] = Car(car_id=car_id,
                                     longitude=car_dict["latitude"],
                                     latitude=car_dict["longitude"],
                                     battery_lvl=car_dict["battery_level"],
                                     charging_station_id=car_dict["station_id"],
                                     state=car_dict["state"])

    def update_fleet(self, update_dict):
        # first update all the vehicles
        for car_id, car_dict in update_dict["cars"].items():
            self.fleet[car_id].update(car_dict)

        # then update all the stations
        # for station in self.stations:
        #     station.update()

        self.current_simulation_step -= 1

    def initialize_stations(self, init_station_state):
        path_t = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../data/stations.txt")
        with open(path_t, "r") as file:
            lines = [line.rstrip() for line in file]
        for line in lines:
            items = line.strip().split(",")
            station_id = int(items[0])
            lat = items[1]
            lon = items[3]
            capacity = int(items[4])

            station = Station(longitude=lon, latitude=lat, total_capacity=capacity, station_id=station_id)
            self.stations[station_id] = station

    def get_current_simulation_step(self):
        return self.current_simulation_step

    def get_total_simulation_duration(self):
        return self.simulation_duration