from flask import Blueprint
from flask import Blueprint, jsonify

class Planet():
    def __init__(self, id, name, description, mythology):
        self.id = id
        self.name = name
        self.description = description
        self.mythology = mythology 

planet_instances = [
    Planet(1, "Mercury", "First planet in the solar system", "God of financial gain"),
    Planet(2, "Venus", "Second planet in our solar system", "Goddess of love"),
    Planet(3, "Earth", "Third planet in our solar system", "God of land"),
    Planet(4, "Mars", "Fourth planet in our solar system", "God of war"),
    Planet(5, "Saturn", "Fifth planet in our solar system", "God of quite a few things"),
    Planet(6, "Jupiter", "Sixth planet in our solar system", "God of sky and thunder"),
    Planet(7, "Uranus", "Seventh planet in our solar system", "God of sky"),
    Planet(8, "Neptune", "Eighth planet, in our solar system", "God of the oceans"),
    Planet(9, "Not Pluto", "Not quite a planet", "God of disillusuinment")
]

planets_bp = Blueprint("planets", __name__, url_prefix ="/planets")

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planet = []
    for each_planet in planet_instances:
        planet.append({
            "id": each_planet.id,
            "name": each_planet.name,
            "description": each_planet.description,
            "mythology": each_planet.mythology,
        }   
        )
    return jsonify(planet)

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_single_planet(planet_id):
    planet_id = int(planet_id)
    for each_planet in planet_instances:
        if each_planet.id == planet_id:
            return {
                "id": each_planet.id,
                "name": each_planet.name,
                "description": each_planet.description,
                "mythology": each_planet.mythology,
            }
