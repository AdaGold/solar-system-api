from app import db 
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json() 
    new_planet = Planet (
        name=request_body["name"],
        description=request_body["description"],
        distance=request_body["distance"]
        )
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def read_all_planets():
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "distance": planet.distance
            })
        return jsonify(planets_response)


            
# class Planet:
#     def __init__(self, id, name, description, distance):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.distance = distance
#         self.dictionary = {"id" : id, "name" : name, "description": description, "distance": distance}

# planets = [
#     Planet(1, 'Mercury', 'Rocky', '38 million'),
#     Planet(2, 'Venus', 'Cloudy', '66 million'),
#     Planet(3, 'Earth', 'Home', '92 million'),
#     Planet(4, 'Mars', 'Red', '141 million'),
#     Planet(5, 'Jupiter','Spotty', '483 million'),
#     Planet(6, 'Saturn', 'Rings', '890 million'),
#     Planet(7, 'Uranus', 'Ice Giant', '1.7 billion'),
#     Planet(8, 'Neptune', 'Dense Ice', '2.7 billion'),
#     Planet(9, 'Pluto', 'Dwarf Planet', '3.7 billion')

# ]

# planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

# @planet_bp.route("", methods=["GET"])
# def get_planets():
#     planet_list = []
#     for planet in planets:
#         planet_list.append(
#             {
#             "id" : planet.id,
#             "name" : planet.name,
#             "description" : planet.description,
#             "distance" : planet.distance
#             }
#         )
#     return jsonify(planet_list)

# @planet_bp.route("/<planet_id>", methods=["GET"])
# def get_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message" : f"book {planet_id} invalid"}, 400))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet.dictionary
        
#     abort(make_response({"message":f"planet {planet_id} not found"}, 404))