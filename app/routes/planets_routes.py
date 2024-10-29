from flask import Blueprint, abort, make_response, request
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
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)
    
    response_body = [planet.to_dict() for planet in planets]
    
    return response_body, 200
 
 
 
        
