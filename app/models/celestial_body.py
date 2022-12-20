from app import db
class CelestialBody(db.Model):
    __tablename__ = 'celestial_bodies'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String)
    description = db.Column(db.String)
    image=db.Column(db.String)
