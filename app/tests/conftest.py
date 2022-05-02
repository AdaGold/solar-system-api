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
def two_saved_planets(app):
    # Arrange
    jupiter = Planet(name="Jupiter",
                      description="has big spot",
                      moons=66)
    venus = Planet(name="Venus",
                         description="beauty",
                         moons=0)

    db.session.add_all([jupiter, venus])
    # Alternatively, we could do
    # db.session.add(jupiter)
    # db.session.add(venus)
    db.session.commit()