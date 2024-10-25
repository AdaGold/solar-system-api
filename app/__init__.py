from flask import Flask
from app.db import db, migrate
from app.routes.planets_routes import planet_bp


def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(planet_bp)

    return app
