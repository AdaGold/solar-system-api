from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    #need to register blueprint here for planets_bp
    return app
