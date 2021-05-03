from app import db
from app.models.planets import Planet
from flask import request, Blueprint, make_response, jsonify

solar_systems_bp = Blueprint("solar_systems", __name__, url_prefix = "/planets")

@solar_systems_bp.route("", methods = ["POST"])

def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name = request_body["name"], description = request_body["description"], size = request_body["size"])

    db.session.add(new_planet)
    db.session.commit()


    return make_response(f"New planet, {new_planet.name} was successfully created.")

@solar_systems_bp.route("", methods = ["GET"])
def get_all_planets():
    planets = Planet.query.all()
    planet_response = []
    for planet in planets:
        planet_response.append({"id": planet.id, "name": planet.name, "description": planet.description, "size": planet.size})

    return jsonify(planet_response)

@solar_systems_bp.route("/<planet_id>", methods = ["GET"])
def get_planet(planet_id):
    planet = Planet.query.get(planet_id)
    
    return jsonify({"id": planet.id, "name": planet.name, "description": planet.description, "size": planet.size})

