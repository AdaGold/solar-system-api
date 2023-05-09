from app import db
from app.models.moon import Moon
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request
from .routes_helpers import validate_model

moon_bp = Blueprint("moons", __name__, url_prefix="/moons")


# CREATE ENDPOINT
@moon_bp.route("",methods=["POST"])
def create_moon():
    request_body = request.get_json()
    new_moon = Moon.from_dict(request_body)

    db.session.add(new_moon)
    db.session.commit()

    return make_response(f"Moon {new_moon.name} successfully created", 201)

@moon_bp.route("/<moon_id>/planets", methods=["POST"])
def create_planet(moon_id):
    moon = Planet.query.get(moon_id)
    
    request_body = request.get_json()

    new_planet = Planet.from_dict(request_body, moon)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created with Moon {moon.name}", 201)

# GET ONE ENDPOINT
@moon_bp.route("/<moon_id>", methods=["GET"])
def read_one_moon(moon_id):
    moon = validate_model(Moon,moon_id)

    return jsonify(moon.to_dict()), 200

# GET ALL PLANETS BY MOON ENDPOINT
@moon_bp.route("/<moon_id>/planets", methods=["GET"])
def handle_planets_from_moon(moon_id):
    moon = validate_model(Moon, moon_id)

    planets_response = []
    for planet in moon.planets:
        planets_response.append(planet.to_dict())

    return jsonify(planets_response), 200  