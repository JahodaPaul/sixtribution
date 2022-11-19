from flask_restful import Api
from app.controllers.user import UserList, User
from app.controllers.example import Example
from app.controllers.Stations import Stations
from app.main.errors import errors

# Flask API Configuration
api = Api(
    catch_all_404s=True,
    errors=errors,
    prefix='/api'
)

api.add_resource(UserList, '/users')
api.add_resource(User, '/users/<int:id>/')
api.add_resource(Example, '/example/<int:x>')
api.add_resource(Stations, '/stations')