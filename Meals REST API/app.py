from flask import Flask, app

# default MongoDB config

default_config = {
    'MONGODB_SETTINGS': {
        'db': 'meals',
        'host': 'localhost',
        'port': 27017,
        'username': 'admin',
        'password': '2006',
        'authentication_source': 'admin'
    }
}


def get_flask_app(config: dict = None) -> app.Flask:
    """
    Initializes Flask app with given configuration.
    Main entry point for wsgi (gunicorn) server.
    :param config: Configuration dictionary
    :return: Flask app
    """
    flask_app = Flask(__name__)
    config = default_config if config is None else config
    return flask_app


if __name__ == '__main__':
    app = get_flask_app()
    app.run(debug=True)
