import pytest
from app import create_app, db
from flask.signals import request_finished
from app.models.planet import Planet
from app.models.moon import Moon

@pytest.fixture
def app():
    app = create_app(test_config=True)

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
    Mercury_planet = Planet(
        name="Mercury",
        description="Mercury is the smallest planet of our solar system.",
        is_rocky=True
    )

    Venus_planet = Planet(
        name="Venus",
        description="Venus is the hottest planet in the solar system.",
        is_rocky=True
    )
    db.session.add_all([Mercury_planet, Venus_planet])
    db.session.commit()
    db.session.refresh(Mercury_planet, ["id"])
    db.session.refresh(Venus_planet, ["id"])

@pytest.fixture
def one_saved_planet(app):
    Mercury_planet = Planet(
        name="Mercury",
        description="Mercury is the smallest planet of our solar system.",
        is_rocky=True
    )
    db.session.add(Mercury_planet)
    db.session.commit()
    db.session.refresh(Mercury_planet, ["id"])

@pytest.fixture
def one_planet_with_moon(app):
    earth = Planet(
        name="Earth",
        description="Earth is the only planet with life.",
        is_rocky=True
    )
    db.session.add(earth)
    db.session.commit()
    db.session.refresh(earth, ["id"])

    moon = Moon(
        name = "Moon",
        size = "2500",
        description = "The only natural satelite around Earth",
        gravity = 0.2
    )
    moon.planet = earth
    db.session.add(moon)
    db.session.commit()

@pytest.fixture
def three_saved_planets(app):
    Mercury_planet = Planet(
        name="Mercury",
        description="Mercury is the smallest planet of our solar system.",
        is_rocky=True
    )

    Venus_planet = Planet(
        name="Venus",
        description="Venus is the hottest planet in the solar system.",
        is_rocky=True
    )

    Earth_planet = Planet(
        name="Earth",
        description="This is the only place where there is life.",
        is_rocky=True
    )
    
    db.session.add_all([Mercury_planet, Venus_planet, Earth_planet])
    db.session.commit()
    db.session.refresh(Mercury_planet, ["id"])
    db.session.refresh(Venus_planet, ["id"])
    db.session.refresh(Earth_planet, ["id"])

@pytest.fixture
def one_planet_with_two_moons(app):
    Mars_planet = Planet(
        name="Mars",
        description="This planet is very cold and dry but there is ice at the poles.",
        is_rocky=True
    )
    db.session.add(Mars_planet)
    db.session.commit()
    db.session.refresh(Mars_planet, ["id"])

    one_moon = Moon(
        name = "Phobos",
        size = "14",
        description = "It flies around Mars three times in one Martian day.",
        gravity = 0.0057
    )
    one_moon.planet = Mars_planet
    
    two_moon = Moon(
        name = "Deimos",
        size = "8",
        description = "It is further from Mars, so each orbit around the planet takes a little over one day.",
        gravity = 0.003
    )
    two_moon.planet = Mars_planet
    
    db.session.add_all([one_moon, two_moon])
    db.session.commit()

    