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
    planet_number_one = Planet(name="Planet number one",
                    description="watr 4evr",
                    color = "color")
    test_planet = Planet(name="Test planet",
                        description="i luv 2 climb rocks",
                        color = "color")

    db.session.add_all([planet_number_one, test_planet])
    # Alternatively, we could do
    # db.session.add(planet_number_one)
    # db.session.add(test_planet)
    db.session.commit()