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
    planet_one = Planet(name="Planet One", description="One", moon=True)
    planet_two = Planet(name="Planet Two", description="Two", moon=True)

    db.session.add_all([planet_one, planet_two])

    db.session.commit()