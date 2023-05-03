import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

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
def one_planet(app):
    planet = Planet(
            name = "Uranus",
            description = "7th planet from the Sun",
            color = "dark blue"
            )
    db.session.add(planet)
    db.session.commit()

    return planet

@pytest.fixture
def two_planets(app):
    planet_one = Planet(
            name = "Mars",
            description = "3rd planet from the Sun",
            color = "red"
            )
    planet_two = Planet(
            name = "Venus",
            description = "2nd planet from the Sun",
            color = "orange"
            )
    db.session.add_all([planet_one, planet_two])
    db.session.commit()

    return planet_one, planet_two