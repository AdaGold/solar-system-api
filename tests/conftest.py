import pytest
from app import create_app, db
from app.models.planet import Planet
from flask.signals import request_finished

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
        name="Earth", 
        size=4, 
        description="Earth is the third planet from the Sun and the only astronomical object known to harbor life.",
        distance_from_earth=0
    )

    db.session.add(planet)
    db.session.commit()
    db.session.refresh(planet, ["id"])
    return planet

@pytest.fixture
def many_planets(app):
    earth_planet = Planet(
                    name="Earth", 
                    size=4,
                    description="Earth is the third planet from the Sun and the only astronomical object known to harbor life.",
                    distance_from_earth=0
                    )
    mars_planet = Planet(
                    name="Mars", 
                    size=7,
                    description="Mars is the fourth planet from the Sun a dusty, cold, desert world with a very thin atmosphere.",
                    distance_from_earth=61.194
                    )
    jupiter_planet = Planet(
                    name="Jupiter", 
                    size= 1,
                    description="Jupiter is a gas giant with a mass more than two and a half times that of all the other planets combined.",
                    distance_from_earth=468.62
                    )
    planets = [earth_planet, mars_planet, jupiter_planet]
    db.session.add_all(planets)
    db.session.commit()
    #db.session.refresh(planets, ["id"])
    return planets
