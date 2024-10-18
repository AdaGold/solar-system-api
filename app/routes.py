from flask import Blueprint
from .planets import planets

planets_bp = Blueprint('planets_bp', __name__, url_prefix='/planets')

@planets_bp.get('')
def get_all_planets():
    planets_list = []
    for planet in planets:
        planets_list.append(
            {
                'id': planet.id,
                'title': planet.name,
                'description': planet.description,
                'moons': planet.moons
            }
        )
    return planets_list