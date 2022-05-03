import json # maybe don't need 
from unicodedata import name # maybe don't need
from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet


# class Planet:
#     # def __init__(self, id, name, description, dist_from_sun):
#     #     self.id = id
#     #     self.name = name
#     #     self.description = description
#     #     self.dist_from_sun = dist_from_sun

#     def to_dict(self):
#         return {
#             "id" : self.id,
#             "name" : self.name,
#             "description" : self.description,
#             "distance from sun" : self.dist_from_sun
#         }

# planets = [
#     Planet(1, "Mercury", "rocky", 1),
#     Planet(2, "Venus", "rocky", 2),
#     Planet(3, "Earth", "water", 3),
#     Planet(4, "Mars", "red", 4),
#     Planet(5, "Jupiter", "big", 5),
#     Planet(6, "Saturn", "rings", 6),
#     Planet(7, "Uranus", "butt", 7),
#     Planet(8, "Neptune", "ice", 8),
#     Planet(9, "Pluto", "dwarf", 9)
# ]

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods = ["POST"])
def handle_planets():
    request_body = request.get_json()
    new_planet = Planet(
        name = request_body["name"], 
        description = request_body["description"], 
        distance_from_sun = request_body["distance from sun"]
        )

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f'planet {new_planet.name} successfully created!', 201)

@planets_bp.route("", methods = ["GET"])
def planet_data():
    planets = Planet.query.all()
    planets_response = []

    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "distance from sun": planet.distance_from_sun
        })
    
    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods = ["GET"])
def get_planet_by_id(planet_id):
    planet = validate_planet(planet_id)
    return { 
            "name": planet.name,
            "description": planet.description,
            "distance from sun": planet.distance_from_sun
    }


    # planet_list = []
    # for planet in planets:
    #     planet_list.append({
    #     "id" : planet.id,
    #     "name" : planet.name,
    #     "description" : planet.description,
    #     "distance from sun" : planet.dist_from_sun
    #     }
    #     )
    # return jsonify(planet_list)

# @planets_bp.route("/<planet_id>", methods = ["GET"])
# def get_planet_by_id(planet_id):
#     planet = validate_planet(planet_id)
#     return planet.to_dict()


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"planet {planet_id} is invalid"}, 400))

    planet = Planet.query.get(planet_id)
    
    if not planet:
        abort(make_response({"message": f"planet {planet_id} not found"}, 404))
    return planet

    # for planet in planets:
    #     if planet.id == planet_id:
    #         return planet


