from crypt import methods
from flask import Blueprint, jsonify
class Planet:
    def __init__(self, id, name, description, size):
        self.id = id
        self.name = name
        self.description = description
        self.size = size


planets = [
    Planet(1, "Mars", "Red", 2106), 
    Planet(2, "Earth", "Blue", 3958),
    Planet(3, "Mercury", "Grey", 1500)
]

planet_bp = Blueprint("planet_bp", __name__, url_prefix = "/planets")


#this is the decorator that saying when a request matches turn this function into url
@planet_bp.route("", methods = ["GET"])
#need to create function here 

def all_planets():
    planet_data = []
    for planet in planets:
        planet_data.append({
            "id": planet.id, "name": planet.name, "description": planet.description, "size": planet.size

        })
    return jsonify(planet_data)

@planet_bp.route("/<planet_id>", methods = ["GET"])

def planet_info(planet_id):
    try: 
        planet = int(planet_id)
    except:
        {"message": f'planet_id {planet_id} is in valid'}, 400

    for planet in planets:
        if planet.id == planet_id:
            return {"id": planet.id, "name": planet.name, "description": planet.description, "size": planet.size}