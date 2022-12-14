from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, gravity,description):
        self.id = id
        self.name = name
        self.gravity = gravity
        self.description = description

planets = [
    Planet(1,"Mars","","Mars is the fourth planet from the Sun. A dusty, cold, desert world with a very thin atmosphere.")
]       
planets_bp = Blueprint("planets", __name__)

@planets_bp.route("/planets", methods = ["GET"])
def planet_json():
    response_body = []