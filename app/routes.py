from flask import Blueprint, jsonify


class Planets: 
    def __init__(self, id, name, description, gravity): 
        self.id = id
        self.name = name 
        self.description = description 
        self.gravity = gravity 
    
planets = [
    Planets(1, "Mercury", "The smallest planet in our solar system and nearest to the Sun.", "3.7 m/s^2"),
    Planets(2, "Earth", "The third planet from the Sun", "9.807 m/s^2"),
    Planets(3, "Jupiter", "The largest planet in the solar system", "24.79 m/s^2")
]

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods = ["GET"])
def planets_json():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "gravity":planet.gravity
        })
    return jsonify(planets_response)
