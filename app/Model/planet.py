from app import db

class Planet(db.Model):
    __tablename__= 'planets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    description = db.Column(db.String)
    mythology = db.Column(db.String)

    def to_dict(self):
        return {"id": self.id,
        "name":self.name,
        "description": self.description,
        "mythology": self.mythology}