from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color

planets = [
    Planet(1, "Mars", "Round,Big", "Red"), 
    Planet(2,"Saturn","Round,Big", "Yellow"),Planet(3, "Jupiter","Round,Big", "Blue")
    ]

planets_bp = Blueprint("planets",__name__,url_prefix="/planets")

@planets_bp.route("", methods = ["GET"])
def get_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id" : planet.id,
            "name" : planet.name, 
            "description" : planet.description,
            "color" : planet.color
        })
    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods = ["GET"])
def get_single_planet(planet_id):
    planet_repsonse = []
    planet_id = int(planet_id)
    for planet in planets:
        if planet.id == planet_id:
            return {
                "id" : planet.id,
                "name" : planet.name,
                "description" : planet.description,
                "color" : planet.color
            }
