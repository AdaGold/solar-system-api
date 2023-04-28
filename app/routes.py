from app import db
from flask import Blueprint, jsonify, abort, make_response, request
from app.models.planet import Planet




# class Planet:
#     def __init__(self, id, name, description, position_from_sun):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.position_from_sun = position_from_sun 

# planets = [
#         Planet(1, "mercury", "smallest in our solar system", 1),
#         Planet(2, "venus", "hottest planet in our solar system", 2),
#         Planet(3, "earth", "humans live here", 3),
#     ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
                            name=request_body["name"],
                            description=request_body["description"],
                            position_from_sun=request_body["position_from_sun"]
                        )
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)



# @planets_bp.route("", methods=["GET"])
# def get_planets():
#     planets_response = []
#     for planet in planets:
#         planets_response.append({
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description,
#             "position_from_sun": planet.position_from_sun
#         })
#     return jsonify(planets_response)

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message": f"planet {planet_id} is invalid"}, 400))
    
#     for planet in planets:
#         if planet.id == planet_id:
#             return planet
        
#     abort(make_response({"message": f"planet not found"}, 404))

# @planets_bp.route("/<planet_id>", methods=["GET"])
# def handle_planet(planet_id):
#     planet = validate_planet(planet_id)

#     return dict(
#         id=planet.id,
#         name=planet.name,
#         description=planet.description,
#         position_from_sun=planet.position_from_sun
#     )

