from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False # Don't sort keys alphabetically 


    from .routes import planets_bp 
    app.register_blueprint(planets_bp) 

    return app
