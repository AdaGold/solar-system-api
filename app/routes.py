from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, title, description, color):
        self.id = id
        self.title = title
        self.description = description
        self.color = color

planets = [
    Planet(1, "Neptune", "ice giant", "azure blue"),
    Planet(2, "Saturn", "has rings", "yellow-brown"),
    Planet(3, "Earth", "home planet", "blue"), 
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])

def get_planet_info():
    planet_responses = []
    for planet in planets:
        planet_responses.append(
            {
                "id": planet.id,
                "title": planet.title,
                "description": planet.description,
                "color": planet.color
            }
        )
    return jsonify(planet_responses)

@planets_bp.route("/<planet_id>", methods=["GET"])

def get_planet_id(planet_id):
    planet_id = int(planet_id)
    for planet in planets:
        if planet_id == planet_id:
            planet_response = {
                "id": planet.id,
                "title": planet.title,
                "description": planet.description,
                "color": planet.color
            }
    return planet_response
     




