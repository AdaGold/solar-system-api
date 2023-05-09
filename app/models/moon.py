from app import db
from flask import make_response 

class Moon(db.Model):
    moon_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    planets = db.relationship("Planet", back_populates="moon")

    def moon_to_dict(self):
        return {
        "moon_id": self.moon_id,
        "name": self.name
        }
    def __str__(self):
        return f'An object of type {self.__class__.__name__} with id {self.moon_id}.'

    @classmethod 
    def create_new_planet(cls, request_data):
        if "name" not in request_data or request_data is None:
            return make_response("Invalid Request. Missing required fields: name or request data", 400)
        return cls(
            name=request_data["name"].title()
        )

    def update(self, moon_to_dict):
        for key, value in moon_to_dict.items():
            if key == "name":
                value = value.title()
            setattr(self,key,value)