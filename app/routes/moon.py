from app.models.moon import Moon
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.routes.planet import planets_bp, validate_model
moons_bp = Blueprint("moons", __name__, url_prefix="/moons")


@planets_bp.route("/<planet_id>/moons", methods=["POST"])
def create_moon(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()
    try:
        new_moon = Moon(
        name=request_body["name"],
        size = request_body["size"],
        description = request_body["description"],
        image = request_body["image"],
        planet=planet
    )
    except KeyError as key_error:
        abort(make_response({"message": f"Bad request: {key_error.args[0]} attribute is missing"}, 400))

    db.session.add(new_moon)
    db.session.commit()
    return make_response(jsonify(f"New Moon {new_moon.name} created!"), 201)

@planets_bp.route("/<planet_id>/moons", methods=["GET"])
def get_all_moons_by_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    moons_response = []
    for moon in planet.moons:
        moons_response.append({
            "id":moon.id,
            "name": moon.name,
            "size": moon.size,
            "description": moon.description,
            "image":moon.image,

        })
    return jsonify(moons_response)
    
@moons_bp.route("", methods=["GET"])
def get_all_moons():
    moons = Moon.query.all()
    moons_response = []
    for moon in moons:
        moons_response.append(moon.to_dict())
    return jsonify(moons_response)


@moons_bp.route("/<moon_id>", methods=["GET"])
def get_moon_by_id(moon_id):
    moon=validate_model(Moon, moon_id)
    
    return jsonify({
        "id": moon.id,
        "name": moon.name,
        "size": moon.size,
        "description": moon.description,
        "image": moon.image
    })

@moons_bp.route("/<moon_id>", methods=["PUT"])
def update_moon(moon_id):
    moon=validate_model(Moon, moon_id)
    request_body = request.get_json()
    moon.name = request_body["name"]
    moon.size = request_body["size"]
    moon.description=request_body["description"]
    moon.image=request_body["image"]

    db.session.commit()
    return make_response(jsonify(f"Moon {moon.name} has been updated"))

@moons_bp.route("/<moon_id>", methods=["DELETE"])
def delete_a_moon(moon_id):
    moon = validate_model(Moon, moon_id)

    db.session.delete(moon)
    db.session.commit()

    return make_response(jsonify(f"Moon {moon.id} successfully deleted"))

