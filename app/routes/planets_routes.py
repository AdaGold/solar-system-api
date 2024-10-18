from flask import Blueprint
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



