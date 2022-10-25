from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    from .routes import planets_bp
    app.register_blueprint(planets_bp)

    return app
    
# commands to remember: 
# flask run -h localhost -p 3000
# FLASK_ENV=development flask run