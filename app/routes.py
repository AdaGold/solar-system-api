from flask import Blueprint

class Planet:
    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons 

planets = [
    Planet(1, "Mercury", "Smallest planet", "None"),
    Planet(2,"Venus", "Second planet from sun","None"),
    Planet(3, "Jupiter", "Gas giant", "53")
    ]
planets_bp = Blueprint("planets", __name__,url_prefix="/planets")

@planets_bp.route("", methods = ["GET"])
def get_planets():
    planet_response = []
    for planet in planets:
        planet_response.append({
            "id" : planet.id,
            "name" : planet.name,
            "description" : planet.description,
            "color" : planet.color,
        })
    return jsonify(planet_response)
@planets_bp.route("/<planet_id>", methods = ["GET"])
def get_single_planet(planet_id):
    given_planet_id = int(planet_id)
    for planet in planets:
        if planet.id == given_planet_id:
            return {
                "id" : planet.id,
                "name" : planet.name,
                "description" : planet.description,
                "moons" : planet.color,
                }