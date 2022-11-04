from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    from app.models.planet import Planet
    
    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import bp
    app.register_blueprint(bp)

    return app
