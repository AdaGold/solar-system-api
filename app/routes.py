from flask import Blueprint, jsonify, abort, make_response, request
from app.filter_attributes import PLANET_ATTRIBUTES
from app.models.moon import Moon
from app.models.planet import Planet
from app import db
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")
moons_bp = Blueprint("moons", __name__, url_prefix="/moons")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"{planet_id} invalid"}, 400))
    planet = Planet.query.get(planet_id)
    if planet:
        return planet
    abort(make_response({"message":f"Planet with {planet_id} not found"}, 404))

def validate_moon(moon_id):
    try:
        moon_id=int(moon_id)
    except:
        abort(make_response({"message":f"moon {moon_id} invalid"}))
    
    moon = Moon.query.get(moon_id)
    if moon:
        return moon
    
    abort(make_response({"message": f"moon {moon_id} not found"}))


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
        planets_response.append({
            "id": planet.id,
            "name": planet.name, 
            "description": planet.description,
            "mass": planet.mass,
            "diameter":planet.diameter,
            "density": planet.density,
            "gravity": planet.gravity,
            "escape_velocity": planet.escape_velocity,
            "rotation_period": planet.rotation_period,
            "day_length": planet.day_length,
            "distance_from_sun":planet.distance_from_sun,
            "orbital_period": planet.orbital_period,
            "orbital_velocity" : planet.orbital_velocity,
            "orbital_inclination": planet.orbital_inclination,
            "orbital_eccentricity":planet.orbital_eccentricity,
            "obliquity_to_orbit":planet.obliquity_to_orbit,
            "mean_tempurature":planet.mean_tempurature_c,
            "surface_pressure":planet.surface_pressure,
            "global_magnetic_feild":planet.global_magnetic_feild,
            "img":planet.img,
            "Has Rings": planet.has_rings,
            #"moons":planet.moons
        })
    return jsonify(planets_response)

@planets_bp.route("", methods=["POST"])
def create_planets():
    request_body=request.get_json()
    for key in PLANET_ATTRIBUTES:
        if not key in request_body:
            abort(make_response({"message": f"Bad request: {key} attribute is missing"}, 400))
    new_planet = Planet(
    name=request_body["name"],
    description=request_body["description"],
    mass=request_body["mass"],
    diameter=request_body["diameter"],
    density=request_body["density"],
    gravity=request_body["gravity"],
    escape_velocity=request_body["escape_velocity"],
    rotation_period=request_body["rotation_period"],
    day_length=request_body["day_length"],
    distance_from_sun=request_body["distance_from_sun"],
    orbital_period=request_body["orbital_period"],
    orbital_velocity=request_body["orbital_velocity"],
    orbital_inclination=request_body["orbital_inclination"],
    orbital_eccentricity=request_body["orbital_eccentricity"],
    obliquity_to_orbit=request_body["obliquity_to_orbit"],
    mean_tempurature_c=request_body["mean_tempurature_c"],
    surface_pressure=request_body["surface_pressure"],
    global_magnetic_feild=request_body["global_magnetic_feild"],
    img=request_body["img"],
        has_rings=request_body["has_rings"])
    db.session.add(new_planet)
    db.session.commit()
    return make_response(f"New Planet {new_planet.name} created!", 201)

@planets_bp.route("/<planet_id>", methods=["GET"])
def display_planet(planet_id):
    planet = validate_planet(planet_id)
    planet_response = []
    planet_response.append({
            "id": planet.id,
            "name": planet.name, 
            "description": planet.description,
            "mass": planet.mass,
            "diameter":planet.diameter,
            "density": planet.density,
            "gravity": planet.gravity,
            "escape_velocity": planet.escape_velocity,
            "rotation_period": planet.rotation_period,
            "day_length": planet.day_length,
            "distance_from_sun":planet.distance_from_sun,
            "orbital_period": planet.orbital_period,
            "orbital_velocity" : planet.orbital_velocity,
            "orbital_inclination": planet.orbital_inclination,
            "orbital_eccentricity":planet.orbital_eccentricity,
            "obliquity_to_orbit":planet.obliquity_to_orbit,
            "mean_tempurature_c":planet.mean_tempurature_c,
            "surface_pressure":planet.surface_pressure,
            "global_magnetic_feild":planet.global_magnetic_feild,
            "img":planet.img,
            "Has Rings": planet.has_rings,
            #"moons":planet.moons
        })
    return jsonify(planet_response)

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_a_planet(planet_id):
    planet = validate_planet(planet_id)
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
    return make_response(f"Planet {planet.id} successfully updated")

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_a_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {planet.id} successfully deleted")


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
    
    return {
        "id": moon.id,
        "name": moon.name,
        "description": moon.description,
        "image": moon.image
    }

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





@moons_bp.route("/<moon_id>", methods=["DELETE"])
def delete_moon(moon_id):
    moon=validate_moon(moon_id)
    
    db.session.delete(moon)
    db.session.commit()

    return make_response(f"moon {moon.id} successfully deleted")