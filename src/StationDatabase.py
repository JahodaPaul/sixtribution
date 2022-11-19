
class Station:
    def __init__(self, lon, lat, capacity, station_id):
        self.lon = lon
        self.lat = lat
        self.capacity = capacity
        self.station_id = station_id

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
            station = Station(lon=lon,lat=lat,capacity=capacity,station_id=id)
            self.stations[id] = station

        return self.stations




# st = StationDatabase()
# stations = st.get_stations()
# for key in stations.keys():
#     print(stations[key].station_id)