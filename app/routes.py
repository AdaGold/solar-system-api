from flask import Blueprint, jsonify, abort, make_response
from .moon import moons_list
from .planets import Planet, solar_system
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")
moons_bp = Blueprint("moons", __name__, url_prefix="/moons")

@planets_bp.route("", methods=["GET"])
def display_planets():
    planets_response = []
    for planet in solar_system:
        planets_response.append({
            "id": planet.id,
            "name": planet.name, 
            "description": planet.description,
            "Has Rings": planet.has_rings,
            "Moons" : [moon.name for moon in planet.moons]
        })
    return jsonify(planets_response)

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"{planet_id} invalid"}, 400))
    
    for planet in solar_system:
        if planet.id == planet_id:
            return planet
    abort(make_response({"message":f"Planet with {planet_id} not found"}, 404))

@planets_bp.route("/<planet_id>", methods=["GET"])
def display_planet(planet_id):
    planet = validate_planet(planet_id)
    return {
        "id": planet.id,
        "name": planet.name, 
        "description": planet.description,
        "Has Rings": planet.has_rings,
        "Moons" : [moon.name for moon in planet.moons]
    }


@moons_bp.route("", methods=["GET"])
def get_all_moons():
    moons_response = []
    for moon in moons_list:
        moons_response.append({
            "id":moon.id,
            "name": moon.name,
            "description": moon.description
        })
    return jsonify(moons_response)

def validate_moon(moon_id):
    try:
        moon_id=int(moon_id)
    except:
        abort(make_response({"message":f"moon {moon_id} invalid"}))
    
    for moon in moons_list:
        if moon.id==moon_id:
            return moon
    
    abort(make_response({"message": f"moon {moon_id} not found"}))

@moons_bp.route("/<moon_id>", methods=["GET"])
def get_moon_by_id(moon_id):
    moon=validate_moon(moon_id)
    
    return {
        "id": moon.id,
        "name": moon.name,
        "description": moon.description
    }