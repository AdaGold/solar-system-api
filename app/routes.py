from flask import Blueprint, jsonify
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



@planets_bp.route("/<planet_id>", methods=["GET"])
def display_planet(planet_id):
    pass

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



    


    

    

