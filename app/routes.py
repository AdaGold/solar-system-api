from flask import Blueprint, jsonify

class Planet:

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    
planets = [
    Planet(1, "Mercury", "Smallest"),
    Planet(2, "Venus", "NA"),
    Planet(3, "Mars", "NA"),
    Planet(4, "Earth", "Blue Planet"),
    Planet(5, "Jupiter", "NA"),
    Planet(6, "Saturn", "NA"),
    Planet(7, "Uranus", "NA"),
    Planet(8, "Neptune", "NA"),
    Planet(9, "Pluto", "NA")
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