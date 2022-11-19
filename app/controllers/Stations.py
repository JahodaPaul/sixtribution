from flask_restful import Resource
import pickle
import json


class Stations(Resource):

    def get(self):
        # json_str = ""
        # json_dict = {}
        with open('data/stations_current.pickle', 'rb') as pickle_file:
            stations = pickle.load(pickle_file)
        for key in stations.keys():
            stations[key] = json.dumps(stations[key].__dict__)
            # json_str = json_str
        return stations

    # def update(self, stations):
    #     self.stations = stations