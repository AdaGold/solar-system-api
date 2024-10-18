from flask import Blueprint
from app.models.planet import Planets

planets_bp = Blueprint("planets_bp", __name__, url_prefix=("/planets"))


@planets_bp.get("")
def get_all_planets():
    planet_list = []
    for planet in Planets:
        planet_list.append(
            {"id": planet.id, "name": planet.name, "description": planet.description}
        )
    return planet_list


@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        return {"message": f"{planet_id} is not a invalid id"}, 400
    for planet in Planets:
        if planet.id == planet_id:
            return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
            }
    return {"success": False, "msg": "Planet id not valid"}, 404
