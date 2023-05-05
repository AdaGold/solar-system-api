from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    number_of_moons = db.Column(db.Integer)


    def to_dict(planet):
        return {
                    "id": planet.id,
                    "name": planet.name,
                    "description": planet.description,
                    "number_of_moons": planet.number_of_moons
                }
    @classmethod
    def from_dict(cls, data_dict): 
        return cls(
            name = data_dict["name"],
            description = data_dict["description"],
            number_of_moons = data_dict["number_of_moons"]
        )