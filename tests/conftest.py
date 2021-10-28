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


@pytest.fixture #purpse to make code clean and logical
def two_saved_planets(app):
    # Arrange
    earth = Planet(name="Earth",
                    description="Round and big", 
                    color="Blue")
    mars = Planet(name="Mars",
                    description="It is on fire", 
                    color="Red")

    db.session.add_all([earth, mars])
    # Alternatively, we could do
    # db.session.add(ocean_book)
    # db.session.add(mountain_book)
    db.session.commit()