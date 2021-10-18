from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color 
        
planets = [
    Planet(1, "mercury", "the littlest planet", "gray"),
    Planet(2, "venus", "the hottest planet", "maroon"),
    Planet(3, "earth", "the liveliest planet", "green"),
    Planet(4, "mars", "the reddest planet", "red" ),
    Planet(5, "jupiter", "the biggest planet", "orange"),
    Planet(6, "saturn", "the ring planet", "yellow"),
    Planet(7, "uranus", "the most sidways planet", "purple"),
    Planet(8, "neptune", "the boring planet", "blue"),
]

planets_bp = Blueprint("planets", __name__)
one_planet_bp = Blueprint("one_planet", __name__, url_prefix="/planet")

@planets_bp.route("/planets", methods=["GET"])
def all_planets():
    planets_return = []
    for planet in planets:
        planet_dict = {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "color": planet.color
        }
        planets_return.append(planet_dict)
    return jsonify(planets_return)

#one_planet_bp = Blueprint("one_planet", __name__, url_prefix="/planet")
# http://127.0.0.1:5000/planet/<planet_id>
@one_planet_bp.route("/<planet_id>", methods=["GET"])
def one_planet(planet_id):
    planet_id = int(planet_id)
    for planet in planets:
        if planet.id == planet_id:
            return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "color": planet.color
            }