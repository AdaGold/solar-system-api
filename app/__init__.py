from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv 
import os 

#postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development
db = SQLAlchemy()
migrate = Migrate(compare_type=True)
load_dotenv() 

def create_app(test_config=None):
    app = Flask(__name__)

    if test_config: 
        app.config['JSON_SORT_KEYS'] = False # Don't sort keys alphabetically
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")
        app.config["Testing"] = True 
    else:
        app.config['JSON_SORT_KEYS'] = False # Don't sort keys alphabetically
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")

    db.init_app(app)
    migrate.init_app(app, db)
    
    from app.models.planet import Planet
    from app.models.moon import Moon
    from .planet_routes import planets_bp 
    from .moon_routes import moon_bp

    app.register_blueprint(planets_bp)  
    app.register_blueprint(moon_bp)

    return app
