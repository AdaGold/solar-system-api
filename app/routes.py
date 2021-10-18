from flask import Blueprint,jsonify
class Planet:
    #Dunder, it is a constructer method to construct each planet object, it requires us everytime when we construct we have to provide details of the following attributes
    def __init__(self,id,name,description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color
planets = [
    Planet(1,"Mars","Round,Big", "Red"),
    Planet(2,"Saturn","Round,Big","Yellow"),
    Planet(3, "Jupiter","Round,Big","Blue")
    ]
planets_bp = Blueprint("planets",__name__,url_prefix="/planets")
@planets_bp.route("", methods = ["GET"])
def get_planets():
    #this planet_response is a variable which will store a list, there will be dicitonaries inside the list, each dictionary represents each planet.
    planet_response = []
  #We used a for loop to loop through the planets list which is on line 8, and each iteration we look at EACH planet.
    for planet in planets:
        #append is a method of a list to add DICT to that list. Content insisde need to be in K:V Pair, the key is a "" type and each key rep planet attributes, and the value of each key rep each planet attribute
        planet_response.append({
        "id" : planet.id,   
        "name" : planet.name,
        "description" : planet.description,
        "color" : planet.color,
        })
    return jsonify(planet_response)
@planets_bp.route("/<planet_id>", methods = ["GET"])
def get_single_planet (planet_id):
    #Make str into int because to compare == both datatype should be the same
    given_planet_id = int(planet_id)
    for planet in planets:
        if planet.id == given_planet_id:
            return {
        "id" : planet.id,   
        "name" : planet.name,
        "description" : planet.description,
        "color" : planet.color,
            }
            

