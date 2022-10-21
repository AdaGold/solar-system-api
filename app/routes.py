
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

@planets_bp.route("",methods=["GET"])
def get_all_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description
        })
    return jsonify(planets_response)
    
        