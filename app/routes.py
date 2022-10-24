
from flask import Blueprint, jsonify

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
    
planets = [
    Planet(1, "Mercury", "The smallest planet in our solar system and nearest to the Sun,\
        Mercury is only slightly larger than Earth's Moon."),
    Planet(2, "Earth", "Our home planet is the third planet from the Sun, and the only place we know of so far\
        that is inhabited by living things."),
    Planet(3, "Venus", "Venus is the second planet from the Sun and is Earths closest planetary neighbor."),
    Planet(4, "Mars", "Mars is the fourth planet from the Sun, a dusty, cold, desert world with a very thin atmosphere."),
    Planet(5, "Jupiter", "Fifth in line from the Sun, Jupiter is, by far, the largest planet in the solar system\
        more than twice as massive as all the other planets combined."),
    Planet(6, "Saturn", "Saturn is the sixth planet from the Sun and the second-largest planet in our solar system."),
    Planet(7, "Uranus", "Uranus is the seventh planet from the Sun, and has the third-largest diameter in our solar system."),
    Planet(8, "Neptune", "Dark, cold, and whipped by supersonic winds, ice giant Neptune is the eighth and most distant\
        planet in our solar system."),
    ]

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planets_response = [{"id": planet.id, "name": planet.name, "description": planet.description} for planet in planets]

    return jsonify(planets_response)

@planets_bp.route('<planet_id>',methods=["GET"])    
def get_one_planet(planet_id):
    planet_id = int(planet_id)
    for planet in planets:
        if planet.id == planet_id:
            return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description
            }
    