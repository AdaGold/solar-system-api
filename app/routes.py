from flask import Blueprint, jsonify, abort, make_response, request
from app.models.planet import Planet
from app import db

bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"Planet #{planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"Planet #{planet_id} not found"}, 404))

    return planet

@bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        rings=request_body["rings"])
    
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@bp.route("", methods=["GET"])
def get_all_planets():
    name_query = request.args.get("name")
    rings_query = request.args.get("rings")
    limit_query = request.args.get("limit")

    planet_query = Planet.query

    if name_query:
        planet_query = planet_query.filter_by(name=name_query)
    if rings_query:
        planet_query = planet_query.filter_by(rings=rings_query)
    if limit_query:
        planet_query = planet_query.limit(limit=limit_query)

    planets = planet_query.all()
    planets_response = []

    for planet in planets:
        planets_response.append(planet.build_planet_dict())

    return jsonify(planets_response)

@bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return jsonify(planet.build_planet_dict())

@bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.rings = request_body["rings"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated", 200)

@bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)
    
    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted", 200)