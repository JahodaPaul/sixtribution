from src.Car import Car
from src.StationDatabase import Station


class Core:
    def __init__(self, simulation_length):
        self.simulation_duration = simulation_length
        self.current_simulation_step = self.simulation_duration
        self.fleet = {}
        self.stations = {}

    def initialize_fleet(self, n_cars):
        for i in range(0, n_cars):
            self.fleet[i] = Car(i)

    def update_fleet(self, update_dict):
        # first update all the vehicles
        for car_id, car_dict in update_dict["cars"].items():
            self.fleet[car_id].update_position(car_dict["latitude"], car_dict["longitude"])
            self.fleet[car_id].update_lock_status(car_dict["locked"])
            self.fleet[car_id].update_battery_level(car_dict["battery_level"])
            self.fleet[car_id].update_wants_to_return(car_dict["wants_to_return"])
            self.fleet[car_id].update_charging_status(car_dict["charging_station_id"], car_dict["is_charging"])

        # then update all the stations
        # for station in self.stations:
        #     station.update()

        self.current_simulation_step -= 1

    def initialize_stations(self, n_stations):
        for i in range(0, n_stations):
            self.stations[i] = Station(lat=20.2, lon=20.2, capacity=2, station_id=i)

    def get_current_simulation_step(self):
        return self.current_simulation_step

    def get_total_simulation_duration(self):
        return self.simulation_duration