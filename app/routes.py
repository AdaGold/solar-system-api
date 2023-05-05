from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")



#helper function
def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except: 
        abort(make_response({"message": f"{cls.__name__} {model_id} is invalid. Find a planet in our solar system!"}, 400))

    
    model = cls.query.get(model_id)
    if not model:
        abort(make_response({"message": f"{cls.__name__} {model_id} is not found. Find a planet in our solar system!"}, 404))
    return model

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)


@planets_bp.route("", methods=["GET"])
def read_all_planets():
    name_query = request.args.get("name")
    if name_query:
        planets = Planet.query.filter_by(name = name_query)
    else:
        planets = Planet.query.all()
    results = [planet.to_dict() for planet in planets]
    return jsonify(results), 200

@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    return  jsonify(planet.to_dict()), 200

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_model(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]

    db.session.commit()

    return make_response(f"Planet # {planet_id} successfully updated")

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_model(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet # {planet_id} successfully deleted")