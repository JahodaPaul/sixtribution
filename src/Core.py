from src.Car import Car
from src.StationDatabase import Station


class Core:
    def __init__(self, simulation_length):
        self.simulation_duration = simulation_length
        self.current_simulation_step = self.simulation_duration
        self.fleet = {}
        self.stations = {}

    def initialize_fleet(self, init_car_state):
        for car_id, car_dict in init_car_state.items():
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
        for station_id, station_dict in init_station_state.items():
            self.stations[station_id] = Station(longitude=station_dict["longitude"],
                                                latitude=station_dict["latitude"],
                                                total_capacity=station_dict["capacity"],
                                                station_id=station_id)

    def get_current_simulation_step(self):
        return self.current_simulation_step

    def get_total_simulation_duration(self):
        return self.simulation_duration