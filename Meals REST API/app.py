"""
This API was built with the help of Johnathon Barhydt's tutorial:
https://towardsdatascience.com/creating-a-beautiful-web-api-in-python-6415a40789af,
but with my personal changes and additions.
"""
import os

from flask import app, Flask
from flask_mongoengine import MongoEngine
from flask_restful import Api
from flask_jwt_extended import JWTManager

from api.meals import MealsApi, MealApi
from api.users import UsersApi, UserApi
from api.auth import LogInApi, SignUpApi

# default test config
# (for production pass config dict to get_flask_app()
# through env vars specified in cloud platform)
default_config = {
    'MONGODB_SETTINGS': {
        'db': 'meals',
        'host': 'localhost',
        'port': 27017
    },
    'JWT_SECRET_KEY': 'MY_JWT_SECRET_KEY'
}


def get_flask_app(config: dict = None) -> app.Flask:
    """
    Initializes Flask app with given configuration.
    Main entry point for wsgi (gunicorn) server.
    :param config: Configuration dictionary
    :return: Flask app
    """
    # init flask app
    flask_app = Flask(__name__)

    # configure flask app
    config = default_config if config is None else config
    flask_app.config.update(config)

    @flask_app.route('/')
    def index():
        return 'Meals API for managing users and their favourite meals'

    # load config variables
    if 'MONGODB_URI' in os.environ:
        flask_app.config['MONGODB_SETTINGS'] = {'host': os.environ['MONGODB_URI'],
                                                'retryWrites': False}
    if 'JWT_SECRET_KEY' in os.environ:
        flask_app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']

    # init api and routes
    api = Api(app=flask_app, catch_all_404s=True)
    create_routes(api=api)

    # init mongoengine
    MongoEngine(app=flask_app)

    # init JWTManager
    JWTManager(app=flask_app)

    return flask_app


def create_routes(api):
    # create routes for resources (api classes)
    api.add_resource(SignUpApi, '/auth/signup')
    api.add_resource(LogInApi, '/auth/login')
    api.add_resource(UsersApi, '/users')
    api.add_resource(UserApi, '/users/<user_id>')
    api.add_resource(MealsApi, '/meals')
    api.add_resource(MealApi, '/meals/<meal_id>')


if __name__ == '__main__':
    app = get_flask_app()
    app.run(debug=True)
