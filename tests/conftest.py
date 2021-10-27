# pytest file that holds test configurations & common test helper functions
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


# client fixture will make a test client (object able to simulate a client making HTTP requests)
@pytest.fixture
def client(app):
	return app.test_client()


@pytest.fixture
def one_saved_planet(app):
    planet_1 = Planet(name="Red Planet", description="The best planet in the universe!", color="Red")

    db.session.add(planet_1)
    db.session.commit()

@pytest.fixture
def all_saved_planets(app):
    planet_1 = Planet(name="Red Planet", description="The best planet in the universe!", color="Red")
    planet_2 = Planet(name="Ada Planet", description="An invisible rock in our solar system", color="Let your imagination run wild with this one.")

    db.session.add_all([planet_1, planet_2])
    db.session.commit()

