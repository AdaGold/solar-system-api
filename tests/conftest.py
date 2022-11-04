import pytest
from app import create_app
from app import db
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

from app.models.planet import Planet
# ...

@pytest.fixture
def two_saved_planets(app):
    # Arrange
    earth_planet = Planet(name="Earth",
                    description="Inhabits life",
                    size= "7,917.5 mi" )
    saturn_planet = Planet(name="Saturn",
                    description="Adorned with ringlets 0o0o0o",
                    size="72,367 mi")

    db.session.add_all([earth_planet, saturn_planet])
    db.session.commit()