from flask import Flask
from .routes.routes import solar_system_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(solar_system_bp)

    return app
