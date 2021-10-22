from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# creating a class instance of SQLAlchemy
db= SQLAlchemy()
# creating a class instance of Migrate class
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)
    from .routes import planets_bp
    app.register_blueprint(planets_bp)
    # setting a SQLAlchemy config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # establishing connection string to the database, 5432 is the port for postgres
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'
    # connects db and migrate to Flask app, using package syntax
    db.init_app(app)
    migrate.init_app(app, db)
    from app.Models.planets import Planet
    
    return app
