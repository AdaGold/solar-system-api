from app import db 


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    planet_type = db.Column(db.String)
    description=  db.Column(db.String) 
    moons = db.Column(db.String)
