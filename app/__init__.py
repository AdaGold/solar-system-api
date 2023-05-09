from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from dotenv import load_dotenv
import os

# postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development

db =SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)

    #DB Config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   
    if not test_config:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    else:
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')

    db.init_app(app)
    migrate.init_app(app, db)
    from app.models.planet import Planet
    from app.models.moon import Moon

    from app.routes.planet_routes import planets_bp
    from app.routes.moon_routes import moons_bp
    app.register_blueprint(planets_bp)
    app.register_blueprint(moons_bp)

    # from app.models.<model> import <model>
    
    return app
