from flask_restful import Resource


class Example(Resource):
    def get(self, x):
        return x + x

