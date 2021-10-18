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
