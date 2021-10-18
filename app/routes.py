from flask import Blueprint, jsonify


planets_bp = Blueprint("planets", __name__)

class Planet:
    def __init__(self, name, id, type, description, moons) -> None:
        self.name = name
        self.id = id
        self.type = type
        self.description = description
        self.moons = moons


planet_1= Planet("Mercury", 1, "Rocky", "Mercury is the closest planet to the sun and the eighth largest. It has a diameter of 4,880 kilometers. ", "1 Moon")
planet_2= Planet("Venus", 2, "Terrestrial","Venus is the second planet from the Sun. It is named after the Roman goddess of love and beauty.", "13 Moons")


planet_lst=[planet_1,planet_2]
@planets_bp.route("/planets", methods =["GET"])

def handle_planets():
    planets_response=[]
    for planet in planet_lst:
        planets_response.append({"id": planet.id, 
        "name": planet.name,
        "type": planet.type,
        "description": planet.description,
        "moons": planet.moons})
    return jsonify(planets_response)