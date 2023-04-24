from flask import Blueprint, jsonify, make_response, abort

class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def to_dict(self):
        return {"id": self.id,
            "name" : self.name,
            "description": self.description}

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
        planet_dic = planet.to_dict()
        all_planets.append(planet_dic)
    return jsonify(all_planets)


@planet_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_id(planet_id)
    return planet.to_dict()

def validate_id(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"id {planet_id} is not valid"}, 400))
    for planet in planets:
        if planet.id == id:
            return planet
    abort(make_response({"message":f"id {planet_id} not found"}, 404))