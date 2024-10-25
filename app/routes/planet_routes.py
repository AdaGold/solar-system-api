from flask import Blueprint, abort, make_response
from ..models.planet import Planet

planets_bp = Blueprint('planets_bp', __name__, url_prefix='/planets')

# @planets_bp.get('')
# def get_all_planets():
#     return [planet.to_dict() for planet in planets]

# @planets_bp.get('/<planet_id>')
# def get_one_planet(planet_id):
#     planet = validate_planet(planet_id)

#     return planet.to_dict()

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except ValueError:
#         abort(make_response({"message": f"planet {planet_id} invalid"}, 400))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet
        
#     abort(make_response({"message": f"planet {planet_id} not found"}, 404))