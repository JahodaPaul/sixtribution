
class Station:
    def __init__(self, longitude, latitude, total_capacity, station_id):
        assert isinstance(total_capacity, int)
        assert total_capacity > 0, "Capacity must be greater than 0!"

        self.longitude = longitude
        self.latitude = latitude
        self.total_capacity = total_capacity
        self.station_id = station_id
        self.occupied_capacity = list()

    def add_to_station(self, car_id):
        if self.total_capacity > len(self.occupied_capacity):
            self.occupied_capacity.add(car_id)
        else:
            raise Exception(f"Station {self.station_id} is full! Can't add car {car_id}!")

    def remove_from_station(self, car_id):
        if car_id in self.occupied_capacity:
            self.occupied_capacity.remove(car_id)
        else:
            raise Exception(f"Car {car_id} is not in station {self.station_id}!")
