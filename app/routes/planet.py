from flask import Blueprint, jsonify, abort, make_response, request
from app.filter_attributes import PLANET_ATTRIBUTES
from app.models.planet import Planet
from app import db
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{model_id} invalid"}, 400))
    model = cls.query.get(model_id)
    if model:
        return model
    abort(make_response({"message":f"{cls.__name__} with {model_id} not found"}, 404))



def apply_filter(planet_query):
    FILTERABLE_ATTRIBUTES = ['global_magnetic_feild', 'has_rings']
    required_parameters = {}
    for attribute in FILTERABLE_ATTRIBUTES:
        value = request.args.get(attribute)
        if value is not None:
            required_parameters[attribute] = value
    if required_parameters:
        planet_query = planet_query.filter_by(**required_parameters)

    order_by_asc = request.args.get("order_by_asc")
    order_by_desc = request.args.get("order_by_desc")
    max_query = request.args.get("max")
    min_query = request.args.get("min")

    # Validate that only one option at a time is specified
    options = [order_by_asc, order_by_desc, max_query, min_query]
    num_options = sum(1 if option is not None else 0 for option in options)
    if num_options > 1:
        abort(make_response("Bad request: Too many options", 400))

    #greater_than_ave = request.args.get("greater_than_ave")
    if order_by_asc is not None:
        planet_query = planet_query.order_by(getattr(Planet, order_by_asc))
    elif order_by_desc is not None:
        planet_query = planet_query.order_by(getattr(Planet, order_by_desc).desc())
    elif max_query is not None:
        planet_query = planet_query.order_by(getattr(Planet, max_query).desc()).limit(1)
    elif min_query is not None:
        planet_query = planet_query.order_by(getattr(Planet, min_query)).limit(1)
    #elif greater_than_ave is not None:
    #    planet_query = planet_query.query.filter(getattr(Planet, greater_than_ave).func.avg())
    
    return planet_query

@planets_bp.route("", methods=["GET"])
def display_planets():
    planets_response = []
    planet_query = Planet.query
    planet_query = apply_filter(planet_query).all()
    for planet in planet_query:
        planets_response.append(planet.to_dict())
    return jsonify(planets_response)

@planets_bp.route("", methods=["POST"])
def create_planets():
    request_body=request.get_json()
    try:
        new_planet = Planet.from_dict(request_body)
    except KeyError as key_error:
        abort(make_response({"message": f"Bad request: {key_error.args[0]} attribute is missing"}, 400))
    db.session.add(new_planet)
    db.session.commit()
    return make_response(jsonify(f"New Planet {new_planet.name} created!"), 201)

@planets_bp.route("/<planet_id>", methods=["GET"])
def display_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    return planet.to_dict()

        
 

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_a_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()
    for key in PLANET_ATTRIBUTES:
        if not key in request_body:
            abort(make_response({"message": f"Bad request: {key} attribute is missing"}, 400))
    planet.name=request_body["name"]
    planet.description=request_body["description"]
    planet.mass=request_body["mass"]
    planet.diameter=request_body["diameter"]
    planet.density=request_body["density"]
    planet.gravity=request_body["gravity"]
    planet.escape_velocity=request_body["escape_velocity"]
    planet.rotation_period=request_body["rotation_period"]
    planet.day_length=request_body["day_length"]
    planet.distance_from_sun=request_body["distance_from_sun"]
    planet.orbital_period=request_body["orbital_period"]
    planet.orbital_velocity=request_body["orbital_velocity"]
    planet.orbital_inclination=request_body["orbital_inclination"]
    planet.orbital_eccentricity=request_body["orbital_eccentricity"]
    planet.obliquity_to_orbit=request_body["obliquity_to_orbit"]
    planet.mean_tempurature_c=request_body["mean_tempurature_c"]
    planet.surface_pressure=request_body["surface_pressure"]
    planet.global_magnetic_feild=request_body["global_magnetic_feild"]
    planet.img=request_body["img"]
    planet.has_rings=request_body["has_rings"]

    db.session.commit()
    return make_response(jsonify(f"Planet {planet.id} successfully updated"))

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_a_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(jsonify(f"Planet {planet.id} successfully deleted"))