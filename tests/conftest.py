import pytest
from app import create_app
from app import db
from app.models.planet import Planet


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

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
    first_planet = Planet(name="First Planet", description="it's first", moons=7)
    second_planet = Planet(name="Second Planet", description="it's second", moons=11)

    db.session.add_all([first_planet, second_planet])
    db.session.commit()