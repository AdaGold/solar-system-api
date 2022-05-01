from app import db
'''
planet_data = [
    {"name":"Earth", "description": "blue planet", "moons": "1" },
    {"name":"Mercury", "description": "closest to sun and smallest", "moons": "0"},
    {"name":"Jupiter", "description": "largest in the solar system", "moons": "66"},
    {"name":"Venus", "description": "brightest object in Earth's night sky after the Moon", "moons": "0"}
    {"name":"Mars", "description": "Second smallest planet and also is called 'Red planet'", "moons": "2"}
]
'''

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    moons = db.Column(db.Integer)

    def to_json(self):
        return {
            "id": self.id,
            "name" : self.name,
            "decription": self.description,
            "moons": self.moons
        }

