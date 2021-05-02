from app import db 
from models.planet import Planet
from flask import request, Blueprint, make_response, jsonify 

planet_bp = Blueprint("planets", __name__, url_prefix="/planets") 

# ENPOINT 1
@planet_bp.route("", methods=["POST"]) # Ask: /add-a-planet
def add_planet():    
    """Adds a new planet record to the DB table"""
    request_body = request.get_json() 
    new_planet = Planet(
        name=request_body["name"],
        description=request_body["description"], 
        order=request_body["order"] 
    )
    
    db.session.add(new_planet) 
    db.session.commit() 

    return make_response(f"Planet {new_planet.name} has been successfully added.", 201)

# ENDPOINT 2
@planet_bp.route("", methods=["GET"]) # Ask: /all-planets
def get_all_planets():
    """Gets data of the existing planets in the DB table"""
    all_planets = Planet.query.all() 
    response = [] 

    if all_planets: 
        for planet in all_planets:
            response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "order": planet.order
                })

        planets_json = jsonify(response) 
        return make_response(planets_json, 200) 
    
    return({"message": "No planets were found."}, 404) 

# ENDPOINT 3
@planet_bp.route("/<planet_id>", methods=["GET"]) 
def get_one_planet(planet_id):
    """Gets data of a particular planet"""
    planet = Planet.query.get(planet_id)

    if planet:
        return({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "order": planet.order
        }, 200)

    return({"message": f"Planet with id #{planet_id} was not found."}, 404) 
