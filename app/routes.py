from flask import Blueprint, jsonify
import requests

class Planet:
    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons

planets =  [
    Planet(1, "Mercury", "Mercury is hot, but not too hot for ice", 0),
    Planet(2, "Mercury", "Venus doesn’t have any moons, and we aren’t sure why", 0),
    Planet(3, "Earth", "Best planet ever!", 1),
    Planet(4, "Mars", "Mars has two moons named in Latin that translate to fear and panic", 2),
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def all_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id" : planet.id,
            "name" : planet.name,
            "description" : planet.description,
            "moons" : planet.moons
        })
    return jsonify(planets_response)

@planets_bp.route("/category_planets", methods=["GET"])
def get_category_planets(): 
    path = "https://api.le-systeme-solaire.net/rest.php/bodies"

    query_params = {
        "filter[]": "isPlanet,neq,false",
        "data": "id,englishName,isPlanet"
    }

    response = requests.get(path, params=query_params)

    return response.json()
    
@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet_id = int(planet_id)
    for planet in planets:
        if planet.id == planet_id:
            return {
               "id" : planet.id,
                "name" : planet.name,
                "description" : planet.description,
                "moons" : planet.moons
            }



    # print("The value of response is", response)
    # print("The value of response.text, which contains a text description of the request, is", response.text)

