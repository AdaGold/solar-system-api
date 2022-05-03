from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

# class Planet:
#     def __init__(self, id, name, color, description):
#         self.id = id
#         self.name = name
#         self.color = color
#         self.description = description

#     def to_dict(self):
#         return dict(
#                 id=self.id,
#                 name=self.name,
#                 color=self.color,
#                 personality=self.description,)
        

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)
    if not planet:
        abort(make_response({"message":f"planet {planet_id} not found"}, 404))

    return planet

@planets_bp.route("", methods=["GET"])
def index_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "color": planet.color,
                "description": planet.description
            })
        return jsonify(planets_response)


# planets = [
#     Planet(1, "Pluto", "blue", "dwarf-sized"),
#     Planet(2, "Saturn", "yellow", "2nd largest planet"),
#     Planet(3, "Jupiter", "red-orange", "largest planet")
# ]

# @planets_bp.route("/<id>", methods=["GET"])
# def get_planet_id(id):
#     try:

#         id = int(id)
    
#     except:
#         return "Bad data, 400"

#     for planet in planets:
#         if planet.id == id:
#             return planet.to_dict()
#     return "Not found", 404
@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                    color=request_body["color"],
                    description=request_body["description"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "color": planet.color,
        "description": planet.description
    }


@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.color = request_body["color"]
    planet.description = request_body["description"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated")

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted")
