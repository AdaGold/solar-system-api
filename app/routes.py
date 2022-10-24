from crypt import methods
from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, description, rings):
        self.id = id
        self.name = name
        self.description = description
        self.rings = rings

planets = [
        Planet(1, "Mercury", "The smallest and fastest planet", False),
        Planet(2, "Venus", "The hottest planet", False),
        Planet(3, "Earth", "The blue marble", False),
        Planet(4, "Mars", "The red planet", False),
        Planet(5, "Jupiter", "The gas giant", False),
        Planet(6, "Saturn", "The second largest planet", True),
        Planet(7, "Uranus", "This planet spins on its side", True),
        Planet(8, "Neptune", "The most distant planet from the sun", False)
        ]

bp = Blueprint("planets", __name__, url_prefix="/planets")

@bp.route("", methods=["GET"])
def handle_planets():
    return_body = []
    for planet in planets:
        return_body.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "rings": planet.rings
        })
    
    return jsonify(return_body)

@bp.route("/<id>", methods=["GET"])
def handle_planet(id):
    try:
        planet_id = int(id)
    except:
        abort(400, description=f"planet {id} is not valid")
    
    for planet in planets:
        if planet.id == planet_id:
            return jsonify({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "rings": planet.rings
            })
    
    abort(404, description=f"Planet {id} not found")

