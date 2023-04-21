from flask import Blueprint, jsonify

class Planet:

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    
planets = [
    Planet(1, "Mercury", "The Morning star"),
    Planet(2, "Venus", "The Evening star"),
    Planet(3, "Mars", "The Red planet"),
    Planet(4, "Earth", "The Blue Planet"),
    Planet(5, "Jupiter", "The Giant Planet"),
    Planet(6, "Saturn", "The Ringed Planet"),
    Planet(7, "Uranus", "The Ice Giant"),
    Planet(8, "Neptune", "Big Blue"),
    Planet(9, "Pluto", "The Minor Planet")
    ]

bp = Blueprint("planets", __name__, url_prefix="/planets")

@bp.route("", methods=["GET"])
def handle_planets():
    results = []
    for planet in planets:
        results.append(dict(
            id=planet.id,
            name=planet.name,
            description=planet.description
        ))

    return jsonify(results)