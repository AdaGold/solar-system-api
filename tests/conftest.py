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
    planet = Planet(name="Mars", description="Roman god of war, aka Ares.", number_of_moons=2)
    db.session.add(planet)
    db.session.commit()
    return planet
# jasmin

@pytest.fixture
def two_planets(app):
    # Arrange
    planet_one = Planet(name="Jupiter",
                        description="King of the Roman gods, aka Zeus.",
                        number_of_moons=79)
    planet_two = Planet(name="Mars",
                        description="Roman god of war, aka Ares.",
                        number_of_moons=2)

    db.session.add_all([planet_one, planet_two])
    db.session.commit()
    return [planet_one, planet_two]