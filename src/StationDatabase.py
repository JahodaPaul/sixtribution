
class Station:
    def __init__(self, longitude, latitude, total_capacity, station_id):
        assert total_capacity > 0, "Capacity must be greater than 0!"

        self.longitude = longitude
        self.latitude = latitude
        self.total_capacity = total_capacity
        self.station_id = station_id
        self.occupied_capacity = set()

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


class StationDatabase:
    def __init__(self):
        self.stations = {}

    def get_stations(self):
        with open('data/stations.txt','r') as file:
            lines = [line.rstrip() for line in file]
        for line in lines:
            items = line.split(',')
            id = int(items[0])
            lat = items[1]
            lon = items[2]
            capacity = items[3]
            station = Station(lon=lon, lat=lat, total_capacity=capacity, station_id=id)
            self.stations[id] = station

        return self.stations




# st = StationDatabase()
# stations = st.get_stations()
# for key in stations.keys():
#     print(stations[key].station_id)