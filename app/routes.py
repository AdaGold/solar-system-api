from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, feature=None):
        self.id = id
        self.name = name
        self.description = description
        self.feature = feature if feature is not None else ''
        

planets =[
    Planet(1, "Mercury", "Mercury is the smallest planet in our solar system."),
    Planet(2, "Venus", "Venus is the second planet from the Sun."),
    Planet(3, "Earth", "Earth is an ellipsoid with a circumference of about 40,000 km. It is the densest planet in the Solar System. ")
    
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