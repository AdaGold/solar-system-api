from app import db


class Planet(db.Model):
    
    id = db.Column(db.Integer,primary_key = True, autoincrement = True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    gravity = db.Column(db.Float)
    distance_from_earth = db.Column(db.Float)
    moons = db.relationship("Moon", back_populates = "planet")

    def to_dict(self):
        planet_as_dict = {}
        planet_as_dict["id"] = self.id
        planet_as_dict["name"] = self.name
        planet_as_dict["description"] = self.description
        planet_as_dict["gravity"] = self.gravity
        planet_as_dict["distance_from_earth"] = self.distance_from_earth  

        moon_names = []
        for moon in self.moons:
            moon_names.append(moon.name)
        planet_as_dict["moons"] = [moon.name for moon in self.moons]

        return planet_as_dict

    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(
            name=planet_data["name"],
            description=planet_data["description"],
            gravity = planet_data['gravity'],
            distance_from_earth = planet_data['distance_from_earth']
        )
        
        return new_planet