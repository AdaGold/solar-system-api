# configuration file is to set up all tset case I need to run

import pytest
from app import create_app
from app import db

from app.models.planet import Planet
# ...
    
@pytest.fixture
def app():
    app = create_app({"TESTING": True})
    # At the start of each test, db.create_all() will rebuild the entire test database, creating all the tables needed for our models. Crucially, these tables begin empty!
    with app.app_context():
        # set up all data in my database
        db.create_all()
        yield app

    # Then at the end of each test, db.drop_all() deletes all the tables from the database. This prevents any test data created during one test from contaminating later tests.
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def two_saved_planets(app):
    # Arrange
    mars = Planet(name="Mars",
                    description="red_planet ",
                    distance_from_sun_in_million_mi=1000,
                        moon_count=1
                    )
    earth = Planet(name="Earth",
                        description="where human being lives",
                        distance_from_sun_in_million_mi=90,
                        moon_count=1
                        
                        )

    db.session.add_all([mars, earth])
    # Alternatively, we could do
    # db.session.add(ocean_book)
    # db.session.add(mountain_book)
    db.session.commit()

