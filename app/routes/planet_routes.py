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
