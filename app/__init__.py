from flask import Flask


def create_app():
    app = Flask(__name__)
    
    from .routes import planets_bp
    app.register_blueprint(planets_bp)
    
    return app

