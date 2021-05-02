# routes.py //////////////////////////////////////////////////////////////////////////////////////////////////////
from app import db 
from models.planet import Planet
from flask import request, Blueprint, make_response

planet_bp = Blueprint("planets", __name__,url_prefix="/planets") # change back?

# ENPOINT 1
# request with new valid planet data and get a success response
@planet_bp.route("", methods=["POST"]) # /add-a-planet
def add_planet():
    # what conditional can we use to control for returning a 'failure' message? 
    ap_response_body = request.json()
    new_planet = Planet(name=ap_response_body["name"],
            description=ap_response_body["description"], size=ap_response_body["size"])
    
    db.session.add(new_planet) 
    db.session.commit() 
    return make_response(f"You successfully added Planet {new_planet.name}", 201)


# ENDPOINT 2
# get ALL existing planets + their data
@planet_bp.route("", methods=["GET"]) # all-planets
def see_all_planets():
    all_planets = Planet.query.all() 
    hold_planets = []

    #if all_planets:
    for planet in all_planets:
        hold_planets.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "size": planet.size
            })

        planets_json = jsonify(hold_planets)
        return make_response(planets_json, 200) # do we really need jsonify??
    
    #return {
        #"message": "No planets were found"}, 404

# ENDPOINT 3
# get ONE existing planet + its data
@planet_bp.route("/<planet_id>", methods=["GET"]) # /<planet_id>
def see_one_planet(planet_id):
    planet = Planet.query.get(planet_id)

    #if planet:
    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "size": planet.size
        }
    #return {
        #"message": f"Planet {planet.name} was not found"}, 404