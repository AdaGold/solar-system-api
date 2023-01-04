import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet
from app.models.moon import Moon
from app.routes.planet import validate_planet


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
def two_saved_planets(app):
    test_one = Planet(
    name="Neptune",
        description="Named for the god of the sea because it is blue",
        mass=102,
        diameter=49528,
        density=1638,
        gravity=11.0,
        escape_velocity=23.5,
        rotation_period=16.1,
        day_length=16.1,
        distance_from_sun=4515,
        orbital_period=59800,
        orbital_velocity=5.4,
        orbital_inclination=1.8,
        orbital_eccentricity=0.01,
        obliquity_to_orbit=28.3,
        mean_tempurature_c=-200,
        surface_pressure=None,
        global_magnetic_feild=True,
        img="https://solarsystem.nasa.gov/resources/611/neptune-full-disk-view/?category=planets_neptune",
        has_rings=True,
    )
    test_two = Planet(name="number two")

    db.session.add_all([test_one, test_two])

    db.session.commit()


@pytest.fixture
def two_saved_moons(app, two_saved_planets):
    planet_one = validate_planet(1)
    moon_one=Moon(name="Test Moon", description="First Moon for Neptune", image="pretty_moon.jpg", planet_id=1)
    moon_two=Moon(name="2 Test Moon", description="Second Neptune", image="prettiestMoon.jpg", planet_id = 1)

    db.session.add_all([moon_one,moon_two])
    db.session.commit()

