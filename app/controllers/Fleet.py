from flask_restful import Resource
import pickle
import json


class Fleet(Resource):
    def get(self):
        with open('data/fleet_current.pickle', 'rb') as pickle_file:
            fleet = pickle.load(pickle_file)
        for key in fleet.keys():
            fleet[key] = json.dumps(fleet[key].__dict__)
        return fleet