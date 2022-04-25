from flask import Blueprint, jsonify




class Planet:
    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons

planets = [
    Planet(1, "Mercury", "Mercury is the first planet from the Sun. It is the smallest and the fastest of all planets in our Solar system",0),
    Planet(2, "Venus", "Venus is the second planet from the Sun. It spins clockwise on its axis and is the second brightest natural object in the night sky after the Moon", 0),
    Planet(3, "Earth", "Third planet from the Sun and our home planet is 4.5 billion years old. The only planet to sustain a liquid surface area", 1),
    Planet(4, "Mars", "This planet is named after Mars, the Roman god of war. It's landmass which is similar to Earth, has a reddish-brown color.", 2),
    Planet(5, "Jupiter", "Jupiter is the largest of all planets in our Solar system. This gaseous planet is more than twice as large as the other planets combined", 79),
    Planet(6, "Saturn", "Saturn is the second largest of the planets and is primarily composed of hydrogen gas. It is known for its over 30 stunning Rings of ice", 82),
    Planet(7, "Uranus", "This ice giant is massive with a size four times wider than of Earth. It has 13 known Rings", 27),
    Planet(8, "Neptune", "At a distance of 2.8 billion miles from the Sun, this massive planet is four times wider than Earth. It's mainly made up of icy materials- water, methane and ammonia with 7 Rings", 14),
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")						
						
@planets_bp.route("", methods=["GET"])						
def get_planets():						
    planets_response = []						
    for planet in planets:						
        planets_response.append({					
        "id": planet.id,					
        "title": planet.name,					
        "description": planet.description,
        "moons": planet.moons						
    })						
    return jsonify(planets_response)						