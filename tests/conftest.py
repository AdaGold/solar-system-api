import pytest 
from app import create_app
from app import db 

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


    
