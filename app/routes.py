from crypt import methods
from flask import Blueprint
import json
class Planet:
    def __init__(self, id, name, color, description):
        self.id = id
        self.name = name
        self.color = color
        self.description = description

def to_dict(self):
    return dict(
            id=Planet.id,
            name=planet.name,
            color=planet.color,
            personality=planet.description,)
        


solar_bp = Blueprint("solar-system", __name__)

bp = Blueprint("planets", __name__, url_prefix="/planets")

def index_planets():
    result_list = [dict(
            id=planet.id,
            name=planet.name,
            color=planet.color,
            personality=planet.description,
        ) for planet in index_planets]

    return jsonify(result_list) 

#@solar_bp.route("/solar-system", methods=["GET"])

solar_system_list = [
    
    { "id": "1",
    "name": "pluto",
    "description": "dwarf-sized"
    } ,

    { "id" : "2",
    "name" : "saturn",
    "description" : "2nd largest planet"
    },

    { "id" : "3",
    "name" : "jupiter"
    "description" : "largest planet"
    }

    
        ]

@solar_bp.route("/<id>", methods=["GET"])
def get_planet_id():
    id = int(id)

    for planet in index_planets:
        if planet.id == id:
            jasonify(dict(
            id=planet.id,
            name=planet.name,
            color=planet.color,
            personality=planet.description,

            ))