from flask import Blueprint, jsonify, request, make_response
from app import db
from app.models.planet import Planet

class Planet:
    def __init__(self, id, name, description, num_of_moons):
        self.id = id 
        self.name = name 
        self.description = description 
        self.num_of_moons = num_of_moons

# planets = [
#     Planet(1, "Mercury", "First planet from the sun", 0),
#     Planet(2, "Venus", "Second planet from the sun", 0),
#     Planet(3, "Earth", "Third planet from the sun", 1),
#     Planet(4, "Mars", "Fourth planet from the sun", 2),
#     Planet(5, "Jupiter", "Fifth planet from the sun", 79)
# ]

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

def make_planet_dict(planet):
    return {
                "id" : planet.id,
                "name" : planet.name,
                "description" : planet.description,
                "num_of_moons" : planet.num_of_moons
            }

@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "GET":
        planets_response = []
        planets = Planet.query.all()
        
        for planet in planets:
            current_planet = make_planet_dict(planet)
            planets_response.append(current_planet)
            
        return jsonify(planets_response) 

    else: 
        request_body = request.get_json()
        new_planet = Planet(
            name = request_body["name"],
            description= request_body["description"],
            num_of_moons=request_body["num_of_moons"]
        )
        db.session.add(new_planet)
        db.session.commit()

        return f"Planet successfully created {new_planet.name}", 201

@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_one_planet(planet_id):
    planet_response = jsonify("Not a valid planet")

    for planet in planets:
        if planet.id == int(planet_id):
            planet_response = make_planet_dict(planet)

    return planet_response