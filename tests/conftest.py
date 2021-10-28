import pytest
from app import create_app
from app import db
from app.Model.planet import Planet
from flask import Flask


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def create_two_planets(app):
    planet_1 = Planet(name="Not Planet", description="Not a real planet", mythology="False")
    planet_2 = Planet(name="Real Planet", description="No really a planet", mythology="Truly I have a myth")
    
    db.session.add_all([planet_1, planet_2])
    db.session.commit()