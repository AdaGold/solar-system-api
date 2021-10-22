from flask import Blueprint
from flask import jsonify

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")


class Planet:
    def __init__(self, id, name, description, moon=False):
        self.id = id
        self.name = name
        self.description = description
        self.moon = moon

    @staticmethod
    def make_json_data(planets):
        planet_response_object = []
        for planet in planets:
            planet_response_object.append(
                {
                    "id": planet.id,
                    "name": planet.name,
                    "description": planet.description,
                    "moon": planet.moon
                }
            )
        return jsonify(planet_response_object)


planets = [Planet(1, "Jenesess", "chaos", True), Planet(2, "Binet", "misandrist", False), Planet(3, "Nerouba", "purple haze", True)]

@planet_bp.route("", methods=["GET"])
def get_planets():
    planet_response = Planet.make_json_data(planets)
    return planet_response

    # planet_response = []
    # for planet in planets:
    #     planet_response.append(
    #         {
    #             "id": planet.id,
    #             "name": planet.name,
    #             "description": planet.description,
    #             "moon": planet.moon
    #         }
    #     )
    # return jsonify(planet_response)


@planet_bp.route("<planet_id>", methods=["GET"])
def single_planet(planet_id):
    planet_data = Planet.make_json_data(planets)
    for planet in planet_data:
        if planet_id == planet["id"]:
            return jsonify(planet)


# def single_planet():
#     planet_response = []
#     for planet in planets:
#         if planet_response["id"] == id:
#             planet_response.append(
#             {
#                 "id": planet.id,
#                 "name": planet.name,
#                 "description": planet.description,
#                 "moon": planet.moon
#             }
#         )
#     return jsonify(planet_response)
