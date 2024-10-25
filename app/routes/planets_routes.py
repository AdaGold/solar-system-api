from flask import Blueprint, abort, make_response
# from app.models.planets import planets

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

# @planet_bp.get("")
# def get_all_planets():
#     planets_response = [planet.to_dict() for planet in planets ]
#     return planets_response

# @planet_bp.get("/<planet_id>")
# def get_one_planet(planet_id):
#     planet = validate_planet(planet_id)

#     return planet.to_dict()


# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         response = {"message": f"planet {planet_id} invalid"}
#         abort(make_response(response, 400))
    
#     for planet in planets:
#         if planet.id == planet_id:
#             return planet
    
#     response = {"message": f"planet {planet_id} not found"}
#     abort(make_response(response, 404))