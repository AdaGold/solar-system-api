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
    new_planet = Planet(name="Earth", description="Earth description", moons=2)
        
    db.session.add(new_planet)
    db.session.commit()


@pytest.fixture
def two_saved_planets(app):
    # Arrange
    planet_mercury = Planet(name="Mercury",
                      description="Mercury description",
                      moons=1)
    planet_pluto = Planet(name="Pluto",
                         description="Pluto description",
                         moons=2
                         )

    db.session.add_all([planet_mercury, planet_pluto])
    # Alternatively, we could do
    # db.session.add(ocean_book)
    # db.session.add(mountain_book)
    db.session.commit()

