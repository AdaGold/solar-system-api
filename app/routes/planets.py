from flask import Blueprint, jsonify, abort, make_response
from ..source.planet import Planet

planets = [
    Planet(1, "Mercury" ,"First planet of the solar system",True),
    Planet(2, "Venus" ,"2nd planet of the solar system",True),
    Planet(3, "Earth" ,"3rd planet of the solar system",True),
    Planet(4, "Mars" ,"4th planet of the solar system",True),
    Planet(5, "Jupiter" ,"5th planet of the solar system",False),
    Planet(6, "Saturn" ,"6th planet of the solar system",False),
    Planet(7, "Uranus" ,"7th planet of the solar system",False),
    Planet(8, "Neptune" ,"8th planet of the solar system",False)
    
]

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("",methods=["GET"])
def get_all_planets():
    planets_response = []
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
            if planet.id == planet_id:
                return planet.to_dict()
                
    abort(make_response({"message" :  f"Planet id {planet_id} is Not Found" },404))

@planets_bp.route("/<planet_id>",methods=["GET"])
def get_planet(planet_id):
     planet_info = validate_planet(planet_id)
     return jsonify(planet_info)

