from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request


planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def handle_post_planets():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                    description=request_body["description"],
                    moons = int(request_body["moons"]))

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def handle_read_planets():
    planets = Planet.query.all()
    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_json())

    return jsonify(planets_response)


@planets_bp.route("/<id>", methods=["GET"])
def handle_one_planet(id):
    planet = validate_planet(id)
    return jsonify(planet.to_json())

@planets_bp.route("/<id>", methods=["PUT"])
def update_one_planet(id):
    planet = validate_planet(id)

    request_body = request.get_json()

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






def validate_planet(id):
    if not id.isdigit():
        abort(make_response({"message":f"planet_id {id} invalid"}, 400))
    
    planet = Planet.query.get(id)
    if (planet == None):
        abort(make_response({"message":f"planet {id} not found"}, 404))

    return planet