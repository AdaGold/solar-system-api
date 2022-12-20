from flask import Blueprint, jsonify, abort, make_response, request
from app.models.moon import Moon
from app.models.planet import Planet
from app import db
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")
moons_bp = Blueprint("moons", __name__, url_prefix="/moons")


@planets_bp.route("", methods=["GET"])
def display_planets():
    planets_response = []
    solar_system = Planet.query.all()
    for planet in solar_system:
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

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"{planet_id} invalid"}, 400))
    solar_system = Planet.query.all()
    for planet in solar_system:
        if planet.id == planet_id:
            return planet
    abort(make_response({"message":f"Planet with {planet_id} not found"}, 404))

@planets_bp.route("", methods=["POST"])
def create_planets():
    request_body=request.get_json()
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
    has_rings=request_body["has_rings"]
    )
    db.session.add(new_planet)
    db.session.commit()
    return make_response(f"New Planet {new_planet.name} created!", 201)

# @planets_bp.route("/<planet_id>", methods=["GET"])
# def display_planet(planet_id):
#     planet = validate_planet(planet_id)
#     # return {
#     #     "id": planet.id,
#     #     "name": planet.name, 
#     #     "description": planet.description,
#     #     "Has Rings": planet.has_rings,
#     #     "Moons" : [moon.name for moon in planet.moons]
#     # }
#     # Use __dict__ to access all the attributes from planet
#     return planet.serialize()



@planets_bp.route("/<planet_id>/moons", methods=["POST"])
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

@moons_bp.route("", methods=["GET"])
def get_all_moons():
    moons_response = []
    moons_list = Moon.query.all()
    for moon in moons_list:
        moons_response.append({
            "id":moon.id,
            "title": moon.title,
            "description": moon.description,
            "image":moon.image,
            "planet_id":moon.planet_id,
            "planet":moon.planet
        })
    return jsonify(moons_response)

# def validate_moon(moon_id):
#     try:
#         moon_id=int(moon_id)
#     except:
#         abort(make_response({"message":f"moon {moon_id} invalid"}))
    
#     for moon in moons_list:
#         if moon.id==moon_id:
#             return moon
    
#     abort(make_response({"message": f"moon {moon_id} not found"}))

# @moons_bp.route("/<moon_id>", methods=["GET"])
# def get_moon_by_id(moon_id):
#     moon=validate_moon(moon_id)
    
#     return {
#         "id": moon.id,
#         "name": moon.name,
#         "description": moon.description
#     }