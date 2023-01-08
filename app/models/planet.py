from app import db

class Planet(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.Text, nullable = False)
    is_rocky = db.Column(db.Boolean, nullable = False)
    moons = db.relationship("Moon", back_populates="planet")

    def to_dict(self):
        planet_dict =  {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "is_rocky" : self.is_rocky
        }
        planet_dict["moons"] = [moon.name for moon in self.moons]

        return planet_dict

    @classmethod
    def from_dict(cls, planet_data):
        planet = cls(
            name = planet_data["name"],
            description = planet_data["description"],
            is_rocky = planet_data["is_rocky"]
        )

        return planet