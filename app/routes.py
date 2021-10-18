from flask import Blueprint, jsonify
from .planets_class import Planet
from .load_json import load
import pprint

# loads json data as dictionaries
planet_data = load('app/planets.json')
satellite_data = load('app/satellites.json')

# pprint.pprint(planet_data, sort_dicts=False)
# pprint.pprint(satellite_data, sort_dicts=False)

def make_planet_objects():
    planets_list = []

    for planet in planet_data:
        description = f'{planet["name"]} is the {planet["id"]} planet and has {planet["numberOfMoons"]} moon(s).'
        planet_object = Planet(planet["id"], planet["name"], description, planet["numberOfMoons"])
        planets_list.append(planet_object)

    return planets_list

planets = make_planet_objects()

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("/", methods=["GET"])
def handle_planets():
    planets_response = []
    
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "num_of_moons": planet.num_of_moons
            })
    return jsonify(planets_response)


@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet_id = int(planet_id)

    planet_response = {}

    for planet in planets:
        if planet_id == planet.id:
            planet_response["id"] = planet.id
            planet_response["name"] = planet.name
            planet_response["description"] = planet.description
            planet_response["num_of_moons"] = planet.num_of_moons
            
    return jsonify(planet_response)