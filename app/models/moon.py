from app import db


class Moon(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    radius = db.Column(db.Integer, nullable=False)
    
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    planet = db.relationship("Planet", back_populates="moons")

    def to_dict(self):
        moon_as_dict = {}
        moon_as_dict["id"] = self.id
        moon_as_dict["name"] = self.name
        moon_as_dict["description"] = self.description
        moon_as_dict["radius"] = self.radius
        return moon_as_dict
    
    @classmethod
    def from_dict(cls, moon_data):
        new_moon = Moon(
            name=moon_data["name"],
            description=moon_data["description"],
            radius=moon_data["radius"]
        )
        return new_moon