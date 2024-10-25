from flask import Flask
from .db import db, migrate
from .models.planet import Planet
from app.routes.planet_routes import planets_bp


def create_app(test_config=None):
    app = Flask(__name__)

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development"
    )

    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints here
    app.register_blueprint(planets_bp)

    return app
