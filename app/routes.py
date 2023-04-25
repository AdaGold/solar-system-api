from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, num_moons):
        self.id = id
        self.name = name
        self.description = description
        self.num_moons = num_moons

planets = [
    Planet(1,"mercury", "terrestrial",0),
    Planet(2,"venus", "terrestrial",0),
    Planet(3,"earth", "terrestrial",1),
    Planet(4,"mars", "terrestrial",2),
    Planet(5,"jupiter", "gas giant",95),
    Planet(6,"mercury", "gas giant",83),
    Planet(7,"uranus", "ice giant",27),
    Planet(8,"neptune", "ice giant",14)
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def handle_planets():
    results = []

    for planet in planets:
        results.append(dict(
            id=planet.id,
            name=planet.name,
            description=planet.description,
            num_moons=planet.num_moons
        ))

    return jsonify(results)




