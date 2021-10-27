import pytest
from app import create_app
from app import db


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

from app.Models.planets import Planet
@pytest.fixture
def two_saved_planets(app):
    # Arrange
    earth = Planet(name="Earth",
                      description="home",
                      number_of_moons=0)
    mars = Planet(title="Mars",
                         description="red",
                         number_of_moons=0)

    db.session.add_all([earth, mars])
    db.session.commit()