from flask import Blueprint
from app.models.planets import planets

<<<<<<< HEAD

=======
>>>>>>> fe0c62ab7223aeadaa935a37f34bd348e8280491
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
        
<<<<<<< HEAD
    return planets_response






=======
    return planets_response


