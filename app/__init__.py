from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


#postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development
db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    app.config['JSON_SORT_KEYS'] = False # Don't sort keys alphabetically
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'


    db.init_app(app)
    migrate.init_app(app, db)
    
    from app.Models.planet import Planets
    from .planet_routes import planets_bp 

    app.register_blueprint(planets_bp)  

    return app
