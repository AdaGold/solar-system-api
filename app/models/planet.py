from app import db
from flask import make_response 

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    color = db.Column(db.String)
    moon_id = db.Column(db.Integer, db.ForeignKey('moon.moon_id'))
    moon = db.relationship("Moon", back_populates="planets")
    # __tablename__ = "planets"

    
    def update(self, planet_to_dict):
        for key, value in planet_to_dict.items():
            if key == "name":
                value = value.title()
            setattr(self,key,value)
        
    
    def planet_to_dict(self):
        return {
        "id": self.id,
        "name": self.name,
        "description": self.description,
        "color": self.color,
        "moon_id": self.moon_id }
    
    def __str__(self):
        return f'An object of type {self.__class__.__name__} with id {self.id}.'
    
    @classmethod 
    def create_new_planet(cls, request_data):
        if "name" not in request_data or "description" not in request_data:
            return make_response("Invalid Request. Missing required fields: name or description", 400)
        return cls(
            name=request_data["name"].title(),
            description=request_data["description"],
            color=request_data.get("color"),
            moon_id=request_data.get("moon_id") 
        )
    


    