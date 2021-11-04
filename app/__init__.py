from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()       # library that faciliates the communication between Python program and database
migrate = Migrate()         # we will need it when we need to change the structur of the db
# handling database migration
load_dotenv()


# postgresql+psycopg2://postgres:postgres@localhost:5432/ada_books_development

def create_app(test_config=None):
    app = Flask(__name__)

    #DB Config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # our application doesn;t use the Flask-SQLAlchemy even system, no need to track modificatinos
    if not test_config:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    
    else:
        app.config["TESTING"] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    # we need to tell Flask where to find our database

    db.init_app(app)
    migrate.init_app(app, db) # cconnect db and migrate to our Flask app, using the package's recommended snytax
    from app.models.planet import Planet # Book model will be available to the app 

    from .routes import planets_bp
    app.register_blueprint(planets_bp)
    
    return app

