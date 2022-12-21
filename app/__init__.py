from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()  # Create a database
migrate = Migrate() 

def create_app(test_config=None):
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False # Don't sort keys alphabetically  
    # Database Config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Connection String
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'

    db.init_app(app)  # Tell database this is the app it will work with
    migrate.init_app(app, db) # Tell migrate this is the app to work with and the way to get to the database
    
    from .planet_routes import planets_bp 
    from app.Models.planet import Planet # Import our model, before we do anything with our API 
    app.register_blueprint(planets_bp)  

    return app
