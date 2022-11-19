from flask_restful import Resource
import pickle
import json


class Stations(Resource):
    def get(self):
        with open('data/stations_current.pickle', 'rb') as pickle_file:
            stations = pickle.load(pickle_file)
        for key in stations.keys():
            stations[key] = json.dumps(stations[key].__dict__)
        return stations