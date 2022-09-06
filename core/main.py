from flask import Flask

from .controllers import register_views


def create_app():
    # Create a new Flask application.
    flask_app = Flask(__name__)

    # Register core controller endpoints.
    register_views(flask_app)

    return flask_app
