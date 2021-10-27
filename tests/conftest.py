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
    neptune = Planet(
        name = "Mars",
        description = "musty and cold",
        cycle_len = 780)
    mars = Planet(
        name = "Neptune",
        description = "its a planet",
        cycle_len = 1080
    )

    db.session.add_all([neptune, mars])

    db.session.commit()