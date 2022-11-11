from app import db
from flask import abort, make_response, jsonify

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    moons = db.Column(db.Integer)


    @classmethod
    def from_dict(cls, data_dict):
        return cls(name=data_dict["name"], description=data_dict["description"], moons=data_dict["moons"])

    def to_dict(self):
        planet_dict = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "moons": self.moons
        }

        return planet_dict
    
    def update(self,req_body):
        try:
            self.name = req_body["name"]
            self.description = req_body["description"]
            self.moons = req_body["moons"]
        except KeyError:
            abort(make_response(jsonify(dict(details="Invalid data")), 400))

 