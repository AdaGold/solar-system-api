from app import db
from app.Models.planet import Planets
from flask import Blueprint, jsonify, abort, make_response,request, abort

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

#helper functions
def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response(
            {"message":f"Planet {planet_id} invalid"},400
        ))
    planet = Planets.query.get(planet_id)

    if not planet:
        abort(make_response(
            {"message":f"Planet {planet_id} not found"}, 404
        ))

    return planet

#wave 3 create and read endpoints for planets
@planets_bp.route("", methods=["GET", "POST"])
def planets_create_and_read():
    if request.method == "GET":
        planets = Planets.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "gravity": planet.gravity
            })
        return jsonify(planets_response), 200
    elif request.method == "POST":
        planet_data = request.get_json()
        new_planet = Planets(
            name = planet_data["name"],
            description = planet_data["description"],
            gravity = planet_data["description"]
            )

        db.session.add(new_planet)
        db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created.", 201)


#wave 4 read, update and delete
@planets_bp.route("/<planet_id>", methods = ["GET"]) 
#read planet by id endpoint
def read_planet_by_id(planet_id):
    planet = validate_planet(planet_id)
    return jsonify({
        "id": planet.id,
        "name": planet.name,
        "description": planet.description, 
        "gravity": planet.gravity
    })

@planets_bp.route("/<planet_id>", methods = ["PUT"]) 
#update planet by id endpoint
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    planet_data = request.get_json()

    planet.name = planet_data["name"]
    planet.description = planet_data["description"]
    planet.gravity = planet_data["gravity"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated") 
    

@planets_bp.route("/<planet_id>", methods = ["DELETE"])
#delete planet by id endpoint
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted")

#--------------------------- hard coded data below -----------------------------------


# planets = [
#     Planets(1, "Mercury",
#             "The smallest planet in our solar system and nearest to the Sun.", "3.7 m/s^2"),
#     Planets(2, "Earth", "The third planet from the Sun", "9.807 m/s^2"),
#     Planets(3, "Jupiter", "The largest planet in the solar system", "24.79 m/s^2")
# ]




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
