from flask import Blueprint,abort, make_response, jsonify, request
from app import db

class Planet:
    def __init__(self,id, name, description,color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color
        
    def planet_to_dict(self):
        return {
            "id":self.id,
            "name": self.name,
            "description":self.description,
            "color":self.color
        }


planets = [
    Planet(1,"big","pretty", "purple"),
    Planet(2,"bigg","round","orange"),
    Planet(3,"bigger","lumpy", "rainbow"),
    Planet(4,"biggerthan","wiggly","blue"),

]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods = ["GET"])
def handle_planets():
    result_list = []

    for planet in planets:
        result_list.append(planet.planet_to_dict())

    return jsonify(result_list)

def validate_planet(id):
    try:
        id = int(id)
    except:
        abort(make_response({"message": f"planet{id} invalid planet"}, 400))

    for planet in planets:
        if planet.id == id:
            return planet
        
    abort(make_response({"message":f"Planet{id} not found"},404))


@planets_bp.route("/<id>", methods=["GET"])
def handle_planet(id):
    planet = validate_planet(id)
    return planet.planet_to_dict()


@planets_bp.route("/<id>", methods=["PUT"])
def update_planet(id):
    planet = validate_planet(id)

    request_body = request.get_json()

    planet.description = request_body["description"]

    db.session.commit()

    return make_response(f"planet #{id} successfully updated")
    
   




   