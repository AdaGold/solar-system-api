from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        elements=request_body["elements"])

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
                "elements": planet.elements
            })
        return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet is None:
            return make_response("", 404)

    if request.method == "GET":
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "elements": planet.elements
        }
    
    elif request.method == "PUT":
        form_data = request.get_json()

        planet.name = form_data["name"]
        planet.description = form_data["description"]
        planet.elements = form_data["elements"]

        db.session.commit()

        return make_response(f"Planet #{planet.id} successfully updated")
    
    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return make_response(f"Planet #{planet.id} successfully deleted")
#____________________________________________________________________________
# class Planet:
#     def __init__(self, id, name, description, elements):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.elements = elements

# planets = [
#     Planet(1, "Mercury", "First planet from the sun.", "Oxygen, Magnesium, Aluminum, Silicon, Calcium"),
#     Planet(2, "Venus", "Second planet from the sun.", "Carbon, Nitrogen, Oxygen, Sulfur, Argon"),
#     Planet(3, "Earth", "Third planet from the sun.", "Oxygen, Aluminum, Silicon, Calcium, Iron"),
#     Planet(4, "Mars", "Fourth planet from the sun.", "Oxygen, Magnesium, Aluminum, Silicon, Iron"),
#     Planet(5, "Jupiter", "Fifth planet from the sun.", "Hydrogen, Helium, Carbon, Nitrogen, Oxygen"),
#     Planet(6, "Saturn", "Sixth planet from the sun.", "Hydrogen, Helium, Carbon, Nitrogen, Oxygen"),
#     Planet(7, "Uranus", "Seventh planet from the sun.", "Hydrogen, Helium, Carbon, Nitrogen, Sulfur"),
#     Planet(8, "Neptune", "Eighth planet from the sun.", "Hydrogen, Helium, Carbon, Nitrogen, Oxygen"),
#     Planet(9, "Pluto", "Still a planet!", "Hydrogen, Oxygen, Magnesium, Silicon, Iron")
# ]

# #https://www.lpi.usra.edu/education/IYPT/

# planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# @planets_bp.route("", methods = ["GET"])
# def handle_planets():
#     planets_response = []
#     for planet in planets:
#         planets_response.append(
#             {
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description,
#             "elements": planet.elements
#         }
#             )
#     return jsonify(planets_response)

# @planets_bp.route("/<planet_id>", methods = ["GET"])
# def handle_planet(planet_id):
#     planet_id = int(planet_id)
#     for planet in planets:
#         if planet.id == planet_id:
#             return {
#                 "id": planet.id,
#                 "name": planet.name,
#                 "description": planet.description,
#                 "elements": planet.elements}


