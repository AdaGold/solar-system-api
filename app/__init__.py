from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    app = Flask(__name__)

    # Database configuration:
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system'

    
    db.init_app(app) 
    migrate.init_app(app, db) 
    from app.models.planet import Planet # We want to do the import after we configure our the datababase and is set up and connected

    from .routes import planets_bp
    app.register_blueprint(planets_bp)
    
    return app


