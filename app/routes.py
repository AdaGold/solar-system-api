from flask import Blueprint

class Planet:
    def __init__(self, id, name, description, num_of_moons):
        self.id = id 
        self.name = name 
        self.description = description 
        self.num_of_moons = num_of_moons

planets = [
    Planet(1, "Mercury", "First planet from the sun", 0),
    Planet(2, "Venus", "Second planet from the sun", 0),
    Planet(3, "Earth", "Third planet from the sun", 1),
    Planet(4, "Mars", "Fourth planet from the sun", 2),
    Planet(5, "Jupiter", "Fifth planet from the sun", 79)
]

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def handle_planets():
    planets_response = []
    
    for planet in planets:
        planets_response.append(
            {
                "id" : planet.id,
                "name" : planet.name,
                "description" : planet.description,
                "num_of_moons" : planet.num_of_moons
            }
        ) 

    return jsonify(planets_response) 