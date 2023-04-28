from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

# class Planet:
#     def __init__(self, id, name, description, color):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.color = color

#     def make_dict(self):
#         return dict(
#             id=self.id,
#             name=self.name,
#             description=self.description,
#             color=self.color,
#         )

# planets = [
#     Planet(1, "Mercury", "1st planet from the Sun", "light blue"),
#     Planet(2, "Venus", "2nd planet from the Sun", "orange"),
#     Planet(3, "Earth", "3rd planet from the Sun", "black"),
#     Planet(4, "Mars", "4th planet from the Sun", "red"),
#     Planet(5, "Jupiter", "5th planet from the Sun", "green"),
#     Planet(6, "Saturn", "6th planet from the Sun", "purple"),
#     Planet(7, "Uranus", "7th planet from the Sun", "dark blue"),
#     Planet(8, "Neptune", "8th planet from the Sun", "aqua"),
# ]

bp = Blueprint("planets", __name__, url_prefix="/planets")

# ______________________________________________
@bp.route("", methods=["POST"])
def handle_planets():
    if request.method == "POST":
        request_body = request.get_json()
        if "name" not in request_body or "description" not in request_body or "color" not in request_body:
            return make_response("Invalid Request", 400)

        new_planet = Planet(
            name = request_body["name"],
            description = request_body["description"],
            color = request_body["color"]
            )

        db.session.add(new_planet)
        db.session.commit()

        return make_response(
            f"Planet {new_planet.name} successfully created", 201
        )
    
@bp.route("", methods=["GET"])
def read_all_planets():
    planets = Planet.query.all()
    planets_list = []
    for planet in planets:
        planets_list.append(planet.make_dict())
    return jsonify(planets_list), 200   







# ____________________________________________


# def validate_planet(id):
#     try:
#         id = int(id)
#     except:
#         abort(make_response({"message": f"Planet {id} is invalid."}, 400))

#     for planet in planets:
#         if planet.id == id:
#             return planet

#     abort(make_response({"message": f"Planet {id} not found."}, 404))
    
# @bp.route("", methods=["GET"])
# def handle_planets():
#     result_list = []
#     for planet in planets:
#         result_list.append(planet.make_dict())
#     return jsonify(result_list)

# @bp.route("/<id>", methods=["GET"])
# def handle_planet(id):
#     planet = validate_planet(id)
#     return planet.make_dict()