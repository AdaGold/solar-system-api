import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet


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


@pytest.fixture
def two_saved_planets(app):
    earth = Planet(
        description="Earth is the third planet from the Sun and the only place in the universe known to harbor life.",
        distance_from_earth=0,
        name="Earth",
        size=5
    )
    saturn = Planet(
        description="Saturn is the sixth planet from the Sun and the second-largest in the Solar System, after Jupiter. It is a gas giant with an average radius of about nine and a half times that of Earth.",
        distance_from_earth=982,
        name="Saturn",
        size=2
    )
    db.session.add_all([earth, saturn])
    db.session.commit()