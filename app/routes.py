from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# class Planet:
#     def __init__(self, id, name, description, num_moons):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.num_moons = num_moons

#     def planet_dict(self):
#         return dict(
#             id = self.id,
#             name = self.name,
#             description = self.description,
#             num_moons = self.num_moons
        # )    

# planets = [
#     Planet(1,"mercury", "terrestrial",0),
#     Planet(2,"venus", "terrestrial",0),
#     Planet(3,"earth", "terrestrial",1),
#     Planet(4,"mars", "terrestrial",2),
#     Planet(5,"jupiter", "gas giant",95),
#     Planet(6,"saturn", "gas giant",83),
#     Planet(7,"uranus", "ice giant",27),
#     Planet(8,"neptune", "ice giant",14)
# ]

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except ValueError:
#         abort(make_response({"message": f"planet {planet_id} is invalid. Find a planet in our solar system!"}, 400))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet
#     abort(make_response({"message": f"planet {planet_id} is not found. Find a planet in our solar system!"}, 404))


@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name=request_body["name"],
        description=request_body["description"],
        num_moons=request_body["num_moons"]
        )
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    planets = Planet.query.all()
    planets_response = []
    for planet in planets:
        planets_response.append(
            {
            "name": planet.name,
            "description" : planet.description,
            "num_moons" : planet.num_moons
        }
        )
    return jsonify(planets_response), 200
 

# @planets_bp.route("/<planet_id>",methods=["GET"])
# def handle_planet(planet_id):
#     planet = validate_planet(planet_id)

#     return planet.planet_dict()

