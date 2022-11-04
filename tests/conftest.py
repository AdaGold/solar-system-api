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
def two_saved_planets(app):
    # Arrange
    venus_planet = Planet(name="Venus",
                    description="a fun planet to be on",
                    diameter = "2,374 km")
    mars_planet = Planet(name="Mars",
                        description="home of the martians",
                        diameter="3,456 km")

    db.session.add_all([venus_planet, mars_planet])
    db.session.commit()

@pytest.fixture
def client(app):
    return app.test_client()