from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

# class Planet:
#     def __init__(self, id, name, description, color):
#         self.id =id
#         self.name = name
#         self.description = description
#         self.color = color
    
#     def planet_to_dict(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "description": self.description,
#             "color": self.color
#         }


# planets = [
#     Planet(1,"big", "Pretty", "Purple"),
#     Planet(2,"bigg", "Round", "Orange"),
#     Planet(3,"bigger", "Lumpy", "Rainbow"),
#     Planet(4,"biggerthan","Wiggly", "Blue"),
# ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")
@planets_bp.route("", methods = ["GET"])
def read_all_planets():
    planets = Planet.query.all()
    planets_response = []
    for planet in planets:
        planets_response.append(planet.planet_to_dict())
    return jsonify(planets_response)

@planets_bp.route("", methods = ["POST"])
def create_planets():
    request_body = request.get_json()
    if "name" not in request_body or "description" not in request_body:
        return make_response("Invalid Requesrt", 400)
    new_planet = Planet(
                    name=request_body["name"],
                    description=request_body["description"],
                    color=request_body["color"])
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

def validate_planet(id):
    try:
        id = int(id)
    except:
        abort(make_response({"message":f"Planet {id} invaid"}, 400))
    
    for planet in planets:
        if planet.id == id:
            return planet
        
    abort(make_response({"message":f"Planet {id} not found"}, 404))

@planets_bp.route("/<id>", methods=["GET"])
def handle_planet(id):
    planet = validate_planet(id)
    return planet.planet_to_dict()
        
    
