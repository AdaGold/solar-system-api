import json
from unicodedata import name
from flask import Blueprint, jsonify, abort, make_response


class Planet:
    def __init__(self, id, name, description, dist_from_sun):
        self.id = id
        self.name = name
        self.description = description
        self.dist_from_sun = dist_from_sun

planets = [
    Planet(1, "Mercury", "rocky", 1),
    Planet(2, "Venus", "rocky", 2),
    Planet(3, "Earth", "water", 3),
    Planet(4, "Mars", "red", 4),
    Planet(5, "Jupiter", "big", 5),
    Planet(6, "Saturn", "rings", 6),
    Planet(7, "Uranus", "butt", 7),
    Planet(8, "Neptune", "ice", 8),
    Planet(9, "Pluto", "dwarf", 9)
]

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods = ["GET"])
def planet_data():
    planet_list = []
    for planet in planets:
        planet_list.append({
        "id" : planet.id,
        "name" : planet.name,
        "description" : planet.description,
        "distance from sun" : planet.dist_from_sun
        }
        )
    return jsonify(planet_list)

# @planets_bp.route("<")
# def 

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"planet {planet_id} is invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

    abort(make_response({"message": f"planet {planet_id} not found"}, 404))

