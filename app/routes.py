from flask import Blueprint, jsonify
from app.models.planet import Planet
from app import db

class Planets:
    def __init__(self, id, name, description, proximity):
        self.id = id
        self.name = name
        self.description = description 
        self.proximity = proximity
        
planets = [
    Planets(1, "Mercury", "it is the smallest and fastest planet", "35.98 million miles from the Sun"),
    Planets(2, "Venus", "spins slowly in opposite direction, hottest planet because of its thick atmosphere", "67.24 million miles from the Sun"),
    Planets(3, "Earth", "is the only planet inhabited by living things (that we know of). Humans are ruining it", "92.96 millio miles from the Sun"),
    Planets(4, "Mars", "is dusty, cold dessert with thin atmosphere", "141.6 million miles from the Sun"),
    Planets(5, "Jupiter", "It is the biggest planet. Its Great red spot is a storm bigger than Earth", "483.8 million miles from the Sun"),
    Planets(6, "Saturn", "It is the second largest planet. It has icy rings. made mostly of hydrogen and helium", "890.8 million miles from the Sun"),
    Planets(7, "Uranus", "A day in uranus lasts 17 hours and a year takes 84 Earth days. it has 27 moons", "1.784 billion miles from the Sun"),
    Planets(8, "Neptune", "A day takes 16 hours and a year takes 165 Earth days. Dark, cold and windy", "2.793 billion miles from the Sun")
    ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("/all", methods=["GET"])
def list_all_planets():
    #planets = ["Mercury", "Venus", "Earth", "Mars", \
    #"Jupiter", "Saturn", "Uranus", "Neptune"]
    #return jsonify(planets)

    planets_response = []
    planets = Planet.query.all()
    for planet in planets:
        planets_response.append({
            "id" : planet.id,
            "name" : planet.name,
            "description" : planet.description,
            "proximity" : planet.proximity
        })

    return jsonify(planets), 200

@planets_bp.route("/<id>", methods=["GET"])
def list_one(id):
    for planet in planets:
        if planet.id == int(id):
            response = {
                "id" : planet.id,
                "name" : planet.name,
                "description" : planet.description,
                "proximity" : planet.proximity
            }
            return response
    return "There are only eight planets", 404

