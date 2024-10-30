from flask import Blueprint, abort, make_response, request, Response
from app.models.planets import Planet
from ..db import db

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planet_bp.post("")
def create_planet():
    request_body = request.get_json()
   
    name = request_body["name"]
    description = request_body["description"]
    diameter = request_body["diameter"]
    number_of_moons = request_body["number_of_moons"]
    
    new_planet = Planet(name=name, description=description, diameter=diameter, number_of_moons=number_of_moons)
    db.session.add(new_planet)
    db.session.commit()
    
    response = new_planet.to_dict()
    return response, 201
    
@planet_bp.get("")
def get_all_planets():
    query = db.select(Planet)
    
    description_param = request.args.get("description")
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))
    
    number_of_moons_param = request.args.get("number_of_moons")
    if number_of_moons_param:
        query = query.where(Planet.number_of_moons == number_of_moons_param)
        
    query = query.order_by(Planet.id)
    
    planets = db.session.scalars(query)
    
    response_body = [planet.to_dict() for planet in planets]
    
    return response_body 

@planet_bp.get("/<planet_id>")
def get_single_planet(planet_id):
    planet = validate_planet(planet_id)

    return planet.to_dict()

@planet_bp.put("/<planet_id>")
def update_single_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.diameter = request_body["diameter"]
    planet.number_of_moons = request_body["number_of_moons"]

    db.session.commit()

    return Response(status=204, mimetype='application/json')

@planet_bp.delete("/<planet_id>")
def delete_single_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype='application/json')


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        response = {
            "message": f"Planet {planet_id} invalid"
        }
        abort(make_response(response, 400))

    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.scalar(query)

    if not planet:
        response = {
            "message": f"Planet {planet_id} not found"
        }
        abort(make_response(response, 404))

    return planet 
 
        
