from flask import Blueprint, abort, make_response
from app.models.planets import planets

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planet_bp.get("")
def get_all_planets():
    planets_response = []
    for planet in planets:
        planets_response.append(dict(
            id=planet.id,
            name=planet.name,
            description=planet.description    
            
        ))
    
    return planets_response

@planet_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_palnet(planet_id)

    return planet.to_dict(planet_id)


def validate_palnet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        response = {"message": f"planet {planet_id} invalid"}
        abort(make_response(response, 400))
    
    for planet in planets:
        if planet.id == planet_id:
            return planet
    
    response = {"message": f"planet {planet_id} not found"}
    abort(make_response(response, 404))