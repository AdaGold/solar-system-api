import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet

#instance of our app that is listening for our test databse
@pytest.fixture
def app():
    app = create_app({"TESTING":True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

   #our database is clean,its empty of all data
    with app.app_context():
        db.create_all()
        yield app
    
    # once test is complete clears out any data that it created
    #so we can work with clean database
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    #app that references another fixture
    # holds the reference to the test interface
    return app.test_client()


