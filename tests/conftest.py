import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app import Planet


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

    from app.models.book import Book
# ...

@pytest.fixture
def two_saved_planets(app):
    # Arrange
    mercury = Planet(name= "Mercury",
                    description="pretty",
                    color= "purple")
    saturn = Planet(name="Saturn",
                    description="has rings",
                    color= "brown")

    db.session.add_all([mercury, saturn])
    # Alternatively, we could do
    # db.session.add(ocean_book)
    # db.session.add(mountain_book)
    db.session.commit()