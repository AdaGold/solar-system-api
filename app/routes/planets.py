from flask import Blueprint, jsonify, abort, make_response,request
from app.models.planet import Planet
from app import db

'''
planets = [
    Planet(1, "Mercury" ,"Mercury is the smallest planet of our solar system.",True),
    Planet(2, "Venus" ,"Venus is the hottest planet in the solar system.",True),
    Planet(3, "Earth" ,"This is the only place where there is life.",True),
    Planet(4, "Mars" ,"This planet is very cold and dry but there is ice at the poles.",True),
    Planet(5, "Jupiter" ,"The planet has more than 80 moons and the largest moon of all planets.",False),
    Planet(6, "Saturn" ,"Saturn has a beatuful visible rings.",False),
    Planet(7, "Uranus" ,"The planet orbits on its side and has 27 moons.",False),
    Planet(8, "Neptune" ,"Neptune is a planet of heavy winds and storms.",False)
]'''

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("",methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name = request_body["name"],
        description = request_body["description"],
        is_rocky = request_body["is_rocky"]
    )

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("",methods=["GET"])
def get_all_planets():
    planets_response = []
    planets = Planet.query.all()
    for planet in planets:
        planets_response.append(planet.to_dict())
    return jsonify(planets_response)

def validate_planet(planet_id):
    try:
        id = int(planet_id)
    except:
        msg = f"Planet id {planet_id} is Invalid"
        abort(make_response({"message" : msg },400))
    for planet in planets:
        if planet.id == id:
            return planet.to_dict()
                
    abort(make_response({"message" :  f"Planet id {planet_id} is Not Found" },404))

@planets_bp.route("/<planet_id>",methods=["GET"])
def get_planet(planet_id):
    planet_info = validate_planet(planet_id)
    return jsonify(planet_info)

