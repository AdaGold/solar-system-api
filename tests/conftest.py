import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet


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
                distance_from_earth=60.81)

    jupiter = Planet(name="Jupiter",
                    description="This is planet: Jupiter",
                    gravity=24.79,
                    distance_from_earth=467.64)

    db.session.add_all([mars, jupiter])
    db.session.commit()
    db.session.refresh(mars, ["id"])
    db.session.refresh(jupiter, ["id"])