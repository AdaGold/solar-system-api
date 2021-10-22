from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request
'''
class Planet:
    def __init__(self, id, name, description, cycle_len):
        self.id=id
        self.name=name
        self.description=description
        self.cycle_len=cycle_len # days

planets = [
    Planet(1, "Earth", "blue marble", 365),
    Planet(2, "Saturn", "ringed planet", 10220),
    Planet(3, "Mars", "musty, dusty and cold", 780),
    Planet(4, "Mercury", "teeny tiny", 88)
]

'''
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "cycle length (days)": planet.cycle_len
            })
        return jsonify(planets_response)
    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name = request_body["name"], 
                        description = request_body["description"], 
                        cycle_len = request_body["cycle_len"])
        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} successfully created", 201)
@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet_id = int(planet_id)
    for planet in planets:
        if planet.id == planet_id:
            return {"id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "cycle length (days)": planet.cycle_len}
