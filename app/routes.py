from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet

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

    return make_response(jsonify(f'planet {new_planet.name} successfully created!'), 201)

@planets_bp.route("", methods = ["GET"])
def planet_data():
    planets = Planet.query.all()
    planets_response = []

    for planet in planets:
        planets_response.append(planet.to_dictionary())
    
    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods = ["GET"])
def get_planet_by_id(planet_id):
    planet = validate_planet(planet_id)
    return jsonify(planet.to_dictionary())

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.distance_from_sun = request_body["distance from sun"]

    db.session.commit()

    return make_response(jsonify(f"Planet {planet.name} successfully updated."))

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet_by_id(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()
    
    return make_response(jsonify(f"Planet {planet.name} successfully deleted."))

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"planet {planet_id} is invalid"}, 400))

    planet = Planet.query.get(planet_id)
    
    if not planet:
        abort(make_response({"message": f"planet {planet_id} not found"}, 404))
    return planet
