# services/users/project/__init__.py

import os # new 
from flask import Flask, jsonify
from flask_restful import Resource, Api
import sys # new


# instantiate the app
app = Flask(__name__)

api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS')  # new
app.config.from_object(app_settings)      # new


class UsersPing(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }


api.add_resource(UsersPing, '/users/ping')