from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, distance_from_sun_in_million_mi, moon_count):
        self.id = id
        self.name = name
        self.description = description
        self.distance_from_sun_in_million_mi = distance_from_sun_in_million_mi
        self.moon_count = moon_count
        

planets = [
    Planet(1, "Mercury", "The smallest and fastest", "35.98", "0"),
    Planet(2, "Venus", "The hottest in our solar system", "67.24", "0"),
    Planet(3, "Earth", "Our planet; the only planet with living things and liquid water", "92.96", "1"),
    Planet(4, "Mars", "In spite of being red, it is a very cold planet", "141.6", "2"),
    Planet(5, "Jupiter","The largest planet in our solar system", "483.8", "79 (53 Confirmed)"),
    Planet(6, "Saturn", "The only planet with rings around it.", "890.8", "82 (53 Confirmed)"),
    Planet(7, "Uranus", "This planet rotates at a 90° degree angle.", "1784", "27"),
    Planet(8, "Neptune", "The furthest planet; dark and cold with supersonic winds.", "2793", "14")
]



planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def handle_planets():
    planets_response = []
    for planet in planets: 
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "distance_from_sun_in_million_mi": planet.distance_from_sun_in_million_mi,
                "moon_count": planet.moon_count,
            }
        )
    return planets_response
    # return jsonify(planets_response)


@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    for planet in planets: 
        if planet.id == int(planet_id):
            return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "distance_from_sun_in_million_mi": planet.distance_from_sun_in_million_mi,
                "moon_count": planet.moon_count,
            }



            