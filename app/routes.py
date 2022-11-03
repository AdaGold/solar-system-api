from flask import Blueprint, jsonify, abort, make_response, request
from app.models.planet import Planet
from app import db

bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"book {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"book {planet_id} not found"}, 404))

    return planet

@bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        rings=request_body["rings"])
    
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} succesfully created", 201)

@bp.route("", methods=["GET"])
def get_all_planets():
    planets = Planet.query.all()
    planets_response = []
    for planet in planets:
        planets_response.append(planet.build_planet_dict())

    return jsonify(planets_response), 400

@bp.route("/<id>", methods=["GET"])
def read_one_planet(id):
    planet = validate_planet(id)

    return jsonify(planet.build_planet_dict())

@bp.route("/<id>", methods=["PUT"])
def update_planet(id):
    planet = validate_planet(id)
    request_body = request.get_json()

    planet.name = request_body["name"],
    planet.description = request_body["description"],
    planet.rings = request_body["rings"]

    db.session.commit()

    return make_response(f"Planet #{id} successfully updated")

# @bp.route("/guide/<id>", methods=["DELETE"])
# def planet_delete(id):
#     request_body = request.get_json()
#     planet_delete = Planet(title=request_body["name"],
#                     description=request_body["description"],
#                     rings=request_body["rings"])

#     return make_response(f"Planet {planet_delete} successfully deleted", 201)