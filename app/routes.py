from flask import Blueprint, jsonify, make_response, request
from app import db
from app.models.planet import Planet


# class Planet:
#     def __init__(self, id, name, description, moons):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.moons = moons 

# planets = [
#     Planet(1, "Mercury", "Smallest planet", 0),
#     Planet(2,"Venus", "Second planet from sun",0),
#     Planet(3, "Jupiter", "Gas giant", 53)
#     ]

planets_bp = Blueprint("planets", __name__,url_prefix="/planets")

# @planets_bp.route("", methods = ["GET"])
# def get_planets():
#     planet_response = []
#     for planet in planets:
#         planet_response.append({
#             "id" : planet.id,
#             "name" : planet.name,
#             "description" : planet.description,
#             "color" : planet.color,
#         })
#     return jsonify(planet_response)

# @planets_bp.route("/<planet_id>", methods = ["GET"])
# def get_single_planet(planet_id):
#     given_planet_id = int(planet_id)
#     for planet in planets:
#         if planet.id == given_planet_id:
#             return {
#                 "id" : planet.id,
#                 "name" : planet.name,
#                 "description" : planet.description,
#                 "moons" : planet.color,
#                 }

@planets_bp.route("", methods=["POST", "GET"])
def handle_planets():
    if request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        moons=request_body["moons"])

        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} successfully created", 201)

    elif request.method == "GET":
        planets = Planet.query.all()	
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "moons": planet.moons
            })
        return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def single_planet(planet_id):
    planet = Planet.query.get(planet_id)

    if not planet:
        return make_response(f"Planet {planet_id} resource was not found", 404)

    if request.method == "GET":
        return { 
            "id": planet.id, 
            "name": planet.name,
            "description": planet.description,
            "moons": planet.moons
        } 
    elif request.method == "PUT":
        request_body = request.get_json()

        planet.name =request_body.get("name", planet.name)
        planet.description =request_body.get("description", planet.description)
        planet.moons = request_body.get("moons", planet.moons)

        db.session.commit()

        return jsonify(f"Planet #{planet.id} successfully updated"), 200

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return jsonify(f"Planet #{planet.id} successfully deleted"), 200