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
    # Arrange
    dolphini_planet = Planet(name="Dolphini", description="Exoplanet", distance= "100 billion miles")
    

    db.session.add(dolphini_planet)
    db.session.commit()

    return dolphini_planet