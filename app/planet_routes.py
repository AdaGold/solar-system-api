from flask import Blueprint, jsonify, abort, make_response, request 
from app import db 
from app.models.planet import Planet 

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

#---------------------------------------------- Helper Functions----------------------------------------------
def validate_planet_id(planet_id):
    try:
        planet_id = int(planet_id)
    except: 
        abort(make_response("Planet id is invalid"), 400)
    
    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response(f"Planet: {planet_id} is not found."), 404)
    
    return planet 

# ---------------------------------------------- Route Functions ----------------------------------------------
@planets_bp.route("", methods = ["POST"])
def create_planet(): 
    request_body =  request.get_json()
    if "name" not in request_body or "description" not in request_body:
        return make_response("Invalid request.", 400)
        
    new_planet = Planet(
        name = request_body["name"], 
        description = request_body["description"]
    )

    db.session.add(new_planet)
    db.session.commit() 

    return make_response(f"Planet: {new_planet.name} created successfully.", 201)

@planets_bp.route("", methods = ["GET"])
def read_all_planets(): 
    planets = Planet.query.all() 
    planet_response = [] 
    for planet in planets: 
        planet_response.append(
            {"id": planet.id,
            "name": planet.name,
            "description": planet.description}
        )
    return jsonify(planet_response), 200 

@planets_bp.route("/<planet_id>", methods = ["GET"])
def read_one_planet_by_id(planet_id): 
    planet = validate_planet_id(planet_id) 

    return ({
        "id" : planet.id,
        "name" : planet.name, 
        "description" : planet.description 
    }, 200)  

@planets_bp.route("/<planet_id>", methods = ["PUT"])
def update_planet_by_id(planet_id):
    planet = validate_planet_id(planet_id) 

    request_body = request.get_json() 

    if "name" in request_body:
        planet.name = request_body["name"]
    if "description" in request_body:
        planet.name = request_body["description"]

    db.session.commit() 

    return (f"Planet: {planet_id} has been updated successfully.", 200) 

@planets_bp.route("/<planet_id>", methods = ["DELETE"])
def delete_planet_by_id(planet_id): 
    planet = validate_planet_id(planet_id)  

    db.session.delete(planet)
    db.session.commit()

    return (f"Planet: {planet_id} has been deleted successfully.", 200) 


# ----------------------- Hard coded routes for practice and notes ------------------------------
# class Planets:
#     def __init__(self, id, name, description, gravity):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.gravity = gravity

#     def to_dict(self): 
#         return {
#             "id": self.id,
#             "name": self.name,
#             "description": self.description,
#             "gravity": self.gravity
#         }


# planets = [
#     Planets(1, "Mercury",
#             "The smallest planet in our solar system and nearest to the Sun.", "3.7 m/s^2"),
#     Planets(2, "Earth", "The third planet from the Sun", "9.807 m/s^2"),
#     Planets(3, "Jupiter", "The largest planet in the solar system", "24.79 m/s^2")
# ]

# planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


# @planets_bp.route("", methods=["GET"])
# def planets_json():
#     planets_response = []
#     for planet in planets:
#         planets_response.append({
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description,
#             "gravity": planet.gravity
#         })
#     return jsonify(planets_response), 200


# def planet_validation(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"Message": "Planet id must be an integer."}, 401))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet

#     abort(make_response({"Message": f"Planet {planet_id} not found."}, 404))


# @planets_bp.route("/<planet_id>", methods=["GET"])
# def get_planet_by_id(planet_id):
#     planet = planet_validation(planet_id)
#     return jsonify(planet.to_dict()), 200

# @planets_bp.route("/name/<planet_name>", methods=["GET"])
# def get_planet_by_name(planet_name):
#     for planet in planets: 
#         if planet.name.lower() == planet_name.lower(): 
#             return jsonify(planet.to_dict()), 200

#     abort(make_response({"Message": f"Planet {planet_name} not found."}, 404))

# ----------------------- Hard coded routes for practice and notes ------------------------------
