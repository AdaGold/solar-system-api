import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet


@pytest.fixture
def app():
    app = create_app({"TESTING" : True})

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
    # arrange
    neptune = Planet(id=1, name="Neptune", description="ice", distance_from_sun=9)
    earth = Planet(id=2, name="Earth", description="water", distance_from_sun=3)

    db.session.add_all([neptune, earth])
    db.session.commit()