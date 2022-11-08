from os import abort
from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

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

    return make_response(f"planet {new_planet.name} successfully created"), 201

@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(Planet, planet_id)
    return jsonify(planet.to_dict()), 200

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()
    
    planet.update(request_body)

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.color = request_body["color"]

    db.session.commit()

    return make_response (f"Planet #{planet.id} successfully updated")

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted")
