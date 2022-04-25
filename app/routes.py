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
def get_planet_id():
    id = int(id)

    for planet in index_planets:
        if planet.id == id:
            jsonify(dict(
            id=planet.id,
            name=planet.name,
            color=planet.color,
            personality=planet.description,

            ))