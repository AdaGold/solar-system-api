from flask import Blueprint, jsonify, request, make_response
from app.Model.planet import Planet
from app import db

planets_bp = Blueprint("planets", __name__, url_prefix ="/planets")

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    name_query = request.args.get("name")
    planet_response = []
    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    else:
        planets = Planet.query.all()
        
    
    for each_planet in planets:
        planet_response.append(each_planet.to_dict())
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
        return jsonify(planet.to_dict())
    else:
        return make_response(f"This planet does not exist"), 404

@planets_bp.route("/<planet_id>", methods=["PUT"])
def change_data(planet_id):
    planet = Planet.query.get(planet_id)
    form_data = request.get_json()

    if planet:
        planet.name = form_data["name"]
        planet.description = form_data["description"]
        planet.mythology = form_data["mythology"]

        db.session.commit()
        return make_response(f"Planet {planet.name} was updated!")
    else:
        return make_response(f"Error planet does not exist"), 404

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = Planet.query.get(planet_id)

    if planet:
        db.session.delete(planet)
        db.session.commit()
        return make_response(f"Planet {planet.name} successfully deleted from this solar system")
    else:
        return make_response("Planet you requested does not currently exist"), 404