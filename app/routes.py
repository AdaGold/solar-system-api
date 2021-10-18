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
        planets of our solar system combined.", 79)
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