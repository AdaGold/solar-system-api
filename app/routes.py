from flask import Blueprint, jsonify, make_response, abort
            
class Planet:
    def __init__(self, id, name, description, distance):
        self.id = id
        self.name = name
        self.description = description
        self.distance = distance
        self.dictionary = {"id" : id, "name" : name, "description": description, "distance": distance}

planets = [
    Planet(1, 'Mercury', 'Rocky', '38 million'),
    Planet(2, 'Venus', 'Cloudy', '66 million'),
    Planet(3, 'Earth', 'Home', '92 million'),
    Planet(4, 'Mars', 'Red', '141 million'),
    Planet(5, 'Jupiter','Spotty', '483 million'),
    Planet(6, 'Saturn', 'Rings', '890 million'),
    Planet(7, 'Uranus', 'Ice Giant', '1.7 billion'),
    Planet(8, 'Neptune', 'Dense Ice', '2.7 billion'),
    Planet(9, 'Pluto', 'Dwarf Planet', '3.7 billion')

]

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planet_bp.route("", methods=["GET"])
def get_planets():
    planet_list = []
    for planet in planets:
        planet_list.append(
            {
            "id" : planet.id,
            "name" : planet.name,
            "description" : planet.description,
            "distance" : planet.distance
            }
        )
    return jsonify(planet_list)

@planet_bp.route("/<planet_id>", methods=["GET"])
def get_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message" : f"book {planet_id} invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet.dictionary
        
    abort(make_response({"message":f"planet {planet_id} not found"}, 404))