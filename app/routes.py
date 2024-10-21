from flask import Blueprint, abort, make_response
from .models import planets

planets_bp = Blueprint('planets', __name__)

@planets_bp.route('/planets', methods=['GET'])
def get_planets():
    planets_reponse = []
    for planet in planets:
        planets_reponse.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "color": planet.color,
            }
        )

    return planets_reponse

@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return {
        "id": planet.id,
        "name": planet.title,
        "description": planet.description,
        "color": planet.color
    }

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        response = {"message": f"planet {planet_id} invalid"}
        abort(make_response(response , 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

    response = {"message": f"planet {planet_id} not found"}
    abort(make_response(response, 404))