from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, description, num_moons):
        self.id = id
        self.name = name
        self.description = description
        self.num_moons = num_moons

    def planet_dict(self):
        return dict(
            id = self.id,
            name = self.name,
            description = self.description,
            num_moons = self.num_moons
        )    

planets = [
    Planet(1,"mercury", "terrestrial",0),
    Planet(2,"venus", "terrestrial",0),
    Planet(3,"earth", "terrestrial",1),
    Planet(4,"mars", "terrestrial",2),
    Planet(5,"jupiter", "gas giant",95),
    Planet(6,"saturn", "gas giant",83),
    Planet(7,"uranus", "ice giant",27),
    Planet(8,"neptune", "ice giant",14)
]

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        abort(make_response({"message": f"planet {planet_id} is invalid. Find a planet in our solar system!"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet
    abort(make_response({"message": f"planet {planet_id} is not found. Find a planet in our solar system!"}, 404))

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def handle_planets():
    results = []

    for planet in planets:
        results.append(planet.planet_dict())
    return jsonify(results)
    

@planets_bp.route("/<planet_id>",methods=["GET"])
def handle_planet(planet_id):
    planet = validate_planet(planet_id)

    return planet.planet_dict()

