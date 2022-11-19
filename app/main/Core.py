import os

from geopy import distance

from app.main.Car import Car
from app.main.Station import Station


class Core:
    def __init__(self, simulation_length):
        self.simulation_duration = simulation_length
        self.current_simulation_step = self.simulation_duration
        self.fleet = {}
        self.stations = {}

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
            self.fleet[car_id].update(car_dict, self)

        # then update all the stations
        for station in self.stations:
            self.stations[station].charge_cars(self)

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

    def find_optimal_station(self, car_id):
        # TODO optimize criteria
        station_id = self.get_station_list_by_distance(car_id=car_id, type="euclidean")
        return station_id

    def get_station_list_by_distance(self, car_id, type="euclidean"):
        eligible_stations = []
        if type == "euclidean":
            for station_id in self.stations:
                if not self.stations[station_id].has_space():
                    continue
                dist_to_station = self.euclidean_distance(car_position=self.fleet[car_id].get_position(),
                                                          station_position=self.stations[station_id].get_position())
                eligible_stations.append((station_id, dist_to_station))

        # find the closest station
        eligible_stations.sort(key=lambda x: x[1])
        return eligible_stations[0][0]

    @staticmethod
    def euclidean_distance(car_position, station_position):
        # function automatically calculates geographical distance
        return distance.distance(car_position, station_position).meters

    def get_current_simulation_step(self):
        return self.current_simulation_step

    def get_total_simulation_duration(self):
        return self.simulation_duration

    def get_fleet(self):
        return self.fleet

    def get_stations(self):
        return self.stations

