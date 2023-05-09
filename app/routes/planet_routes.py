from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request
from .routes_helpers import validate_model


planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planet_bp.route("", methods=["GET"])
def read_all_planets():

    planets_list = []

    color_param = request.args.get("color")
    if color_param:
        planets = Planet.query.filter_by(color=color_param)
    else:
        planets = Planet.query.all()
    planets_list = [planet.make_dict() for planet in planets]

    return jsonify(planets_list), 200   

@planet_bp.route("/<id>", methods=["GET"])
def read_one_planet(id):
    planet = validate_model(Planet, id)
    
    return jsonify(planet.make_dict()), 200

@planet_bp.route("", methods=["POST"])
def create_planet():
    if request.method == "POST":
        request_body = request.get_json()
        if "name" not in request_body or "description" not in request_body or "color" not in request_body:
            return make_response("Invalid Request", 400)

        new_planet = Planet.from_dict(request_body)

        db.session.add(new_planet)
        db.session.commit()

        return make_response(
            f"Planet {new_planet.name} successfully created", 201
        )
    
@planet_bp.route("/<id>", methods=["PUT"])
def update_planet(id):
    planet = validate_model(Planet, id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.color= request_body["color"]
    
    db.session.commit()

    return make_response(
        f"Planet #{id} successfully updated", 200
    )

@planet_bp.route("/<id>", methods=["DELETE"])
def delete_planet(id):
    planet = validate_model(Planet, id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f'Planet #{id} successfully deleted'), 200