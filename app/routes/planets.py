from flask import Blueprint, jsonify, abort, make_response, request
from app.models.planet import Planet
from app.models.moon import Moon
from app import db
from app.routes.helpers import validate_model, validate_request_body
from app.routes.moons import moon_validate_request_body

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

needed_planet_data = ["name","description","is_rocky"]

@planets_bp.route("",methods=["POST"])
def create_planet():
    request_body = request.get_json(silent=True)  #the silent=True prevents this function from raising an exception if a bad or incomplete json was send
    new_planet = Planet.from_dict(validate_request_body(request_body,needed_planet_data))

    db.session.add(new_planet)
    db.session.commit()

    return make_response(jsonify(f"Planet {new_planet.name} successfully created"), 201)

@planets_bp.route("",methods=["GET"])
def get_all_planets():
    planet_query = Planet.query  
    
    name_query = request.args.get("planet_name")
    if name_query:
        planet_query = planet_query.filter(Planet.name.ilike(f"%{name_query}%"))

    sort_query = request.args.get("sort")
    if sort_query:
        if sort_query == "desc":
            planet_query = planet_query.order_by(Planet.name.desc())
        else:
            planet_query = planet_query.order_by(Planet.name.asc())

    planets = planet_query.all()
    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_dict())
    return jsonify(planets_response)


@planets_bp.route("/<planet_id>",methods=["GET"])
def get_planet(planet_id):
    planet_info = validate_model(Planet, planet_id)
    return jsonify(planet_info.to_dict())

@planets_bp.route("/<planet_id>",methods=["PUT"])
def update_planet(planet_id):
    planet_info = validate_model(Planet, planet_id)
    request_body = request.get_json(silent=True)  #the silent=True prevents this function from raising an exception if a bad or incomplete json was send
    validate_request_body(request_body,needed_planet_data)

    planet_info.name = request_body["name"]
    planet_info.description= request_body["description"]
    planet_info.is_rocky = request_body["is_rocky"]

    db.session.commit()
    
    return make_response(jsonify(f"Planet {planet_info.name} successfully updated"), 200)

@planets_bp.route("/<planet_id>",methods=["DELETE"])
def delete_planet(planet_id):
    planet_info = validate_model(Planet, planet_id)
    
    db.session.delete(planet_info)
    db.session.commit()
    
    return make_response(jsonify(f"Planet {planet_info.name} successfully deleted"), 200)

@planets_bp.route("/<planet_id>/moons",methods=["GET"])
def get_moons_of_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    moons_response = [moon.to_dict() for moon in planet.moons]

    return make_response(jsonify(moons_response),200)

@planets_bp.route("/<planet_id>/moons",methods=["POST"])
def add_new_moons_to_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json(silent=True)  #the silent=True prevents this function from raising an exception if a bad or incomplete json was send
    new_moon = Moon.from_dict(moon_validate_request_body(request_body))
    new_moon.planet = planet

    db.session.add(new_moon)
    db.session.commit()

    return make_response(jsonify(f"Moon {new_moon.name} of {new_moon.planet.name} successfully created"), 201)