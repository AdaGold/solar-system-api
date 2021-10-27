from flask import abort, Blueprint, jsonify, request
from app.models.planet import Planet
from app import db

# class Planets:
#     def __init__(self, id, name, description, proximity):
#         self.id = id
#         self.name = name
#         self.description = description 
#         self.proximity = proximity
        
# planets = [
#     Planets(1, "Mercury", "it is the smallest and fastest planet", "35.98 million miles from the Sun"),
#     Planets(2, "Venus", "spins slowly in opposite direction, hottest planet because of its thick atmosphere", "67.24 million miles from the Sun"),
#     Planets(3, "Earth", "is the only planet inhabited by living things (that we know of). Humans are ruining it", "92.96 million miles from the Sun"),
#     Planets(4, "Mars", "is dusty, cold dessert with thin atmosphere", "141.6 million miles from the Sun"),
#     Planets(5, "Jupiter", "It is the biggest planet. Its Great red spot is a storm bigger than Earth", "483.8 million miles from the Sun"),
#     Planets(6, "Saturn", "It is the second largest planet. It has icy rings. made mostly of hydrogen and helium", "890.8 million miles from the Sun"),
#     Planets(7, "Uranus", "A day in uranus lasts 17 hours and a year takes 84 Earth days. it has 27 moons", "1.784 billion miles from the Sun"),
#     Planets(8, "Neptune", "A day takes 16 hours and a year takes 165 Earth days. Dark, cold and windy", "2.793 billion miles from the Sun")
#     ]


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_data = request.get_json()

    if "name" not in request_data or "description" not in request_data \
        or "proximity" not in request_data:
        return jsonify({"message": "Missing data"}), 400

    new_planet = Planet(name=request_data["name"], description=request_data["description"],
                proximity=request_data["proximity"])
    
    db.session.add(new_planet)
    db.session.commit()

    return f"Planet {new_planet.name} created", 201

@planets_bp.route("", methods=["GET"])
def list_all_planets():
    planets_response = []
    #Can't be jsonified
    planets = Planet.query.all()
    for planet in planets:
        planets_response.append(planet.to_dict())
    return jsonify(planets_response), 200

@planets_bp.route("/<id>", methods=["GET", "PUT"])
def handle_planet(planet_id):
    print(planet_id)
    planet_id = int(planet_id)
    planet = Planet.query.get(planet_id)
    if not planet:
        return{ "Error": f"Planet {planet_id} was not found"}, 404

    if request.method == "GET":
        return jsonify(planet.to_dict()), 200
    elif request.method == "PUT":
        input_data = request.get_json()
        input_data = sanitize_data(input_data)
        planet.name = input_data["name"]
        planet.description = input_data["description"]
        planet.proximity = input_data["proximity"]
        db.session.commit()
        return jsonify(planet.to_dict()), 200

def sanitize_data(input_data):
    data_types = {"name": str, "description": str, "proximity": str}
    for name, val_type in data_types.items():
        try:
            val = input_data[name]
            type_test = val_type(val)
        except Exception as e:
            print(e)
            abort(400, "Bad Data")
    return input_data


@planets_bp.route("/<id>", methods=["DELETE"])
def delete_planet(planet_id):
    print(planet_id)
    try:
        planet_id = int(planet_id)
    except ValueError:
        return {"Error": "ID must be a number"}, 404
    planet = Planet.query.get(planet_id)

    if planet:
        db.session.delete(planet)
        db.session.commit()
        return {"Success": f"Deleted Planet {planet_id}"}, 200
    else:
        return {"Error": f" No Planet with ID matching {planet_id}"}, 404
# def list_one(id):
#     for planet in planets:
#         if planet.id == int(id):
#             response = {
#                 "id" : planet.id,
#                 "name" : planet.name,
#                 "description" : planet.description,
#                 "proximity" : planet.proximity
#             }
#             return response
#     return "There are only eight planets", 404

