from os import abort
from turtle import title
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



# def handle_planets():

def validate_planet(class_obj, planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"planet {planet_id} has an invalid planet_id"}, 400))

    query_result = class_obj.query.get(planet_id)

    if not query_result:
        abort(make_response({"message": f"planet {planet_id} not found"}, 404))


    return query_result

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    color_param =request.args.get("color")
    name_param = request.args.get("name")
    
    if color_param:
        planets = Planet.query.filter_by(color=color_param)
    elif name_param:
        planets = Planet.query.filter_by(name=name_param)
    else:
        planets = Planet.query.all()
    planets_response = []

    for planet in planets:
        planets_response.append(planet.to_dict())
            
    return jsonify(planets_response), 200
    
@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.from_json(request_body)
    db.session.add(new_planet)
    db.session.commit()
# I have changed this retun statement and run the test. My terminal is acting up. Plaease try to run the test.
    #return make_response(jsonify(f"planet {new_planet.name} successfully created")), 201
    return make_response(f"planet {new_planet.name} successfully created"), 201

@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(Planet, planet_id)
    return jsonify(planet.to_dict()), 200

# We should also make this change to jsonify our response body 
# in the PUT /books/<book_id> and DELETE /books/<book_id> routes. 
# This adds predictability to our RESTful routes.

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()
    
    planet.update(request_body)

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.color = request_body["color"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated")



@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted")


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