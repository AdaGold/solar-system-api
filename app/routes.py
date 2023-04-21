from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, position_from_sun):
        self.id = id
        self.name = name
        self.description = description
        self.position_from_sun = position_from_sun 

planets = [
        Planet(1, "mercury", "smallest in our solar system", 1),
        Planet(2, "venus", "hottest planet in our solar system", 2),
        Planet(3, "earth", "humans live here", 3)
    ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def get_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "position_from_sun": planet.position_from_sun
        })
    return jsonify(planets_response)

