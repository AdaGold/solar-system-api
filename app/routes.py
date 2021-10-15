from flask import Blueprint, jsonify

planets_bp = Blueprint('planets',__name__, url_prefix='/planets')

class Planet:
    def __init__(self,id, name, description, number_of_moons):
        self.id = id
        self.name = name
        self.description = description
        self.number_of_moons = number_of_moons

planets = [
            Planet(1,'Earth', 'water planet', 1), 
            Planet(2, 'Mercury', 'fastest', 0),
            Planet(3, 'Jupiter', 'biggest', 79),
            Planet(4, 'Saturn', 'gaseous', 82),
            Planet(5, 'Mars', 'red', 2),
            Planet(6, 'Uranus', 'coldest', 27),
            Planet(7, 'Neptune', 'farthest from the sun', 14),
            Planet(8, 'Venus', 'hottest', 0)
          ]

@planets_bp.route('', methods=['GET'])
def handle_planets():
  planets_response = []
  for planet in planets:
    planets_response.append({'id': planet.id, 'name':planet.name, 
    'description':planet.description, 'number of moons': planet.number_of_moons})
  return jsonify(planets_response)

@planets_bp.route('/<planet_id>', methods=['GET'])
def handle_planet(planet_id):
  planet_id = int(planet_id)
  for planet in planets:
    if planet.id == planet_id:
      return {'id': planet.id, 'name':planet.name, 
    'description':planet.description, 'number of moons': planet.number_of_moons}