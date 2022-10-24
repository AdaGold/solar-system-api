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

planet_bp = Blueprint("planets", __name__)


#this is the decorator that saying when a request matches turn this function into url
@planet_bp.route("/planets", methods = ["GET"])
#need to create function here 

def all_planets():
    planet_data = []
    for planet in planets:
        planet_data.append({
            "id": planet.id, "name": planet.name, "description": planet.description, "size": planet.size

        })
    return jsonify(planet_data)
