from flask import Blueprint, jsonify, abort, make_response

class Planet():
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color

planets = [
    Planet(1, "Mercury", "the closest to the Sun", "orange"),
    Planet(2, "Venus", "toxic atmosphere and yellowish clouds", "brown"),
    Planet(3, "Earth", "ocean planet", "blue"),
    Planet(4, "Mars", "small red, cold and dusty planet", "red"),
    Planet(5, "Jupiter", "covered in cloudy stripes", "light blue with brown stripes"),
    Planet(6, "Saturn", "has seven rings around its body", "beige"),
    Planet(7, "Uranus", "made of water", "baby blue"),
    Planet(8, "Neptune", "dark and very windy", "sky blue")
    ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")



@planets_bp.route("", methods=["Get"])
def get_all_planets():
    result = []
    for planet in planets:
        result.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "color": planet.color
        })

    return jsonify(result)

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return jsonify({
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "color": planet.color
    }), 200  

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

    abort(make_response({"message":f"planet {planet_id} not found"}, 404))