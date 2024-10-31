import pytest
from app import create_app
from app.db import db
from flask.signals import request_finished
from dotenv import load_dotenv
import os
from app.models.planet import Planet

load_dotenv()

@pytest.fixture
def app():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    }
    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def saved_all_planets():
    db.session.add(Planet(name="Venus", description="Hottest planet", size = "small", moons=0, has_flag=False))
    db.session.add(Planet(name="Mercury", description="Closest to the Sun, very hot", size="Small", moons=0, has_flag=False))
    db.session.add(Planet(name="Venus", description="Thick atmosphere, hottest planet", size="Small", moons=0, has_flag=False))
    db.session.add(Planet(name="Earth", description="Home to life, oceans and land", size="Medium", moons=1, has_flag=True))
    db.session.add(Planet(name="Mars",    description="Known as the Red Planet", size="Small", moons=2, has_flag=True))
    db.session.add(Planet(name="Jupiter", description="Largest planet, gas giant", size="Large", moons=79, has_flag=False))
    db.session.add(Planet(name="Saturn",  description="Known for its rings", size="Large", moons=83, has_flag=False))
    db.session.add(Planet(name="Uranus",  description="Icy gas giant, tilted axis", size="Large", moons=27, has_flag=False))
    db.session.commit()