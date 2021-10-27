import pytest
from app import create_app
from app import db
from app.model.planet import Planet 


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
    planet_earth = Planet(name="Earth",
                      description="The blue planet")
    planet_venus = Planet(name="Venus",
                         description="The yellow planet.")

    db.session.add_all([planet_earth, planet_venus])
    db.session.commit()