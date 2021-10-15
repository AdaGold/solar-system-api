from flask import Flask

# #test_config param needed?
# def create_app(test_config=None):
def create_app():
    app = Flask(__name__)

    from .routes import planets_bp
    app.register_blueprint(planets_bp)
    return app
