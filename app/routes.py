from app import db
from app.models.planet import Planet
# from unicodedata import name
from flask import Blueprint, jsonify, abort, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():
        if request.method == "GET":
            planets = Planet.query.all()
            planets_response = []
            for planet in planets:
                planets_response.append({
                    "id": planet.id,
                    "title": planet.title,
                    "description": planet.description,
                    "size": planet.description
                })
            return jsonify(planets_response)
        elif request.method == "POST":
            request_body = request.get_json()
            print (request_body)
            new_planet = Planet(title=request_body["title"],
                            description=request_body["description"],
                            size=request_body["size"])

            db.session.add(new_planet)
            db.session.commit()

            return make_response(f"Planet {new_planet.title} successfully created", 201)

# class Planet:
#     def __init__(self, id, name, description, size):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.size = size

# planets = [
#     Planet(1, "Earth", "inhabits life", "7,917.5 mi"),
#     Planet(2, "Mars", "cold dusty desert", "4,212.3 mi"),
#     Planet(3, "Saturn", "Adorned with ringlets", "72,367 mi")
# ]

# planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# @planets_bp.route("",methods=["GET"])
# def handle_planets_data():
#     planets_response = []
#     for planet in planets:
#         planets_response.append({
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description,
#             "size": planet.size
#         }), 200
#     return jsonify(planets_response)

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message": f"Planet {planet_id} invalid"}, 400))
        
#     for planet in planets:
#         if planet.id == planet_id:
#             return planet

#     abort(make_response({"message":f"planet {planet_id} not found"}, 404))

# @planets_bp.route("/<planet_id>", methods=["GET"])
# def handle_planet(planet_id):
#     planet = validate_planet(planet_id)

#     return jsonify({
#         "id": planet.id,
#         "name": planet.name,
#         "description": planet.description,
#         "size": planet.size
#     }), 200