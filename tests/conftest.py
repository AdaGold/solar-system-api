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
    # Arrange
    test_planet = Planet(name="Planet number one",
                    description="watr 4evr",
                    color = "color")

    # test_planet = Planet(name="Test planet",
    #                     description="i luv 2 climb rocks",
    #                     color = "color")

    db.session.add(test_planet)
    # Alternatively, we could do
    # db.session.add(planet_number_one)
    # db.session.add(test_planet)
    db.session.commit()
    db.session.refresh(test_planet, ["id"])

    return test_planet

@pytest.fixture
def many_planets(app):
    # Arrange

    #     ocean_book = Book(title="Ocean Book",
    #                   description="watr 4evr")
    # mountain_book = Book(title="Mountain Book",
    #                      description="i luv 2 climb rocks")


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

    #db.session.add(several_test_planets)
    # Alternatively, we could do
    # db.session.add(planet_number_one)
    # db.session.add(test_planet)
    db.session.commit()
    
    #db.session.refresh(test_planet, ["id"])
    