from flask import Blueprint, jsonify
from source.planet import Planet

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
    planets_res = []
    for planet in planets:
        planets_res.append({
            "planet_id" : planet.id,
            "name" : planet.name,
            "description" : planet.description,
            "is_rocky" : planet.is_rocky
        })
    return jsonify(planets_res)
