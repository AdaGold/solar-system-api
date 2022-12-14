from flask import Blueprint, jsonify
from .moon import moons_list
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")
moons_bp = Blueprint("moons", __name__, url_prefix="/moons")

@planets_bp.route("", methods=["GET"])
def display_planets():
    return "Test Planets"


@planets_bp.route("/<planet_id>", methods=["GET"])
def display_planet(planet_id):
    pass

@moons_bp.route("", methods=["GET"])
def get_all_moons():
    moons_response = []
    for moon in moons_list:
        moons_response.append({
            "id":moon.id,
            "name": moon.name,
            "description": moon.description
        })
    return jsonify(moons_response)



    


    

    

