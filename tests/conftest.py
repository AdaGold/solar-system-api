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
    baby_planet = Planet(name="Baby",
    description="very smol")
    scary_planet = Planet(name="Scary",
    description="very scary")
    
    db.session.add_all([baby_planet, scary_planet])
    #alternative: db.session.add(baby_planet)
    #alternative: db.session.add(scary_planet)

    db.session.commit()
    # db.session.refresh()
    return [baby_planet, scary_planet]

@pytest.fixture
def one_saved_planet(app):
    posh_planet = Planet(name="Posh", 
    description='very posh')

    db.session.add(posh_planet)
    db.sesson.commit()
    db.session.refersh(posh_planet, ["id"])
    return posh_planet