"""
This API was built using Johnathon Barhydt's tutorial:
https://towardsdatascience.com/creating-a-beautiful-web-api-in-python-6415a40789af
"""
from flask import Flask, app
from flask_mongoengine import MongoEngine
from flask_restful import Api

from api.meals import MealsApi
from api.users import UsersApi
from api.auth import LogInApi, SignUpApi

# default test config
# (for production pass config dict to get_flask_app()
# through env vars specified in cloud platform)
default_config = {
    'MONGODB_SETTINGS': {
        'db': 'meals',
        'host': 'localhost',
        'port': 27017
    }
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

    # init api and routes
    api = Api(app=flask_app, catch_all_404s=True)
    create_routes(api=api)

    # init mongoengine
    db = MongoEngine(app=flask_app)
    return flask_app


def create_routes(api):
    # create routes for resources (api classes)
    api.add_resource(SignUpApi, '/auth/signup/')
    api.add_resource(LogInApi, '/auth/login/')
    api.add_resource(UsersApi, '/users/')
    api.add_resource(UsersApi, '/users/<user_id>')
    api.add_resource(MealsApi, '/meals/')
    api.add_resource(MealsApi, '/meals/<meal_id>')


if __name__ == '__main__':
    app = get_flask_app()
    app.run(debug=True)
