import pytest
from app import create_app
from app import db
from app.models.planet import Planet


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
def one_planet(app):
    planet = Planet(
        description = "Mercury has 0 moon(s).",
        name = "Mercury",
        num_of_moons = 0)
    db.session.add(planet)
    db.session.commit()


@pytest.fixture
def many_planets(app):
    planet_1 = Planet(
        description = "Mercury has 0 moon(s).",
        name = "Mercury",
        num_of_moons = 0)
    planet_2 = Planet(
        description = "Venus has 0 moon(s).",
        name = "Venus",
        num_of_moons = 0)
    db.session.add_all([planet_1, planet_2])
    db.session.commit()
