from flask import Blueprint, jsonify, make_response, abort

class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

planets = [
    Planet(1, "Earth", "Solid"),
    Planet(2, "Mars", "Solid"),
    Planet(3, "Saturn", "Gas")
]

planet_bp = Blueprint("planet_blue_print", __name__, url_prefix="/planets")
@planet_bp.route("", methods=["GET"])
def get_planet():
    all_planets = []
    for planet in planets:
        planet_dic = {"id" : planet.id,
                      "name" : planet.name,
                      "description" : planet.description}
        all_planets.append(planet_dic)
    return jsonify(all_planets)

planet_bp = Blueprint("planet_blue_print", __name__, url_prefix="/planets")
@planet_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = valid_id(planet_id)
    return {"id": planet.id,
            "name" : planet.name,
            "description": planet.description}
    #return f"This {id} not found", 404
    #abort(make_response({"message":f"id {planet_id} not found"}, 404))

def valid_id(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"id {planet_id} is not valid"}, 400))
    for planet in planets:
        if planet.id == id:
            return planet
    abort(make_response({"message":f"id {planet_id} not found"}, 404))