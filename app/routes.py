from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

def error_message(message, status_code):
    abort(make_response({"message":message}, status_code))

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        error_message(f"planet {planet_id} invalid", 400)

    planet = Planet.query.get(planet_id)
    if not planet:
        error_message(f"planet {planet_id} not found", 404)

    return planet

@planets_bp.route("", methods=["GET"])
def index_planets():
    if request.method == "GET":
        color_query = request.args.get("color")
        if color_query:
            planets = Planet.query.filter_by(color=color_query)
        else:
            planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append(planet.to_dict())
        return jsonify(planets_response)

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()

    try:
        new_planet = Planet.from_dict(request_body)
    except KeyError as err:
        error_message(f"Missing Key: {err}", 400)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return planet.to_dict()


@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.color = request_body["color"]
    planet.name = request_body["name"]
    planet.description = request_body["description"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated")

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted")
