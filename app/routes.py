from flask import Blueprint, jsonify, make_response, abort

class Planet:

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
    
    def make_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description
            )
        

    
planets = [
    Planet(1, "Mercury", "The Morning star"),
    Planet(2, "Venus", "The Evening star"),
    Planet(3, "Mars", "The Red planet"),
    Planet(4, "Earth", "The Blue Planet"),
    Planet(5, "Jupiter", "The Giant Planet"),
    Planet(6, "Saturn", "The Ringed Planet"),
    Planet(7, "Uranus", "The Ice Giant"),
    Planet(8, "Neptune", "Big Blue"),
    Planet(9, "Pluto", "The Minor Planet")
    ]

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")


def validate_planet_id(id):
    try:
        id = int(id)
    except:
        abort(make_response({"message": "The id {id} invalid"}, 400))

    for planet in planets:
        if planet.id == id:
            return planet
    
    abort(make_response({"message": "The id {id} not found"}, 404))



@planet_bp.route("/<id>", methods=["GET"])
def handle_planet(id):

    planet = validate_planet_id(id)

    return planet.make_dict()

    

@planet_bp.route("", methods=["GET"])
def handle_planets():
    # results = []
    # for planet in planets:
    #     results.append(planet.make_dict())

    results = [planet.make_dict() for planet in planets]

    return jsonify(results)