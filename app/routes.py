from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons

planets = [
    Planet(1, "Mercury", "the smallest planet in our solar system and closest \
        to the Sun", 0),
    Planet(2, "Venus","Venus spins slowly in the opposite direction from most \
        planets. A thick atmosphere traps heat in a runaway greenhouse effect, \
        making it the hottest planet in our solar system.", 0),
    Planet(3, "Earth"," It's also the only planet in our solar system with liquid \
        water on the surface.", 1),
    Planet(4, "Mars","Mars is a dusty, cold, desert world with a very thin \
        atmosphere.", 2),
    Planet(5, "Jupiter","Jupiter is more than twice as massive than the other \
        planets of our solar system combined.", 79),
    Planet(6, "Saturn", "Adorned with a dazzling, complex system of icy rings, \
        Saturn is unique in our solar system.", 62),
    Planet(7, "Uranus", "Uranus rotates at a nearly 90-degree angle from the plane of its \
        orbit. This unique tilt makes Uranus appear to spin on its side.", 27),
    Planet(8, "Neptune", "Neptune is dark, cold and whipped by supersonic winds.", \
        14)

]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "moons": planet.moons
        })
    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    try:
        planet_id = int(planet_id)
        for planet in planets:
            if planet.id == planet_id:
                return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "moons": planet.moons
                }
    except:
        return "Invalid planet id. Please enter a number", 404
    return "We do not have a planet with that id", 404