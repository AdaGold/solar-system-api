from app import db
from flask import Blueprint, jsonify, abort, make_response, request
from app.models.planet import Planet


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
                            name=request_body["name"],
                            description=request_body["description"],
                            position_from_sun=request_body["position_from_sun"]
                        )
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)


@planets_bp.route("", methods=["GET"])
def get_planets():
    planets = Planet.query.all()
    planets_response = []
    for planet in planets:
        planets_response.append(make_planet_dict(planet))
    return jsonify(planets_response)


@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return make_planet_dict(planet)


@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.name=request_body["name"]
    planet.description=request_body["description"]
    planet.position_from_sun=request_body["position_from_sun"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated")

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted")

# Helper functions
def make_planet_dict(planet):
    return dict(
        id=planet.id,
        name=planet.name,
        description=planet.description,
        position_from_sun=planet.position_from_sun
    )

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"planet {planet_id} is invalid"}, 400))
    
    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message": f"planet not found"}, 404))

    return planet



