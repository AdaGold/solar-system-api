from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort

planet_bp = Blueprint("planet_bp", __name__, url_prefix = "/planets")


@planet_bp.route("", methods=["POST"])
def handle_planets():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)


@planet_bp.route("", methods = ["GET"])
def all_planet_data():

    name_query = request.args.get("name")
    description_query = request.args.get("description")
    if description_query:
        planets = Planet.query.filter_by(description = description_query)
    elif name_query:
        planets = Planet.query.filter_by(name = name_query)
    else:
        planets = Planet.query.all()
        
    planet_response = []
    for planet in planets:
            planet_response.append(planet.to_dict())
            
    return jsonify(planet_response) 


def validate_planet(cls, planet_id):
    try: 
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {planet_id} invalid"}, 400))
    
    planet = cls.query.get(planet_id)
    
    if not planet:
        abort(make_response({"message":f"{cls.__name__} {planet_id} not found"}, 404))
    
    return planet


@planet_bp.route("/<planet_id>", methods= ["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(Planet, planet_id)

    return planet.to_dict()


@planet_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(Planet, planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated")


@planet_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted")