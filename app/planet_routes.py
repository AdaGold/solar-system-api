from app import db
from app.models.planet import Planet
from app.models.moon import Moon
from app.route_helper_funcs import validate_model, validate_moon, validate_planet
from flask import Blueprint, jsonify, make_response, request, abort


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    check_invalid_request = validate_planet(request_body)
    if check_invalid_request:
        abort(make_response(jsonify(check_invalid_request), 400))
    new_planet = Planet.from_dict(request_body)
    db.session.add(new_planet)
    db.session.commit()
    db.session.refresh(new_planet)
    # return make_response(jsonify(f"Planet {new_planet.name} successfully created"), 201)
    return new_planet.to_dict(), 201
            

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
    planet = validate_model(Planet, planet_id)
    return planet.to_dict()

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()
    check_invalid_request = validate_planet(request_body)
    if check_invalid_request:
        abort(make_response(jsonify(check_invalid_request), 400))
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.distance_from_earth = request_body["distance_from_earth"]
    planet.size = request_body["size"]
    db.session.commit()
    db.session.refresh(planet)
    #return make_response(jsonify(f"Planet #{planet.id} successfully updated"))
    return planet.to_dict()

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    db.session.delete(planet)
    db.session.commit()
    # return make_response(jsonify(f"Planet #{planet.id} successfully deleted"))
    return planet.to_dict(), 200


# try adding a PATCH request
@planets_bp.route("/<planet_id>", methods=["PATCH"])
def patch_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()
    for key, value in request_body.items():
        try:
            getattr(planet, key)
        except AttributeError:
            abort(make_response({"message": f"Attribute {key} does not exist"}, 400))
        setattr(planet, key, value)
    db.session.commit()
    db.session.refresh(planet)
    # return make_response(jsonify(f"Planet #{planet.id} successfully updated attribute"))
    return planet.to_dict()


@planets_bp.route("/<planet_id>/moons", methods=["POST"])
def create_moon_for_a_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()
    validate_moon_record = validate_moon(request_body)
    if validate_moon_record:
        abort(make_response(jsonify(validate_moon_record), 400))
    new_moon = Moon(
        name=request_body["name"],
        description=request_body["description"],
        radius=request_body["radius"],
        planet=planet
    )
    db.session.add(new_moon)
    db.session.commit()
    return new_moon.to_dict(), 200


@planets_bp.route("/<planet_id>/moons", methods=["GET"])
def get_all_moons_of_a_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    moons_response = list()
    for moon in planet.moons:
        moons_response.append(
            moon.to_dict()
        )
    return jsonify(moons_response)

