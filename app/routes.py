from app import db
from app.models.planet import Planet
# from unicodedata import name
from flask import Blueprint, jsonify, abort, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

#helper function
def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"Planet {planet_id} invalid"}, 400))
        
    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"planet {planet_id} not found"}, 404))

    return planet

#route functions
@planets_bp.route("", methods=["GET"])
def read_all_planets():
    #planets = Planet.query.all()
    planets_response = []

    name_param=request.args.get("name")
    description_param=request.args.get("description")
    size_param=request.args.get("size")
    
    if name_param:
        planets=Planet.query.filter_by(name=name_param)
    elif description_param:
        planets=Planet.query.filter_by(description=description_param)
    elif size_param:
        planets=Planet.query.filter_by(size=size_param)
    else:
        planets=Planet.query.all()


    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "size": planet.size
            }), 200
        #planets_response.append(planet.dict_planet())
    return jsonify(planets_response),200

@planets_bp.route("", methods=["POST"])
def create_planet():          
    request_body = request.get_json()
    print (request_body)
    new_planet = Planet(name=request_body["name"],
            description=request_body["description"],
            size=request_body["size"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(jsonify(f"Planet {new_planet.name} successfully created"), 201)

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

@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return jsonify({
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "size": planet.size
    }), 200

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.size = request_body["size"]

    db.session.commit()

    return make_response(jsonify(f"Planet #{planet.id} successfully updated"), 200)

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(jsonify(f"Planet #{planet.id} successfully deleted"), 200)