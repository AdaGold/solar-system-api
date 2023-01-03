from app.models.moon import Moon
from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.routes.planet import planets_bp, validate_planet
moons_bp = Blueprint("moons", __name__, url_prefix="/moons")

def validate_moon(moon_id):
    try:
        moon_id=int(moon_id)
    except:
        abort(make_response({"message":f"moon {moon_id} invalid"}))
    
    moon = Moon.query.get(moon_id)
    if moon:
        return moon
    
    abort(make_response({"message": f"moon {moon_id} not found"}))


@planets_bp.route("planets/<planet_id>/moons", methods=["POST"])
def create_moon(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()
    new_moon = Moon(
        name=request_body["name"],
        description = request_body["description"],
        image = request_body["img"],
        planet=planet
    )
    db.session.add(new_moon)
    db.session.commit()
    return make_response(f"New Moon {new_moon.name} creative", 201)

@planets_bp.route("/<planet_id>/moons", methods=["GET"])
def get_all_moons_by_planet(planet_id):
    planet = validate_planet(planet_id)
    moons_response = []
    for moon in planet.moons:
        moons_response.append({
            "id":moon.id,
            "title": moon.title,
            "description": moon.description,
            "image":moon.image,

        })
    return jsonify(moons_response)
    
@moons_bp.route("", methods=["GET"])
def get_all_moons():
    moons = Moon.query.all()
    moons_response = []
    for moon in moons:
        moons_response.append({
            "id":moon.id,
            "title": moon.title,
            "description": moon.description,
            "image":moon.image,
        })
    return jsonify(moons_response)


@moons_bp.route("/<moon_id>", methods=["GET"])
def get_moon_by_id(moon_id):
    moon=validate_moon(moon_id)
    
    return jsonify({
        "id": moon.id,
        "name": moon.name,
        "description": moon.description,
        "image": moon.image
    })

@moons_bp.route("/<moon_id>", methods=["PUT"])
def update_moon(moon_id):
    moon=validate_moon(moon_id)
    request_body = request.get_json()
    moon.name = request_body["name"]
    moon.description=request_body["description"]
    moon.image=request_body["img"]
    moon.planet_id=request_body["planet_id"]

    db.session.commit()
    return make_response(f"Moon {moon.name} has been update", 204)