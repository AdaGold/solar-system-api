from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    position_from_sun = db.Column(db.Integer)

