import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet
from app.models.moon import Moon


@pytest.fixture
def app():
    app = create_app({"TEST": True})

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
def saved_two_planets(app):
    mars = Planet(name="Mars",
                description="This is planet: Mars",
                gravity=3.721,
                distance_from_earth=60.81,
                moons = []
                )

    jupiter = Planet(name="Jupiter",
                    description="This is planet: Jupiter",
                    gravity=24.79,
                    distance_from_earth=467.64,
                    moons = [],
                    )

    db.session.add_all([mars, jupiter])
    db.session.commit()
    db.session.refresh(mars, ["id"])
    db.session.refresh(jupiter, ["id"])

@pytest.fixture
def saved_three_planets_with_duplicate_planet_name(app):
    mars = Planet(name="Mars",
                description="This is planet: Mars",
                gravity=3.721,
                distance_from_earth=60.81,
                moons = []
                )

    mars2 = Planet(name="Mars",
                description="This is planet: Mars2",
                gravity=4.721,
                distance_from_earth=60.81,
                moons = []
                )

    jupiter = Planet(name="Jupiter",
                    description="This is planet: Jupiter",
                    gravity=24.79,
                    distance_from_earth=467.64,
                    moons = [],
                    )

    db.session.add_all([mars, mars2, jupiter])
    db.session.commit()
    db.session.refresh(mars, ["id"])
    db.session.refresh(mars2, ["id"])
    db.session.refresh(jupiter, ["id"])


@pytest.fixture
def saved_two_moons(app):
    moon1 = Moon(name="Moon1")

    moon2 = Moon(name="Moon2")


    db.session.add_all([moon1, moon2])
    db.session.commit()
    db.session.refresh(moon1, ["id"])
    db.session.refresh(moon2, ["id"])

