from flask import Blueprint
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
