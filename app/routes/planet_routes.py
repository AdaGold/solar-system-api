from flask import Blueprint, abort, make_response, request
from app.models.planet import Planet
from ..db import db

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.get("")
def get_all_planets():
    description = request.args.get("description")
    max_distance = request.args.get("max_distance")
    min_distance = request.args.get("min_distance")

    query = db.select(Planet)

    if description:
        query = query.where(Planet.description.ilike(f"%{description}%"))

    if max_distance is not None:
        query = query.where(Planet.distance_from_sun <= max_distance)

    if min_distance is not None:
        query = query.where(Planet.distance_from_sun >= min_distance)

    query = query.order_by(Planet.id)
    planets = db.session.execute(query).scalars()

    planets_response = []

    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "distance_from_sun": planet.distance_from_sun
            }
        )

    return planets_response


@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return {"message": f"planet {planet_id} invalid"}, 400

    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.execute(query).scalar_one_or_none()

    if planet:
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "distance_from_sun": planet.distance_from_sun
        }

    return {"message": f"planet {planet_id} not found"}, 404

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()

    required_fields = ("name", "description", "distance_from_sun")
    
    if not isinstance(request_body, dict):
        return {"message": "Expected a JSON object"}, 400

    for field in required_fields:
        if field not in request_body:
            return {"message": f"Missing field: {field}"}, 400
    
    name = request_body["name"]
    description = request_body["description"]
    distance_from_sun = request_body["distance_from_sun"]

    new_planet = Planet(name=name, description=description, distance_from_sun=distance_from_sun)
    db.session.add(new_planet)
    db.session.commit()

    response = {
        "id": new_planet.id,
        "name": new_planet.name,
        "description": new_planet.description,
        "distance_from_sun": new_planet.distance_from_sun
    }

    return response, 201


@planets_bp.put("/<planet_id>")
def update_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return {"message": f"planet {planet_id} invalid"}, 400

    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.execute(query).scalar_one_or_none()

    if planet:
        request_body = request.get_json()
        required_fields = ("name", "description", "distance_from_sun")
            
        if not isinstance(request_body, dict):
            return {"message": "Expected a JSON object"}, 400
        
        for field in required_fields:
            if field not in request_body:
                return {"message": f"Missing field: {field}"}, 400
            
        name = request_body["name"]
        description = request_body["description"]
        distance_from_sun = request_body["distance_from_sun"]

        planet.name = name
        planet.description = description
        planet.distance_from_sun = distance_from_sun

        db.session.commit()

        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "distance_from_sun": planet.distance_from_sun
        }, 200

    return {"message": f"planet {planet_id} not found"}, 404


@planets_bp.delete("/<planet_id>")
def delete_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return {"message": f"planet {planet_id} invalid"}, 400

    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.execute(query).scalar_one_or_none()

    if planet:
        db.session.delete(planet)
        db.session.commit()

        return {"message": f"planet {planet_id} deleted successfully"}, 200

    return {"message": f"planet {planet_id} not found"}, 404