from flask import Flask
from app.routes.planet_routes import planets_bp


def create_app(test_config=None):
    app = Flask(__name__)

    # Register blueprints here
    app.register_blueprint(planets_bp)

    return app
