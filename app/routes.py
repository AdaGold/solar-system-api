from app import db
from app.models.planet import Planet

from crypt import methods
from flask import Blueprint , jsonify, abort, make_response, request


planet_bp = Blueprint("planets", __name__,url_prefix="/planets")

@planet_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                    description=request_body["description"],
                    diameter = request_body["diameter"])

    db.session.add(new_planet)
    db.session.commit()

    return f"Planet {new_planet.name} successfully created", 201

@planet_bp.route("", methods=["GET"])
def read_all_planets():
    planets_response = []
    planets = Planet.query.all()
    for planet in planets:
        planets_response.append(
            {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description
            }
        )
    return jsonify(planets_response)









# class Planet:
#     def __init__(self,id,name,description,diameter):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.diameter = diameter
    
        
# https://space-facts.com/planets/
# https://solarsystem.nasa.gov/planets/neptune/overview/

# PLANETS = [
#     Planet(1, "Mercury", "The smallest planet in our solar system and closest to the Sun", "4,879 km"),
#     Planet(2, "Venus", "Spins slowly in the opposite direction from most planets", "12,104 km"),
#     Planet(3, "Earth", "The only place we know of so far that’s inhabited by living things", "12,742 km"),
#     Planet(4, "Mars", " It is a dusty, cold, desert world with a very thin atmosphere", "6,779 km"),
#     Planet(5, "Jupiter", "It's more than twice as massive than the other planets of our solar system combined", "139,822 km"),
#     Planet(6, "Saturn", "Adorned with a dazzling, complex system of icy rings, Saturn is unique in our solar system", "116,464 km"),
#     Planet(7, "Uranus", "The Sun—rotates at a nearly 90-degree angle from the plane of its orbit", "50,724 km"),
#     Planet(8, "Neptune", "The Sun—is dark, cold and whipped by supersonic winds", "49,244 km")
#     ]




# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

#     for planet in PLANETS:
#         if planet.id == planet_id:
#             return planet

#     abort(make_response({"message":f"book {planet_id} not found"}, 404))

# @planet_bp.route("", methods = ["GET"])
# def get_all_planets():
#     result = []
#     for planet in PLANETS:
#         result.append({
#             "id": planet.id,
#             "name":planet.name,
#             "description":planet.description,
#             "diameter":planet.diameter
#         })
        
#     return jsonify(result)

# @planet_bp.route("/<planet_id>", methods = ["GET"])
# def get_one_planet(planet_id):
#     planet = validate_planet(planet_id)
#     return jsonify({
#         "id": planet.id,
#         "name":planet.name,
#         "description":planet.description,
#         "diameter":planet.diameter
#         })
