from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, cycle_len):
        self.id=id
        self.name=name
        self.description=description
        self.cycle_len=cycle_len # days

planets = [
    Planet(1, "Earth", "blue marble", 365),
    Planet(2, "Saturn", "ringed planet", 10220),
    Planet(3, "Mars", "musty, dusty and cold", 780),
    Planet(4, "Mercury", "teeny tiny", 88)
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "cycle length (days)": planet.cycle_len
        })
    return jsonify(planets_response)
