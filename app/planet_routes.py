from flask import Blueprint, jsonify, make_response, abort, request
from app.models.planet import Planet
from app.helpers import validate_model, apply_filters
from app import db

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")


#POST Planets
@planet_bp.route("", methods=["POST"])
def create_planet():
    try:
        request_body = request.get_json()
        new_planet = Planet.from_dict(request_body)
        db.session.add(new_planet)
        db.session.commit()

        message = f"Planet {new_planet.name} successfully created."
        return make_response(message, 201)
    
    except KeyError as error:
        message = f"missing required value: {error}"
        abort(make_response({"message": message}, 400))


# GET Planets 
@planet_bp.route("", methods=["GET"])
def get_all_planets():

    query_params = {
        "name": request.args.get("name"),
        "description": request.args.get("description")
    }
    
    planets = apply_filters(Planet, query_params).all()
        
    results = [planet.to_dict() for planet in planets]
    
    return jsonify(results), 200


# GET one planet
@planet_bp.route("/<planet_id>", methods = ["GET"])
def get_one_planet(planet_id):

    planet = validate_model(Planet, planet_id)

    return jsonify(planet.to_dict()), 200


# PUT one planet
@planet_bp.route("/<planet_id>", methods = ["PUT"])
def replace_one_planet(planet_id):

    planet_to_update = validate_model(Planet, planet_id)

    planet_request_body = request.get_json()

    planet_to_update.name = planet_request_body["name"]
    planet_to_update.description = planet_request_body["description"]

    db.session.commit()
    
    message = f"Planet {planet_to_update.id} successfully updated"
    return make_response(message, 200)


# DELETE one planet
@planet_bp.route("/<planet_id>", methods = ["DELETE"])
def delete_one_planet(planet_id):

    planet_to_delete = validate_model(Planet, planet_id)

    db.session.delete(planet_to_delete)
    db.session.commit()

    message = f"Planet {planet_to_delete.id} successfully deleted"
    return make_response(message, 200)