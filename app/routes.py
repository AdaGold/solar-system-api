from requests import request
from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request
from .helper import validate_planet



# planets = [
#     Planet(1, "Earth", "blue planet", 1),
#     Planet(2, "Mercury", "closest to sun"),
#     Planet(3, "Jupiter", "has big spot", 66)
# ]
planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message":f"planet_id {planet_id} invalid"}, 400))
        
#     planet = Planet.query.get(planet_id)

#     if not planet:
#         abort(make_response({"message":f"planet {planet_id} not found"}, 404))

#     return planet

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()

    new_planet = Planet.create(request_body)

    # new_planet = Planet(name=request_body["name"],
    #                     description=request_body["description"],
    #                     moons=request_body["moons"])
    db.session.add(new_planet)
    db.session.commit()

    return make_response(jsonify(f"Planet {new_planet.name} successfully created"), 201)

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    name_query = request.args.get("name")
    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    else:
        planets = Planet.query.all()

    planets_response = []
    for planet in planets:
        planets_response.append(
            {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "moons": planet.moons
            }
        )

    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "moons": planet.moons
    }
    
@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()

    planet.update(request_body)

    # planet.name = request_body["name"]
    # planet.description = request_body["description"]
    # planet.moons = request_body['moons']

    db.session.commit()

    return make_response(jsonify(f"Planet #{planet.id} successfully updated"))

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(jsonify(f"Planet #{planet.id} successfully deleted"))