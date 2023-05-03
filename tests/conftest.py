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
    earth_planet = Planet(
        name="Earth",
        description="humans live here",
        position_from_sun=3
    )

    mercury_planet = Planet(
        name="Mercury",
        description="fastest planet",
        position_from_sun=1
    )

    db.session.add_all([earth_planet, mercury_planet])
    db.session.commit()

