from flask import Blueprint, jsonify, request, make_response
from app.Model.planet import Planet
from app import db

planets_bp = Blueprint("planets", __name__, url_prefix ="/planets")

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planets = Planet.query.all()
    planet_response = []
    for each_planet in planets:
        planet_response.append({
            "id": each_planet.id,
            "name": each_planet.name,
            "description": each_planet.description,
            "mythology": each_planet.mythology
        }   
        )
    return jsonify(planet_response), 200

@planets_bp.route("", methods=["POST"])
def create_new_planet():
    request_body = request.get_json()
    if "name" not in request_body or "description" not in request_body or "mythology" not in request_body:
        return jsonify({"message": "Missing input"}), 400

    new_planet = Planet(name=request_body["name"],
                    description=request_body["description"],
                    mythology=request_body["mythology"]
                    )
    db.session.add(new_planet)
    db.session.commit()
    
    return make_response(f"Your mystical planet {new_planet.name} was successfully created in our universe!", 201) 


@planets_bp.route("/<planet_id>", methods=["GET"])
def get_single_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet:
        return jsonify({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "mythology": planet.mythology,
            })
    else:
        return {"Message": f"This planet does not exist"}, 404