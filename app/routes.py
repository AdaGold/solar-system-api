from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, radius_size):
        self.id = id
        self.name = name
        self.description = description
        self.radius_size = radius_size

planets = [
    Planet(1, "Jupiter", "The fifth planet from our Sun and is the largest planet in the solar system.","43,441 mi"),
    Planet(2, "Saturn", "The most distant planet that can be seen with the naked eye.", "36,184 mi" ),
    Planet(3, "Mars", "The fourth planet from the Sun and is a dusty, cold, desert world with a very thin atmosphere", "2,10.61 mi")
] 

planets_bp = Blueprint('planets', __name__, url_prefix='/planets')

@planets_bp.route('', methods=["GET"])
def get_planets():
    planets_response =[]
    for planet in planets:
        planets_response.append({
            'id':planet.id,
            'name':planet.name,
            'description':planet.description,
            'radius_size':planet.radius_size
        })
    return jsonify(planets_response)

@planets_bp.route('/<planet_id>', methods=['GET'])
def get_specific_planet(planet_id):
    planet_id=int(planet_id)
    for planet in planets:
        if planet.id ==planet_id:
            return {
            'id':planet.id,
            'name':planet.name,
            'description':planet.description,
            'radius_size':planet.radius_size
            }