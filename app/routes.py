from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, description, feature=None):
        self.id = id
        self.name = name
        self.description = description
        self.feature = feature if feature is not None else ''
        
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "feature": self.feature
        }

planets =[
    Planet(1, "Mercury", "Mercury is the smallest planet in our solar system."),
    Planet(2, "Venus", "Venus is the second planet from the Sun."),
    Planet(3, "Earth", "Earth is an ellipsoid with a circumference of about 40,000 km. It is the densest planet in the Solar System. "),
    Planet(4, "Mars", "Mars is the fourth planet from the sun."),
    Planet(5, "Jupiter is the fifth planet from the sun and the largest planet in the solar system." ),
    Planet(6, "Saturn is the sixth planet from the sun and is famous for its large and distinct ring system. "),
    Planet(7, "Uranus is the seventh planet from the sun and is a bit of an oddball."),
    Planet(8, "Neptune is the eighth planet from the sun and is on average the coldest planet in the solar system.")
    
]
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")
@planets_bp.route("", methods=["GET"])
def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "feature": planet.feature
        })
    return jsonify(planets_response), 200

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))
    for planet in planets:
        if planet.id == planet_id:
            return planet
    abort(make_response({"message": f"planet {planet_id} not found"}, 404))

@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planets_to_return = validate_planet(planet_id)
    return jsonify(planets_to_return.to_dict())