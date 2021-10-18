from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, elements):
        self.id = id
        self.name = name
        self.description = description
        self.elements = elements

planets = [
    Planet(1, "Mercury", "First planet from the sun.", "elements"),
    Planet(2, "Venus", "Second planet from the sun.", "elements"),
    Planet(3, "Earth", "Third planet from the sun.", "elements"),
    Planet(4, "Mars", "Fourth planet from the sun.", "elements"),
    Planet(5, "Jupiter", "Fifth planet from the sun.", "elements"),
    Planet(6, "Saturn", "Sixth planet from the sun.", "elements"),
    Planet(7, "Uranus", "Seventh planet from the sun.", "elements"),
    Planet(8, "Neptune", "Eighth planet from the sun.", "elements"),
    Planet(9, "Pluto", "Still a planet!", "elements")
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods = ["GET"])
def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append(
            {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "elements": planet.elements
        }
            )
    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods = ["GET"])
def handle_planet(planet_id):
    planet_id = int(planet_id)
    for planet in planets:
        if planet.id == planet_id:
            return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "elements": planet.elements}


