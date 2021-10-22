from flask import Blueprint

class Planet:
    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons 

planets = [
    Planet(1, "Mercury", "Smallest planet", "None"),
    Planet(2,"Venus", "Second planet from sun","None"),
    Planet(3, "Jupiter", "Gas giant", "53")
    ]
planets_bp = Blueprint("planets", __name__,url_prefix="/planets")