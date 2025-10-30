from flask import Flask
from .db import db, migrate
from .models.planet import Planet
from app.routes.planet_routes import planets_bp
import os


def create_app(config=None):
    app = Flask(__name__)

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    if config:
        app.config.update(config)
        
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints here
    app.register_blueprint(planets_bp)

    return app
