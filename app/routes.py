from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

planets = [
    Planet(1, "Earth", "Solid"),
    Planet(2, "Mars", "Solid"),
    Planet(3, "Saturn", "Gas")
]

planet_bp = Blueprint("planet_blue_print", __name__, url_prefix="/planets")
@planet_bp.route("", methods=["GET"])
def get_planet():
    all_planets = []
    for planet in planets:
        planet_dic = {"id" : planet.id,
                      "name" : planet.name,
                      "description" : planet.description}
        all_planets.append(planet_dic)
    return jsonify(all_planets)
