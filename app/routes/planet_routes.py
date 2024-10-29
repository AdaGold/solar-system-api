from flask import Blueprint, abort, make_response, request, Response
from app.db import db 
from app.models.planet import Planet

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()

    name = request_body["name"]
    description = request_body["description"]
    number_of_moons = request_body["number_of_moons"]
    new_planet = Planet(name=name, description=description, number_of_moons=number_of_moons)

    db.session.add(new_planet)
    db.session.commit()

    return new_planet.to_dict(), 201

@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)

    return [planet.to_dict() for planet in planets]

@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    return validate_planet(planet_id).to_dict()

@planets_bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.number_of_moons = request_body["number_of_moons"]

    db.session.commit()

    return Response(status=204, mimetype='application/json')

@planets_bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype='application/json')

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        abort(make_response({"message": f"planet {planet_id} invalid"}, 400))

    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.scalar(query)

    if not planet:
        abort(make_response({"message": f"planet {planet_id} not found"}, 404))
    
    return planet