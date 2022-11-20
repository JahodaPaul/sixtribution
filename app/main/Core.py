import os

import numpy as np
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
            if car_dict["station_id"] is not None and car_dict["station_id"] not in self.stations:
                raise Exception(f"Station ID {car_dict['station_id']} not found in the station list! "
                                f"Please assign a valid station ID to the car {car_id}!")

            self.fleet[car_id] = Car(car_id=car_id,
                                     longitude=np.random.normal(0.0, 0.012, 1)[0] + 48.145,
                                     latitude=np.random.normal(0.0, 0.018, 1)[0] + 11.450,
                                     battery_lvl=car_dict["battery_level"],
                                     charging_station_id=car_dict["station_id"],
                                     state=car_dict["state"])

    def update_fleet(self):
        # then update all the vehicles and their states
        for car_id in self.fleet:
            self.fleet[car_id].update(self)

        self.current_simulation_step -= 1

    def initialize_stations(self):
        """
        :param init_station_state:
        :return:
        """
        path_t = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../data/stations.txt")
        with open(path_t, "r") as file:
            lines = [line.rstrip() for line in file]
        for line in lines:
            items = line.strip().split(",")
            station_id = int(items[0])
            lat = items[1]
            lon = items[3]
            capacity = int(items[4])
            operator = items[5]

            station = Station(longitude=lon, latitude=lat, total_capacity=capacity, station_id=station_id,
                              station_provider=operator)
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

    def pretty_print_car_states(self):
        for car_id in self.fleet:
            car_position = self.fleet[car_id].get_position()
            if self.fleet[car_id].get_state() == "returning" or self.fleet[car_id].get_state() == "charging" or self.fleet[car_id].get_state() == "free":
                station_position = self.stations[self.fleet[car_id].get_charging_station()].get_position()
                distance_to_dst = self.euclidean_distance(car_position=car_position,
                                                          station_position=station_position)

                print(f"Car ID: '{car_id:.<3}', State: '{self.fleet[car_id].get_state():<10}', "
                      f"Battery Level: '{self.fleet[car_id].get_battery_level():.<5}', "
                      f"Charging Station: '{self.fleet[car_id].get_charging_station():.<10}', "
                      f"Distance to Charging Station: '{distance_to_dst:.<5}', "
                      f"Current Position: '{car_position[0]:.5f} {car_position[1]:.5f}', "
                      f"Destination: '{station_position[0]:.5f} {station_position[1]:.5f}'")
            else:
                print(f"Car ID: '{car_id:.<3}', State: '{self.fleet[car_id].get_state():<10}', "
                      f"Battery Level: '{self.fleet[car_id].get_battery_level():.<5}', "
                      f"Charging Station: '{self.fleet[car_id].get_charging_station():.<10}', "
                      f"Current Position: '{car_position[0]:.5f} {car_position[1]:.5f}'")
