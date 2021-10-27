import pytest 
from app import create_app
from app import db 
from app.models.planet import Planet

@pytest.fixture 
def app():
    app = create_app({"TESTING":True})

    # creating a test db + yielding to tests 
    with app.app_context():
        db.create_all()
        yield app 

    # dropping the db when finished (clean up)
    with app.app_context():
        db.drop_all()
    
@pytest.fixture 
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_planets(app):
    venus_planet = Planet(name="Venus", description="Yellow planet", num_of_moons=0)
    dune_planet = Planet(name="Dune", description="Desert planet", num_of_moons=2)

    db.session.add_all([venus_planet, dune_planet])
    db.session.commit()


    
