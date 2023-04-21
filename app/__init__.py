from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    from .routes import bp
    app.register_blueprint(bp)
    
    return app
