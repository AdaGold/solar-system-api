import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet

# instance of our app that is listening for our test db
@pytest.fixture
def app():
    app = create_app({"TESTING": True})
    # helps with the accuracy of tests 
    # clears out temperary data
    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

   # our database is clean,its empty of all data
    with app.app_context():
        # generate a new clean, start to db
        # an empty db that we can test on
        db.create_all()

        # tells fixture to return an instance of app context
        # sending it to test when test is called
        yield app
    
    # once test is complete clears out any data that it created
    # so we can work with clean database
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    # app that references another fixture
    # holds the reference to the test interface
    return app.test_client()

@pytest.fixture
def two_saved_planets(app):
    # Arrange
    ocean_planet = Planet(name="Ocean Planet",
                          description="Smells fishy",
                          color="Silver")
    minion_planet = Planet(name="Mark",
                          description="Miniony",
                          color="Yellow")
    db.session.add_all([ocean_planet, minion_planet])
    db.session.commit()