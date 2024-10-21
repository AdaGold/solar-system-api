from flask import Flask
from .routes import solar_system_bp

def create_app(test_config=None):
    app = Flask(__name__)

    app.register_blueprint(solar_system_bp)

    return app
