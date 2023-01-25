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
def one_saved_planet():
    planet = Planet(name='Earth', description='The blue marble', rings=False)
    db.session.add(planet)
    db.session.commit()
    return planet

@pytest.fixture
def all_planets():
    planets = [
        Planet(name="Mercury", description="The smallest planet", rings=False),
        Planet(name="Venus", description="The hottest planet", rings=False),
        Planet(name="Earth", description="The blue marble", rings=False),
        Planet(name="Mars", description="The red planet", rings=False),
        Planet(name="Jupiter", description="The gas giant", rings=False),
        Planet(name="Saturn", description="The second largest planet", rings=True),
        Planet(name="Uranus", description="This planet spins on its side", rings=True),
        Planet(name="Neptune", description="The most distant planet from the sun", rings=False)
        ]

    db.session.add_all(planets)
    db.session.commit()
    return planets
