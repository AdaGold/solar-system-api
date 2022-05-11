from requests import request
from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request
from .helper import validate_planet

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

# CREATE PLANET
@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()

    new_planet = Planet.create(request_body)

    db.session.add(new_planet)
    db.session.commit()

    # return make_response(jsonify(f"Planet {new_planet.name} successfully created!", 201))
    return make_response(jsonify(f"Planet {new_planet.name} successfully created"), 201)

# GET ALL
@planets_bp.route("", methods=["GET"])
def read_all_planets():
    name_query = request.args.get("name")
    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    else:
        planets = Planet.query.all()

    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_json())

    return jsonify(planets_response), 200

# GET one planet 
@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    # return jsonify(planet.to_json()), 200
    return jsonify(planet.to_json())

# UPDATE one planet
@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.update(request_body)

    db.session.commit()
    return make_response(jsonify(f"Planet #{planet.id} successfully updated")), 200

# DELETE one planet
@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(jsonify(f"Planet #{planet.id} successfully deleted")), 200