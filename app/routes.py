from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort
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

#helper function
#refactored
def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except: #ValueError:
        abort(make_response({"message": f"{cls.__name__} {model_id} is invalid. Find a planet in our solar system!"}, 400))

    # for planet in planets:
    #     if planet.id == planet_id:
    #         return planet
    model = cls.query.get(model_id)
    if not model:
        abort(make_response({"message": f"{cls.__name__} {model_id} is not found. Find a planet in our solar system!"}, 404))
    return model

#refactored
@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)
    # new_planet = Planet(
    #     name=request_body["name"],
    #     description=request_body["description"],
    #     num_moons=request_body["num_moons"]
    #     )
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

#refactored
@planets_bp.route("", methods=["GET"])
def read_all_planets():
    name_query = request.args.get("name")
    if name_query:
        planets = Planet.query.filter_by(name = name_query)
    else:
        planets = Planet.query.all()
    results = [planet.to_dict() for planet in planets]
    return jsonify(results), 200
    # planets = Planet.query.all()
    # planets_response = []
    # for planet in planets:
    #     planets_response.append(
    #         {
    #         "name": planet.name,
    #         "description" : planet.description,
    #         "num_moons" : planet.num_moons
    #     }
    #   )
    #return jsonify(planets_response), 200
 

# @planets_bp.route("/<planet_id>",methods=["GET"])
# def handle_planet(planet_id):
#     planet = validate_planet(planet_id)

#     return planet.planet_dict()

#refactored
#read
@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    return  jsonify(planet.to_dict()), 200
    # {
    #     "id": planet.id,
    #     "name": planet.name,
    #     "description": planet.description,
    # }

#update
@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_model(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]

    db.session.commit()

    return make_response(f"Planet # {planet_id} successfully updated")


#delete
@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_model(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet # {planet_id} successfully deleted")