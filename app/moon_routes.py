from flask import Blueprint, jsonify, abort, make_response, request 
from app import db 
from app.models.moon import Moon 
from app.models.planet import Planet 
from app.planet_routes import validate_model

moon_bp = Blueprint("moons_bp", __name__, url_prefix="/moons")



@moon_bp.route("", methods=["POST"])
def create_new_moon():
    request_body = request.get_json()
    new_moon = Moon(name = request_body["name"], )

    db.session.add(new_moon)
    db.session.commit()

    return make_response(jsonify(f"Moon {new_moon.name} successfully created."), 201)


@moon_bp.route("/<moon_id>", methods=["GET"])
def read_moon_by_id(moon_id): 
    moon_response = validate_model(Moon, moon_id)

    result_dict = {
        "id" : moon_response.id,
        "name" : moon_response.name, 
    }

    return make_response(jsonify(result_dict), 200) 

@moon_bp.route("/all", methods=["GET"])
def read_all_moons(): 
    all_moon = Moon.query.all()

    moons_response = [] 
    for moon in all_moon: 
        moons_response.append({
        "id" : moon.id,
        "name" : moon.name, 
    }
)
    return make_response(jsonify(moons_response), 200) 

@moon_bp.route("/<planet_id>/moon", methods = ["POST"])
def create_moon_to_planet_by_planet_id(planet_id): 
    new_planet = validate_model(Planet, planet_id)

    request_body = request.get_json() 
    new_moon = Moon(
        name = request_body["name"],
        planet_id = new_planet.id, 
        planet = new_planet
        )

    db.session.add(new_moon)
    db.session.commit()

    return make_response(jsonify(f"Moon {new_moon.name} successfully created to planet {planet_id}"), 201)

@moon_bp.route("/<planet_id>/moons", methods=["GET"])
def get_moons_by_planet_id(planet_id): 
    planet = validate_model(Planet, planet_id)
    
    response = planet.to_dict()
    return make_response(jsonify(response),200) 

