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
    # app.config['JSON_SORT_KEYS'] = False # Don't sort keys alphabetically
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if test_config: 
        app.config['JSON_SORT_KEYS'] = False # Don't sort keys alphabetically
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")
    else:
        app.config['JSON_SORT_KEYS'] = False # Don't sort keys alphabetically
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")

    db.init_app(app)
    migrate.init_app(app, db)
    
    from app.models.planet import Planet
    from .planet_routes import planets_bp 

    app.register_blueprint(planets_bp)  

    return app
