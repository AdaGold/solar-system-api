# from flask import Blueprint, jsonify


# planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# class Planet:
#     def __init__(self, name, id, type, description, moons) -> None:
#         self.name = name
#         self.id = id
#         self.type = type
#         self.description = description
#         self.moons = moons




# @planets_bp.route("", methods =["GET"])
# def handle_planets():
#     planets_response=[]
#     for planet in planet_lst:
#         planets_response.append({"id": planet.id, 
#         "name": planet.name,
#         "type": planet.type,
#         "description": planet.description,
#         "moons": planet.moons})
#     return jsonify(planets_response)

# @planets_bp.route("/<planet_id>", methods=["GET"])
# def get_planet(planet_id):
#     planet_id = int(planet_id)

#     result = [vars(planet) for planet in planet_lst if planet.id == planet_id]
#     return jsonify(result)
#     # for planet in planet_lst:
#     #     if planet.id == planet_id:
#     #         return vars(planet)