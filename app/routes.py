from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except: 
        abort(make_response({"message": f"Planet {planet_id} invalid"}, 400))
    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message": f"Planet {planet_id} is not found"}, 404))
    return planet


# make it fail
"""
@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():
    return make_response("I'm a teapot!", 418)
"""


@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name=request_body["name"],
        description=request_body["description"],
        size=request_body["size"],
        distance_from_earth=request_body["distance_from_earth"]
    )
    db.session.add(new_planet)
    db.session.commit()
    return make_response(jsonify(f"Planet {new_planet.name} successfully created"), 201)
            

@planets_bp.route("", methods=["GET"])
def get_planets():
    planets_response = []
    planet_query = Planet.query
    name_query = request.args.get("name")

    #case insensitive and partial match
    if name_query:
        planet_query = planet_query.filter(Planet.name.ilike(f"%{name_query}%"))
    
    sort_query = request.args.get("sort")
    if sort_query:
        if sort_query == "desc":
            planet_query = planet_query.order_by(Planet.size.desc())
        else: 
            planet_query = planet_query.order_by(Planet.size.asc())

    planets = planet_query.all()

    for planet in planets:
        planets_response.append(
            {
                "name": planet.name,
                "id": planet.id,
                "description": planet.description,
                "size": planet.size,
                "distance_from_earth": planet.distance_from_earth
            }
        )
    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "size": planet.size,
        "distance_from_earth": planet.distance_from_earth
    }

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.distance_from_earth = request_body["distance_from_earth"]

    db.session.commit()
    return make_response(jsonify(f"Planet #{planet.id} successfully updated"))

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)
    db.session.delete(planet)
    db.session.commit()
    return make_response(jsonify(f"Planet #{planet.id} successfully deleted"))


# try adding a PATCH request
@planets_bp.route("/<planet_id>", methods=["PATCH"])
def patch_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()
    for key, value in request_body.items():
        try:
            getattr(planet, key)
        except AttributeError:
            abort(make_response({"message": f"Attribute {key} does not exist"}, 400))
        setattr(planet, key, value)
    db.session.commit()
    return make_response(jsonify(f"Planet #{planet.id} successfully updated attribute"))
