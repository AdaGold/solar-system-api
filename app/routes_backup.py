# # from app import db
# from app.models.planet import Planet
# from flask import Blueprint, jsonify, abort, make_response, request


# bp = Blueprint("planets", __name__, url_prefix="/planets")

# # ______________________________________________
# def validate_planet(id):
#     try:
#         id = int(id)
#     except:
#         abort(make_response({"message": f"Planet {id} is invalid."}, 400))

#     planet = Planet.query.get(id)

#     if not planet:
#         abort(make_response({"message": f"Planet {id} not found."}, 404))

#     return planet

# @bp.route("", methods=["GET"])
# def read_all_planets():
#     planets = Planet.query.all()
#     planets_list = []
#     for planet in planets:
#         planets_list.append(planet.make_dict())

#     return jsonify(planets_list), 200   

# @bp.route("/<id>", methods=["GET"])
# def read_one_planet(id):
#     planet = validate_planet(id)
    
#     return jsonify(planet.make_dict()), 200

# @bp.route("", methods=["POST"])
# def create_planet():
#     if request.method == "POST":
#         request_body = request.get_json()
#         if "name" not in request_body or "description" not in request_body or "color" not in request_body:
#             return make_response("Invalid Request", 400)

#         new_planet = Planet.make_dict(request_body)

#         db.session.add(new_planet)
#         db.session.commit()

#         return make_response(
#             f"Planet {new_planet.name} successfully created", 201
#         )
    
# @bp.route("/<id>", methods=["PUT"])
# def update_planet(id):
#     planet = validate_planet(id)

#     request_body = request.get_json()

#     planet.name = request_body["name"]
#     planet.description = request_body["description"]
#     planet.color= request_body["color"]
    
#     db.session.commit()

#     return make_response(
#         f"Planet #{id} successfully updated", 200
#     )

# @bp.route("/<id>", methods=["DELETE"])
# def delete_planet(id):
#     planet = validate_planet(id)

#     db.session.delete(planet)
#     db.session.commit()

#     return make_response(f'Planet #{id} successfully deleted'), 200