from flask import Blueprint
from flask import Blueprint, jsonify 


class Planet:
    def __init__(self, id, name, description, color = None):
        self.id = id
        self.name = name
        self.description = description
        self.color = color


planets = [
    Planet(1, "Mercury", "Smallest planet in our solar system.", "light grey"),
    Planet(2, "Mars", " A planet with a very thin atmosphere made of carbon dioxide, nitrogen, and argon.",["red", "brown", "tan"]),
    Planet(3, "Venus", "The brighest object in the sky second to the Sun and Moon.", ["brown", "grey"]),
    Planet(4, "Earth", "What we live on!", ["blue", "brown-green", "white"]),
    Planet(5, "Jupiter", "The largest planet in our solar system", ["white", "red", "brown", "yellow"]),
    Planet(6, "Saturn", "Is comprised of thousands of ringlets made of chunks of ice and rock", ["yellow", "brown", "red", "white"]),
    Planet(7, "Uranus", "Rotates at nearly a 90 degree angle from the plane of its orbit", ["blue", "green"]),
    Planet(8, "Neptune", "First planet located through mathematical calulations", ["white", "red", "blue", "yellow"])
]


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# client can request all planets listed in "list(planets)"
@planets_bp.route("", methods=["GET"])
def find_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "color": planet.color
        })
    return jsonify(planets_response)


# client can request a specific planet listed in "list(planets)"
@planets_bp.route("/<planet_id>", methods=["GET"])
def find_one_planet(planet_id):
    planet_id = int(planet_id)
    for planet in planets:
        if planet_id == planet.id:
            return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "color": planet.color
            }