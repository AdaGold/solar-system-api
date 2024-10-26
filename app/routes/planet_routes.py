from flask import Blueprint, abort, make_response, request
from app.models.planet import Planet
from app.db import db
from sqlalchemy import select

planets_bp = Blueprint("planets_bp", __name__, url_prefix=("/planets"))


@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body['name']
    description = request_body['description']

    new_planet = Planet(name=name, description=description)
    db.session.add(new_planet)
    db.session.commit()

    response_body = new_planet.to_dict()

    return response_body, 201

@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)

    response_body=[]
    for planet in planets:
        response_body.append(planet.to_dict())
    
    return response_body, 200

@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.scalar(query)

    return planet.to_dict(), 200


# Helper Functions




