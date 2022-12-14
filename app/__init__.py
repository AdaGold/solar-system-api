from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    from .routes import planets_bp, moons_bp
    app.register_blueprint(planets_bp)
    app.register_blueprint(moons_bp)
    return app
