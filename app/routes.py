from os import abort
from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request


# planets = [
#     Planet(1, "Mercury", "the closest to the Sun", "orange"),
#     Planet(2, "Venus", "toxic atmosphere and yellowish clouds", "brown"),
#     Planet(3, "Earth", "ocean planet", "blue"),
#     Planet(4, "Mars", "small red, cold and dusty planet", "red"),
#     Planet(5, "Jupiter", "covered in cloudy stripes", "light blue with brown stripes"),
#     Planet(6, "Saturn", "has seven rings around its body", "beige"),
#     Planet(7, "Uranus", "made of water", "baby blue"),
#     Planet(8, "Neptune", "dark and very windy", "sky blue")
#     ]


planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
#def handle_planets():
def read_all_planets():
    #if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "color": planet.color
            })
        return jsonify(planets_response)
    
@planets_bp.route("", methods=["POST"])
def create_planet():
    #elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
                            description=request_body["description"],
                            color=request_body["color"])

        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"planet {new_planet.name} successfully created", 201)




# planets_bp = Blueprint("planets", __name__, url_prefix="/planets")
# @planets_bp.route("", methods=["Get"])
# def get_all_planets():
#     result = []
#     for planet in planets:
#         result.append({
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description,
#             "color": planet.color
#         })

#     return jsonify(result)

# @planets_bp.route("/<planet_id>", methods=["GET"])
# def get_one_planet(planet_id):
#     planet = validate_planet(planet_id)

#     return jsonify({
#         "id": planet.id,
#         "name": planet.name,
#         "description": planet.description,
#         "color": planet.color
#     }), 200  

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet

#     abort(make_response({"message":f"planet {planet_id} not found"}, 404))