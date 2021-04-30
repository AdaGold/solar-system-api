from flask import Flask

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    db.init_app(app)
    migrate.init_app(app,db)

    from app.models.planet import Planet

    from .routes import planet_bp
    app.register_blueprint(planet_bp)

    return app


# def create_app(test_config=None):
#     app = Flask(__name__)
#     #DB configs
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'

#     #import models here
#     from app.models.book import Book
    
#     db.init_app(app)
#     migrate.init_app(app,db)
    
#     #registers blueprints here
#     from .routes import hello_world_bp
#     app.register_blueprint(hello_world_bp)
    
#     return app