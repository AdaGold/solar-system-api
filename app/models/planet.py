from app import db

class Planet(db.Model):
    __tablename__= 'planets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    elements = db.Column(db.String)



