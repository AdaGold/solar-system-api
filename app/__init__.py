from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    from .routes.planet_routes import planets_bp
    app.register_blueprint(planets_bp)

    from .routes.satellite_routes import satellite_bp
    app.register_blueprint(satellite_bp)
    
    return app
