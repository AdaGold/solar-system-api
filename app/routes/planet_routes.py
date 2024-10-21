from flask import Blueprint, abort, make_response
from app.models.planet import Planets

planets_bp = Blueprint("planets_bp", __name__, url_prefix=("/planets"))


@planets_bp.get("")
def get_all_planets():
    planet_list = []
    for planet in Planets:
        planet_list.append(planet.to_dict())
    return planet_list


@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    
    return planet.to_dict(), 200

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"{planet_id} is not a invalid id"}, 400))
    
    for planet in Planets:
        if planet.id == planet_id:
            return planet
    abort(make_response({"msg": "Planet id not found"}, 404))
        

