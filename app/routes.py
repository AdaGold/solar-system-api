from flask import Blueprint, jsonify, abort, make_response


class Planets: 
    def __init__(self, id, name, description, gravity): 
        self.id = id
        self.name = name 
        self.description = description 
        self.gravity = gravity 
    
planets = [
    Planets(1, "Mercury", "The smallest planet in our solar system and nearest to the Sun.", "3.7 m/s^2"),
    Planets(2, "Earth", "The third planet from the Sun", "9.807 m/s^2"),
    Planets(3, "Jupiter", "The largest planet in the solar system", "24.79 m/s^2")
]

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods = ["GET"])
def planets_json():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "gravity":planet.gravity
        })
    return jsonify(planets_response)

#validate planet id and response
def validate_planet(planet_id):
    try:
        book_id = int(book_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

    abort(make_response({"message":f"book {book_id} not found"}, 404))

#Get planet info by valid id
@planets_bp.route("/<planet id>", methods = ["GET"])
def planets_get_by_id(planet_id):
    planet = validate_planet(planet_id)
    return {
        "id": planet.id,
        "title": planet.title,
        "description": planet.description
    }

