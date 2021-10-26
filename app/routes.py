from flask import Blueprint, jsonify, request, make_response
from app import db
from app.models.planet import Planet

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

def make_planet_dict(planet):
    return {
                "id" : planet.id,
                "name" : planet.name,
                "description" : planet.description,
                "num_of_moons" : planet.num_of_moons
            }

@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "GET":

        planet_name_query = request.args.get("name")
        if planet_name_query: 
            planets = Planet.query.filter(Planet.name.contains(planet_name_query))
            # we can search for a substring
        else: 
            planets = Planet.query.all()


        planets_response = []
        for planet in planets:
            current_planet = make_planet_dict(planet)
            planets_response.append(current_planet)
            
        return jsonify(planets_response), 200

    else: 
        request_body = request.get_json()
        new_planet = Planet(
            name=request_body["name"],
            description=request_body["description"],
            num_of_moons=request_body["num_of_moons"]
        )
        db.session.add(new_planet)
        db.session.commit()

        return f"Planet successfully created {new_planet.name}", 201

@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_one_planet(planet_id):
    planet = Planet.query.get(planet_id)
    
    # Guard clause 
    if planet is None:
        return make_response("", 404)
    
    if request.method == "GET": 
        return make_planet_dict(planet)
        
    elif request.method == "PUT":
        form_data = request.get_json()
        planet.name = form_data["name"]
        planet.description = form_data["description"]
        planet.num_of_moons = form_data["num_of_moons"]

        db.session.commit()
        return make_response(f"Planet #{planet.id} changed successfully")

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()

        return make_response(f"Planet #{planet.id} deleted successfully")

