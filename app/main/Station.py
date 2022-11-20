
class Station:
    def __init__(self, longitude, latitude, total_capacity, station_id, station_provider):
        assert isinstance(total_capacity, int)
        assert total_capacity > 0, "Capacity must be greater than 0!"

        self.longitude = float(longitude)
        self.latitude = float(latitude)
        self.total_capacity = total_capacity
        self.station_id = station_id
        self.occupied_capacity = list()     # discontinued due to serialization set()
        self.charging_constant = 2.5
        self.station_provider = station_provider

    def add_to_station(self, car_id):
        """
        Return True if the car was added to the station, False otherwise.
        """
        if self.has_space():
            if car_id not in self.occupied_capacity:
                self.occupied_capacity.append(car_id)
                return True
        else:
            raise Exception(f"Station {self.station_id} is full! Can't add car {car_id}!")
            # TODO uncomment for deployment -> return False

    def detach_from_station(self, car_id):
        if car_id in self.occupied_capacity:
            self.occupied_capacity.remove(car_id)
        else:
            raise Exception(f"Car {car_id} is not in station {self.station_id}!")

    # moved to car
    # def charge_cars(self, core_instance):
    #     # print("capacity: ", self.occupied_capacity)
    #     for car_id in self.occupied_capacity:
    #         if core_instance.fleet[car_id].get_state() == core_instance.fleet[car_id].CHARGING:
    #             battery_lvl = core_instance.fleet[car_id].get_battery_level() + self.charging_constant
    #             print("Charging car: ", car_id, " to: ", battery_lvl)
    #             core_instance.fleet[car_id].set_battery_level(min(battery_lvl, 100))
    #             # only charge the car if it is not full
    #             # if 0 < battery_lvl <= 100:
    #             #     print(f"Charging car {car_id} at station {self.station_id}! "
    #             #           f"Previous battery level: {core_instance.fleet[car_id].get_battery_level()}% "
    #             #           f"Current battery level: {battery_lvl}%")

    def has_space(self):
        return self.total_capacity > len(self.occupied_capacity)

    def get_position(self):
        return self.latitude, self.longitude

    def get_id(self):
        return self.station_id
