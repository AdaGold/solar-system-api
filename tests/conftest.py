import pytest
from app import create_app, db
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
def one_planet(app):
    test_planet = Planet(name="Planet number one",
                    description="watr 4evr",
                    color = "color")


    db.session.add(test_planet)
    db.session.commit()
    db.session.refresh(test_planet, ["id"])

    return test_planet

@pytest.fixture
def many_planets(app):
    apes_planet = Planet(name="Planet of apes",
                    description="Only apes live there",
                    color = "Grey")
    crocodile_planet = Planet(name="Planet crocodiles",
                    description="Only crocodiles live there",
                    color = "Green")
    butterfly_planet = Planet(name="Planet of butterflies",
                    description="Butterflies and unicorns live there",
                    color = "Rainbow")
    orange_planet = Planet(name="Planet of oranges",
                    description="It's full of oranges",
                    color = "Orange")
    
    db.session.add_all([apes_planet, crocodile_planet, butterfly_planet, orange_planet])

    db.session.commit()