from flask import Flask
from .routes import planets_bp


def create_app(test_config=None):
    app = Flask(__name__)

    app.register_blueprint(planets_bp)

    return app
