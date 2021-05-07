from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv


db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")

    # Import models here for Alembic setup
    from app.models.customer import Customer
    from app.models.video import Video
    from app.models.rental import Rental

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import index_bp
    app.register_blueprint(index_bp)

    from .routes import customer_bp
    app.register_blueprint(customer_bp)

    from .routes import video_bp
    app.register_blueprint(video_bp)

    from .routes import rental_bp
    app.register_blueprint(rental_bp)

    # Register Blueprints here

    @app.errorhandler(500)
    def server_error(error):
        print(error)
        return make_response({"error":"The server has encountered an error."}, 500)

    @app.errorhandler(405)
    def method_error(error):
        print(error)
        return make_response({"error":"The method is not allowed for the requested URL"}, 405)

    @app.errorhandler(404)
    def not_found_error(error):
        print(error)
        return make_response({"error":"The requested URL was not found on the server"}, 404)


    return app
