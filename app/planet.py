from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    planet_name = db.Column(db.String)
    description = db.Column(db.String)
    density = db.Column(db.Integer)