from flask import Blueprint, jsonify, make_response, abort, request
from app.models.planet import Planet
from app import db

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

# helper function
def validate_planet_id(id):
    try:
        id = int(id)
    except:
        abort(make_response({"message": "The id {id} invalid"}, 400))

    planet = Planet.query.get(id)
    
    if not planet:
        abort(make_response({"message": "The id {id} not found"}, 404))

    return planet

#POST Planets
@planet_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name = request_body["name"],
        description = request_body["description"],
    )

    db.session.add(new_planet)
    db.session.commit()

    message = f"Planet {new_planet.name} successfully created."
    return make_response(message, 201)

# GET Planets 
@planet_bp.route("", methods=["GET"])
def get_all_planets():
    planets = Planet.query.all()
    results =[]
    for planet in planets:
        results.append(
            dict(
            id = planet.id,
            name = planet.name,
            description = planet.description,
            )
        )
    return jsonify(results)

# GET one planet
@planet_bp.route("/<planet_id>", methods = ["GET"])
def get_one_planet(planet_id):

    planet = validate_planet_id(planet_id)

    response_body = dict(
        id = planet.id,
        name = planet.name, 
        description = planet.description
    )

    return response_body

# UPDATE one planet
@planet_bp.route("/<planet_id>", methods = ["PUT"])
def update_one_planet(planet_id):

    planet = validate_planet_id(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]

    db.session.commit()
    
    message = f"Planet {planet.id} successfully updated"

    return make_response(message, 200)

# DELETE one planet
@planet_bp.route("/<planet_id>", methods = ["DELETE"])
def delete_one_planet(planet_id):

    planet = validate_planet_id(planet_id)

    db.session.delete(planet)
    db.session.commit()

    message = f"Planet {planet.id} successfully deleted"

    return make_response(message, 200)





# def validate_planet_id(id):
#     try:
#         id = int(id)
#     except:
#         abort(make_response({"message": "The id {id} invalid"}, 400))

#     for planet in planets:
#         if planet.id == id:
#             return planet
    
#     abort(make_response({"message": "The id {id} not found"}, 404))



# @planet_bp.route("/<id>", methods=["GET"])
# def handle_planet(id):

#     planet = validate_planet_id(id)

#     return planet.make_dict()

    

# @planet_bp.route("", methods=["GET"])
# def handle_planets():
#     # results = []
#     # for planet in planets:
#     #     results.append(planet.make_dict())

#     results = [planet.make_dict() for planet in planets]

#     return jsonify(results)