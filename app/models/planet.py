from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    num_of_moons = db.Column(db.String)

    def get_dict(self):
        return {
                "id": self.id,
                "name": self.name,
                "description": self.description,
                "num_of_moons": self.num_of_moons
                }