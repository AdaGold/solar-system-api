import pytest
from app import create_app
from app import db
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({'TESTING': True})

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
    saturn_planet = Planet(name="Saturn",
    description="The sixth planet from our sun.",
    radius_size= "36,184 mi")

    jupiter_planet = Planet(name="Jupiter",
    description="The gas giant.",
    radius_size="43,441 mi")

    db.session.add_all([saturn_planet, jupiter_planet])
    db.session.commit()