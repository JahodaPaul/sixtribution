
class Station:
    """
    Represents a physical charging station location, to which we direct our cars.
    """

    def __init__(self, longitude, latitude, total_capacity, station_id, station_provider):
        assert isinstance(total_capacity, int)
        assert total_capacity > 0, "Capacity must be greater than 0!"

        self.longitude = float(longitude)
        self.latitude = float(latitude)
        self.total_capacity = total_capacity
        self.station_id = station_id
        self.occupied_capacity = list()
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
            print(f"Station {self.station_id} is full! Can't add car {car_id}!")
            return False

    def detach_from_station(self, car_id):
        if car_id in self.occupied_capacity:
            self.occupied_capacity.remove(car_id)
        else:
            raise Exception(f"Car {car_id} is not in station {self.station_id}!")

    def has_space(self):
        return self.total_capacity > len(self.occupied_capacity)

    def get_position(self):
        return self.latitude, self.longitude

    def get_id(self):
        return self.station_id

    def get_provider(self):
        return self.station_provider