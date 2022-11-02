from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planet_bp = Blueprint("planet_bp", __name__, url_prefix = "/planets")

#create a planet 

@planet_bp.route("", methods=["POST"])
def handle_planets():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                description=request_body["description"],
                )

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet} successfully created", 201)


#read  planets
@planet_bp.route("", methods = ["GET"])
def all_planet_data():
    if request.method == "GET":
        planets = Planet.query.all()

        planet_data = []
        for planet in planets:
            planet_data.append({
                "id": planet.id, 
                "name": planet.name,
                "description": planet.description
            })
        return jsonify(planet_data)


# class Planet:
#     def __init__(self, id, name, description, size):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.size = size


# planets = [
#     Planet(1, "Mars", "Red", 2106), 
#     Planet(2, "Earth", "Blue", 3958),
#     Planet(3, "Mercury", "Grey", 1500)
# ]


# #this is the decorator that saying when a request matches turn this function into url
# @planet_bp.route("", methods = ["GET"])
# #need to create function here 

# def all_planets():
#     planet_data = []
#     for planet in planets:
#         planet_data.append({
#             "id": planet.id, "name": planet.name, "description": planet.description, "size": planet.size

#         })
#     return jsonify(planet_data)

# # this is the decorator for the planet_id endpoint
# @planet_bp.route("/<planet_id>", methods = ["GET"])

# def planet_info(planet_id):
#     try: 
#         planet_id = int(planet_id)
#     except:
#         return {"message": f'planet {planet_id} is invalid'}, 400

#     for planet in planets:
#         if planet.id == planet_id:
#             return {
#                 "id": planet.id, 
#                 "name": planet.name, 
#                 "description": planet.description, 
#                 "size": planet.size
#             }
#     return {"message": f"planet {planet_id} is not found"}, 404