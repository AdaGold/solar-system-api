from flask import Blueprint, jsonify, make_response, abort, request
from app import db
from app.models.planet import Planet

planet_bp = Blueprint("planet_blue_print", __name__, url_prefix="/planets")
@planet_bp.route("", methods=["POST"])
def handle_planets():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"], 
                        description=request_body["description"], 
                        number_of_moons = request_body["number_of_moons"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planet_bp.route("", methods=["GET"])
def get_all_planets():
    planets_response = []
    planets = Planet.query.all()
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "number_of_moons": planet.number_of_moons
            }
        )
    return jsonify(planets_response)
#==============
@planet_bp.route("/<id>", methods=["GET"])
def get_one_planet(id):
    planet = validate_id(id)
    return {"id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "number_of_moons": planet.number_of_moons}

@planet_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_id(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.number_of_moons = request_body["number_of_moons"]

    db.session.commit()

    return make_response(f"planet #{planet.id} successfully updated")


@planet_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_id(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted")

def validate_id(id):
    try:
        id = int(id)
    except:
        abort(make_response(f"this is not a valid id: {id}", 400))
    
    planet = Planet.query.get(id)
    if not planet:
        abort(make_response(f"id {id} not found!", 404))
    return planet


#=============================
# {
# "name" : "Jupiter",
# "description": "King of the Roman gods, aka Zeus.",
# "number_of_moons": 79}

#  {
# "name" : "Mars",
# "description": "Roman god of war, aka Ares.",
# "number_of_moons": 2}

# Name, Description, Moons
# Jupiter,"King of the Roman gods, aka Zeus.",79
# Mars,"Roman god of war, aka Ares.",2
# Venus,"Roman goddess of love, aka Aphrodite.",0
# Earth,"A variation on the word ""ground"" in several languages.",1
# Neptune,"Roman god of the sea aka, Poseidon.",14
# Saturn,"Jupiter's father and titan aka, Chronos.",62
# Uranus,"Greek personificatino of the sky or heavens, aka Caelus.",27
# Mercury,"Roman god of travellers, aka Hermes.",0


# class Planet:
#     def __init__(self, id, name, description):
#         self.id = id
#         self.name = name
#         self.description = description

#     def to_dict(self):
#         return {"id": self.id,
#             "name" : self.name,
#             "description": self.description}

# planets = [
#     Planet(1, "Earth", "Solid"),
#     Planet(2, "Mars", "Solid"),
#     Planet(3, "Saturn", "Gas")
# ]

# planet_bp = Blueprint("planet_blue_print", __name__, url_prefix="/planets")
# @planet_bp.route("", methods=["GET"])
# def get_planet():
#     all_planets = []
#     for planet in planets:
#         planet_dic = planet.to_dict()
#         all_planets.append(planet_dic)
#     return jsonify(all_planets)


# @planet_bp.route("/<planet_id>", methods=["GET"])
# def get_one_planet(planet_id):
#     planet = validate_id(planet_id)
#     return planet.to_dict()

# def validate_id(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message":f"id {planet_id} is not valid"}, 400))
#     for planet in planets:
#         if planet.id == id:
#             return planet
#     abort(make_response({"message":f"id {planet_id} not found"}, 404))