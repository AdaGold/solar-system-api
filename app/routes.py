from flask import Blueprint, jsonify, abort, make_response, request
from app.models.planet import Planet
from app import db

# planets = [
#         Planet(1, "Mercury", "The smallest and fastest planet", False),
#         Planet(2, "Venus", "The hottest planet", False),
#         Planet(3, "Earth", "The blue marble", False),
#         Planet(4, "Mars", "The red planet", False),
#         Planet(5, "Jupiter", "The gas giant", False),
#         Planet(6, "Saturn", "The second largest planet", True),
#         Planet(7, "Uranus", "This planet spins on its side", True),
#         Planet(8, "Neptune", "The most distant planet from the sun", False)
#         ]

bp = Blueprint("planets", __name__, url_prefix="/planets")

# @bp.route("", methods=["GET"])
# def handle_planets():
#     return_body = []
#     for planet in planets:
#         return_body.append({
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description,
#             "rings": planet.rings
#         })
    
#     return jsonify(return_body)

# @bp.route("/<id>", methods=["GET"])
# def handle_planet(id):
#     try:
#         planet_id = int(id)
#     except:
#         abort(make_response({"message":f"planet {id} is not valid"}, 400))
    
#     for planet in planets:
#         if planet.id == planet_id:
#             return jsonify({
#                 "id": planet.id,
#                 "name": planet.name,
#                 "description": planet.description,
#                 "rings": planet.rings
#             })
    
#     abort(make_response({"message":f"Planet {id} not found."}, 404))

@bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        rings=request_body["rings"])
    
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} created", 201)

