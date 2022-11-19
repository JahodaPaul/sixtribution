from flask_restful import Resource


class Stations(Resource):
    def __int__(self):
        self.stations = {}
        
    def get(self):
        return self.stations

    def update(self, stations):
        self.stations = stations