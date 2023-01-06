from app import db

class Moon(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable = False)
    size = db.Column(db.Integer, nullable = False)
    description = db.Column(db.Text, nullable = False)
    gravity = db.Column(db.Float, nullable = False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    planet = db.relationship("Planet", back_populates="moons")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "size": self.size,
            "description": self.description,
            "gravity" : self.gravity
        }

    @classmethod
    def from_dict(cls, moon_data):
        moon = cls(
            name = moon_data["name"],
            size = moon_data["size"],
            description = moon_data["description"],
            gravity = moon_data["gravity"]
        )

        return moon
