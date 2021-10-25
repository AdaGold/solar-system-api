from app import db 

class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    proximity = db.Column(db.String(250))
    description = db.Column(db.String(250))
