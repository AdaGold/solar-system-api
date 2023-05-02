from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods = ["GET"])
def read_all_planets():
    planets_response = []
    query_params = request.args.to_dict()

    if query_params:
        query_params = {k.lower(): v.title() for k, v in query_params.items()}
        planets = Planet.query.filter_by(**query_params).all()
    else:
        planets = Planet.query.all()

    planets_response = [planet.planet_to_dict() for planet in planets]
    return jsonify(planets_response)

@planets_bp.route("", methods = ["POST"])
def create_planets():
    request_body = request.get_json()
    try:
        new_planet = Planet.create_new_planet(request_body)
    except ValueError:
        return make_response("Invalid request", 400)
    db.session.add(new_planet)
    db.session.commit()
     # create var for make response 
    return make_response(f"Planet {new_planet.name} successfully created", 201)

def validate_planet(id):
    try:
        id = int(id)
    except:
        abort(make_response({"message":f"Planet {id} invaid"}, 400))
    
    planet = Planet.query.get(id)
    if not planet:    
        abort(make_response({"message":f"Planet {id} not found"}, 404))
    return planet 

@planets_bp.route("/<id>", methods=["GET"])
def read_one_planet(id):
    planet = validate_planet(id)
    planet = Planet.query.get(id)
    return planet.planet_to_dict()

@planets_bp.route("/<id>", methods=["PUT"])
def update_planet(id):
    planet = validate_planet(id)
    
    planet.update(request.get_json())

    db.session.commit()
    
    return make_response(f"Planet #{id} successfully updated")
          
@planets_bp.route("/<id>", methods=["DELETE"])
def delete_planet(id):
    planet= validate_planet(id)

    db.session.delete(planet)
    db.session.commit()

    return make_response (f"Planet #{id} successfully deleted", 200)



