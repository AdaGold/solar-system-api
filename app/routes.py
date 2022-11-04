from attr import validate
from app import db
from app.models.planet import Planet

from crypt import methods
from flask import Blueprint , jsonify, abort, make_response, request


planet_bp = Blueprint("planets", __name__,url_prefix="/planets")

def validate_planet(cls, planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {planet_id} invalid"}, 400))
    
    planet = cls.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"{cls.__name__} {planet_id} not found"}, 404))
    
    return planet

@planet_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(jsonify(f"Planet {new_planet.name} successfully created"), 201)

@planet_bp.route("", methods=["GET"])
def read_all_planets():
    planet_query = request.args.get("name")
    if planet_query:
        planets = Planet.query.filter_by(name=planet_query)
    else:
        planets = Planet.query.all()

    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_dict())
    return jsonify(planets_response)
    

@planet_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(Planet,planet_id)
    return planet.to_dict()

@planet_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(jsonify(f"Planet #{planet.id} successfully deleted!"))

@planet_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(Planet, planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.diameter = request_body["diameter"]

    db.session.commit()

    return make_response(jsonify(f"Planet #{planet_id} successfully updated! "))
