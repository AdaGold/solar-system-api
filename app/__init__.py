from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db=SQLAlchemy()
migrate=Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    if not test_config:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
    #app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'

    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")




    db.init_app(app)
    migrate.init_app(app,db)

    ###QUESTION: Do we need this line? its in learn but im unsure why we need it?
    #from app.models.planet import Planet

    from.routes import planets_bp
    app.register_blueprint(planets_bp)

    return app

# commands to remember: 
# flask run -h localhost -p 3000
# FLASK_ENV=development flask run