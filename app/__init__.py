from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv


db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)
    
    if not test_config:
        #hide a warning about a feature in SQLAlchemy that we wont be using
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        #set app.config['SQLALCHEMY_DATABASE_URI'] to the connection string for our database
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    else:
        app.config['TESTING'] = True
        app.config['SQALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    db.init_app(app)
    migrate.init_app(app,db)

    from app.models.planet import Planet

    from .routes import planet_bp
    app.register_blueprint(planet_bp)

    return app


# def create_app(test_config=None):
#     app = Flask(__name__)
#     #DB configs
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'

#     #import models here
#     from app.models.book import Book
    
#     db.init_app(app)
#     migrate.init_app(app,db)
    
#     #registers blueprints here
#     from .routes import hello_world_bp
#     app.register_blueprint(hello_world_bp)
    
#     return app