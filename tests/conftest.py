import pytest
from app import create_app, db
from flask.signals import request_finished
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app(test_config=True)

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
    Mercury_planet = Planet(
        name="Mercury",
        description="Mercury is the smallest planet of our solar system.",
        is_rocky=True
    )

    Venus_planet = Planet(
        name="Venus",
        description="Venus is the hottest planet in the solar system.",
        is_rocky=True
    )
    db.session.add_all([Mercury_planet, Venus_planet])
    db.session.commit()
    db.session.refresh(Mercury_planet, ["id"])
    db.session.refresh(Venus_planet, ["id"])

@pytest.fixture
def one_saved_planet(app):
    Mercury_planet = Planet(
        name="Mercury",
        description="Mercury is the smallest planet of our solar system.",
        is_rocky=True
    )
    db.session.add(Mercury_planet)
    db.session.commit()
    db.session.refresh(Mercury_planet, ["id"])