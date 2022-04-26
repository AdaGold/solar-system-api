from flask import Blueprint, jsonify, abort, make_response
from .planet import Planet

planets = [
    Planet(1, "Earth", "blue planet", 1),
    Planet(2, "Mercury", "closest to sun", 0),
    Planet(3, "Jupiter", "has big spot", 66)
]
planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_json())

    return jsonify(planets_response)

def validate_planet(id):
    try:
        id = int(id)
    except:
        abort(make_response({"message":f"planet_id {id} invalid"}, 400))
    
    for planet in planets:
        if planet.id == id:
            return planet

    abort(make_response({"message":f"planet {id} not found"}, 404))

@planets_bp.route("/<id>", methods=["GET"])
def handle_planet(id):
    planet = validate_planet(id)
    return jsonify(planet.to_json())
