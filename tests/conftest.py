import pytest
from app import create_app
from app import db
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_contect():
        db.create_all()
        yield app
    
    with app.app_contect():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()
