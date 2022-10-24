
from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

planets = [
    Planet(1, "Mercury", "Mercury description"),
    Planet(2, "Pluto", "Pluto description"),
    Planet(3, "Venus", "Venus description")
    ]

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planets_response = [{"id": planet.id, "name": planet.name, "description": planet.description} for planet in planets]

    return jsonify(planets_response)

@planets_bp.route('<planet_id>',methods=["GET"])    
def get_one_planet(planet_id):
    planet_id = int(planet_id)
    for planet in planets:
        if planet.id == planet_id:
            return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description
            }
    