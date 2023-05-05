import pytest
from app import create_app, db
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
        name="Xplanet",
        description="A far away place"
    )

    db.session.add(planet)
    db.session.commit()
    return planet

@pytest.fixture
def two_saved_planets(app):
    test_planet_1 = Planet(
                    name = "Tatooine",
                    description = "Teenage"
    )
    test_planet_2 = Planet (
                    name = "Hoth", 
                    description = "You're a cold as ice"
                    )
    test_planets = [test_planet_1, test_planet_2]

    db.session.add_all(test_planets)
    db.session.commit()

    return test_planets