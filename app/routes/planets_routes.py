from flask import Blueprint, abort, make_response, request
from app.models.planets import Planet
from ..db import db

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planet_bp.post("")
def create_planet():
    request_body = request.get_json()
    id = request_body["id"]
    name = request_body["name"]
    description = request_body["description"]
    diameter = request_body["diameter"]
    number_of_moons = request_body["number_of_moons"]
    
    new_planet = Planet(id=id, name=name, description=description, diameter=diameter, number_of_moons=number_of_moons)
    db.session.add(new_planet)
    db.session.commit()
    
    response = new_planet.to_dict()
    return response, 201
    
@planet_bp.get("")
def get_all_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)
    
    response_body = [planet.to_dict() for planet in planets]
    
    return response_body, 200
 
 
 
        
# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         response = {"message": f"planet {planet_id} invalid"}
#         abort(make_response(response, 400))
    
#     for planet in planets:
#         if planet.id == planet_id:
#             return planet
    
#     response = {"message": f"planet {planet_id} not found"}
#     abort(make_response(response, 404))       
    
    
    
# @planet_bp.get("")
# def get_all_planets():
#     planets_response = [planet.to_dict() for planet in planets ]
#     return planets_response

# @planet_bp.get("/<planet_id>")
# def get_one_planet(planet_id):
#     planet = validate_planet(planet_id)

#     return planet.to_dict()


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        response = {"message": f"planet {planet_id} invalid"}
        abort(make_response(response, 400))
    
    for planet in planets:
        if planet.id == planet_id:
            return planet
    
    response = {"message": f"planet {planet_id} not found"}
    abort(make_response(response, 404))