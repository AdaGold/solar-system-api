from flask import Blueprint

class Planet:
    def __init__(self, id, name, description, size):
        self.id = id
        self.name = name
        self.description = description
        self.size = size


planets = [
    Planet(1, "Mars", "Red", 2106), 
    Planet(2, "Earth", "Blue", 3958),
    Planet(3, "Mercury", "Grey", 1500)
]

planet_bp = Blueprint("planets", __name__)


#this is the decorator that saying when a request matches turn this function into url
@planet_bp.route("/planets", method = ["GET"])
#need to create function here 