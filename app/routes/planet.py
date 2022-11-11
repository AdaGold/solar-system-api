from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort
from app.routes.routes_helper import validate_model, validate_input_data, error_message

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


# read one planet (GET)
@planets_bp.route("/<id>", methods=["GET"])
def read_one_planet(id):
    planet = validate_model(Planet, id)

    return jsonify({"planet": planet.to_dict()}), 200

# read all planets (GET)
@planets_bp.route("", methods=["GET"])
def read_all_planets():
     # if in url we add a query param -> /planets?name=pluto
    sort_asc_query = request.args.get("sort")

    if sort_asc_query == "asc": 
        planets = Planet.query.order_by(Planet.name)
    elif sort_asc_query == "desc":
        planets = Planet.query.order_by(Planet.name.desc())
    else:
        planets = Planet.query.all()

    planets_response = [planet.to_dict() for planet in planets]

    return jsonify(planets_response)


# create a planet (POST)
@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()

    new_planet = validate_input_data(Planet, request_body)

    db.session.add(new_planet)
    db.session.commit()

    return jsonify({"planet": new_planet.to_dict()}), 201


# replace a planet (PUT)
@planets_bp.route("/<id>", methods=["PUT"])
def update_planet(id):
    planet = validate_model(Planet, id)

    request_body = request.get_json()

    planet.update(request_body)

    db.session.commit()
   
    response = {"planet": planet.to_dict()}
    return response
    


# delete a planet (DELETE)
@planets_bp.route("/<id>", methods=["DELETE"])
def delete_planet(id):
    planet = validate_model(Planet, id)

    # saves name before being deleted 
    name = planet.name

    db.session.delete(planet)
    db.session.commit()
    
    return(make_response({"details": f"planet {id} \"{name}\" successfully deleted"}), 200)


