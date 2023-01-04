from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_planet(cls, model_id):
    try:
        model_id = int(model_id)
    except: 
        abort(make_response({"message": f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message": f"{cls.__name__} {model_id} is not found"}, 404))
    return model


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
        planets_response.append(planet.to_dict())
    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return planet.to_dict()

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    
    planet = validate_planet(planet_id)
    request_body = request.get_json()
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.distance_from_earth = request_body["distance_from_earth"]
    planet.size = request_body["size"]

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
