from flask import Blueprint, jsonify, make_response, abort, request
from app.models.planet import Planet
from app import db

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

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