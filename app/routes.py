from crypt import methods
from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, color, description):
        self.id = id
        self.name = name
        self.color = color
        self.description = description

    def to_dict(self):
        return dict(
                id=self.id,
                name=self.name,
                color=self.color,
                personality=self.description,)
        

bp = Blueprint("planets", __name__, url_prefix="/planets")

@bp.route("", methods=["GET"])
def index_planets():
    result_list = [planet.to_dict() for planet in planets]

    return jsonify(result_list) 


planets = [
    Planet(1, "Pluto", "blue", "dwarf-sized"),
    Planet(2, "Saturn", "yellow", "2nd largest planet"),
    Planet(3, "Jupiter", "red-orange", "largest planet")
]

@bp.route("/<id>", methods=["GET"])
def get_planet_id(id):
    try:

        id = int(id)
    
    except:
        return "Bad data, 400"

    for planet in planets:
        if planet.id == id:
            return planet.to_dict()
    return "Not found", 404