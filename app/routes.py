from flask import Blueprint, jsonify, request, make_response
from app.Model.planet import Planet
from app import db

# class Planet():
#     def __init__(self, id, name, description, mythology):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.mythology = mythology 

# planet_instances = [
#     Planet(1, "Mercury", "First planet in the solar system", "God of financial gain"),
#     Planet(2, "Venus", "Second planet in our solar system", "Goddess of love"),
#     Planet(3, "Earth", "Third planet in our solar system", "God of land"),
#     Planet(4, "Mars", "Fourth planet in our solar system", "God of war"),
#     Planet(5, "Saturn", "Fifth planet in our solar system", "God of quite a few things"),
#     Planet(6, "Jupiter", "Sixth planet in our solar system", "God of sky and thunder"),
#     Planet(7, "Uranus", "Seventh planet in our solar system", "God of sky"),
#     Planet(8, "Neptune", "Eighth planet, in our solar system", "God of the oceans"),
#     Planet(9, "Not Pluto", "Not quite a planet", "God of disillusuinment")
# ]






planets_bp = Blueprint("planets", __name__, url_prefix ="/planets")

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planets = Planet.query.all()
    planet_response = []
    for each_planet in planets:
        planet_response.append({
            "id": each_planet.id,
            "name": each_planet.name,
            "description": each_planet.description,
            "mythology": each_planet.mythology,
        }   
        )
    return jsonify(planet_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_single_planet(planet_id):
    planet = Planet.query.get(planet_id)
        return jsonify({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "mythology": planet.mythology,
        })
