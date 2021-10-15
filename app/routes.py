from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons

planets =  [
    Planet(1, "Mercury", "Mercury is hot, but not too hot for ice", 0),
    Planet(2, "Mercury", "Venus doesn’t have any moons, and we aren’t sure why", 0),
    Planet(3, "Earth", "Best planet ever!", 1),
    Planet(4, "Mars", "Mars has two moons named in Latin that translate to fear and panic", 2),
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def all_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id" : planet.id,
            "name" : planet.name,
            "description" : planet.description,
            "moons" : planet.moons
        })
    return jsonify(planets_response)
