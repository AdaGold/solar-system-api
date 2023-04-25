from flask import Blueprint, jsonify
            
class Planet:
    def __init__(self, id, name, description, distance):
        self.id = id
        self.name = name
        self.description = description
        self.distance = distance

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