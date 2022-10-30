from flask import Blueprint, jsonify, make_response, request
from app.models.planet import Planet
from app import db

bp = Blueprint("planets", __name__, url_prefix="/planets")

@bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        rings=request_body["rings"])
    
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} created", 201)

@bp.route("", methods=["GET"])
def get_all_planets():
    planets = Planet.query.all()
    planets_response = []
    for planet in planets:
        planets_response.append(planet.build_planet_dict())

    return jsonify(planets_response)

@bp.route("/<id>", methods=["GET"])
def get_planet(id):
    planets = Planet.query.all()
    for planet in planets:
        if planet.id == int(id):
            return jsonify(planet.build_planet_dict())
    
    return make_response(f"Planet {id} not found", 404)