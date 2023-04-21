from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        color = color
planets = [
    Planet(1, "Mercury", "1st planet from the Sun", "light blue"),
    Planet(2, "Venus", "2nd planet from the Sun", "orange"),
    Planet(3, "Earth", "3rd planet from the Sun", "black"),
    Planet(4, "Mars", "4th planet from the Sun", "red"),
    Planet(5, "Jupiter", "5th planet from the Sun", "green"),
    Planet(6, "Saturn", "6th planet from the Sun", "purple"),
    Planet(7, "Uranus", "7th planet from the Sun", "dark blue"),
    Planet(8, "Neptune", "8th planet from the Sun", "aqua"),
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def handle_planets():
    result_list = []
    for planet in planets:
        result_list.append(dict(
            id=planet.id,
            name=planet.name,
            description=planet.description,
            color=planet.color,
        ))
    return jsonify(result_list)