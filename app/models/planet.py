from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    num_moons = db.Column(db.Integer)

def to_string(self):
        return f"{self.id}: {self.name} Description {self.description} Number of Moons {self.num_moons}"