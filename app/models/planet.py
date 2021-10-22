from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    distance_from_sun_in_million_mi = db.Column(db.Float)
    moon_count = db.Column(db.Integer)
