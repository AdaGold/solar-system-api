from app import db
from app.model.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST", "GET"])

def handle_planets():
    if request.method == "GET":
        planet_query = request.args.get("name")
        if planet_query:
            planets = Planet.query.filter_by(name=planet_query)
        else:
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
    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
                    description=request_body["description"],
                    moons=request_body["moons"])

        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} successfully created", 201)
        
@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_planet(planet_id):
    planet = Planet.query.get(planet_id)

    if planet is None:
        return make_response("Planet does not exist", 404)

    elif request.method == "GET":
        return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description
    }

    elif request.method == "PUT":
        request_body = request.get_json()

        planet.name = request_body["name"]
        planet.description = request_body["description"]
        planet.moons = request_body["moons"]

        db.session.commit()

        return make_response(f"{planet.name} has been updated.")

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()

        return make_response("Planet was deleted.", 200)


# class Planet:
#     def __init__(self, id, name, description, ring_status):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.ring_status = ring_status 
# # id of planet based on size
# planets = [
#     Planet(1, "Pluto", "The dwarf planet.", 0),
#     Planet(2, "Mercury", "Always in retrograde.",0 ),
#     Planet(3, "Mars", "Men are from Mars.", 0),
#     Planet(4, "Venus", "Women are from Venus.", 0),
#     Planet(5, "Earth", "Earth is ghetto and I want to leave.", 0),
#     Planet(6, "Neptune", "Brother of Jupiter and Pluto.", 6),
#     Planet(7, "Uranus", "What an unfortunate name.", 13),
#     Planet(8, "Saturn", "Like the cars, what happened to them?", "Undetermined"),
#     Planet(9, "Jupiter", "Boys go to Jupiter to get more stupider.", 3)
# ] 

# planets_bp = Blueprint("planets", __name__, url_prefix= "/planets")

# @planets_bp.route("", methods= ["GET"])
# def list_of_planets():
#     planet_list = []
#     for planet in planets:
#         planet_list.append({
#             "id" : planet.id,
#             "name" : planet.name,
#             "description" : planet.description,
#             "ring_status" : planet.ring_status

#         })
#     return jsonify(planet_list)

# @planets_bp.route("/<planet_name>", methods= ["GET"])
# def get_one_planet(planet_name):
#     # planet_name.title()
#     for planet in planets:
#         if planet.name == planet_name:
#             planet_info = {
#             "id" : planet.id,
#             "name" : planet.name,
#             "description" : planet.description,
#             "ring_status" : planet.ring_status}

#             return planet_info
