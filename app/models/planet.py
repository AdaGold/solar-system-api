from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    num_moons = db.Column(db.Integer)

    def to_string(self):
        return f"{self.id}: {self.name} Description {self.description} Number of Moons {self.num_moons}"

    def to_dict(self):
        return {
                "id": self.id,
                "name": self.name,
                "description": self.description,
                "num_moons": self.num_moons
                }

    @classmethod
    def from_dict(cls, planet_data):
        return cls(
            name = planet_data["name"],
            description = planet_data["description"],
            num_moons = planet_data["num_moons"]
        )
    