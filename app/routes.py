from flask import Blueprint,jsonify, make_response, request
from app import db
from app.models.planet import Planet


planets_bp = Blueprint("planets",__name__,url_prefix="/planets")

@planets_bp.route("", methods=["GET","POST"])
def handle_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planet_response = []
        for each_planet in planets:
            planet_response.append({
                "id" : each_planet.id,
                "name" : each_planet.name,
                "description" : each_planet.description,
                "color" : each_planet.color
            })
        return jsonify(planet_response)

    elif request.method == "POST": 
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
                            description=request_body["description"],
                            color=request_body["color"])
        
        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])     # this is a end point with get method to look up a planet with its id(primary key)
# if the path is like /planet/1 with "GET", then the following function will execute

# request methods : GET, POST(CREATE), PUT(BIG UPDATE), PATCH(SMALL UPDATE), DELETE
def get_single_planet(planet_id):
    one_planet = Planet.query.get(planet_id)

    if one_planet is None:
        return make_response("Error" , 404)

    if request.method == "GET": 
        return {
            "id" : one_planet.id,
            "name" : one_planet.name,
            "description" : one_planet.description,
            "color" : one_planet.color
        }

    if request.method == "PUT":
        request_body = request.get_json()
        one_planet.name = request_body["name"]
        one_planet.description = request_body["description"]
        one_planet.color = request_body["color"]

        db.session.commit()

        return make_response(f"Planet {one_planet.name} successfully updated")
    
    if request.method == "DELETE":
        db.session.delete(one_planet)
        db.session.commit()
        return make_response(f"Planet #{one_planet.id} with planet name {one_planet.name} successfully deleted")

























# class Planet:
#     #Dunder, it is a constructer method to construct each planet object, it requires us everytime when we construct we have to provide details of the following attributes
#     def __init__(self,id,name,description, color):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.color = color
# planets = [
#     Planet(1,"Mars","Round,Big", "Red"),
#     Planet(2,"Saturn","Round,Big","Yellow"),
#     Planet(3, "Jupiter","Round,Big","Blue")
#     ]


# @planets_bp.route("", methods = ["GET"])
# def get_planets():
#     #this planet_response is a variable which will store a list, there will be dicitonaries inside the list, each dictionary represents each planet.
#     planet_response = []
#   #We used a for loop to loop through the planets list which is on line 8, and each iteration we look at EACH planet.
#     for planet in planets:
#         #append is a method of a list to add DICT to that list. Content insisde need to be in K:V Pair, the key is a "" type and each key rep planet attributes, and the value of each key rep each planet attribute
#         planet_response.append({
#         "id" : planet.id,   
#         "name" : planet.name,
#         "description" : planet.description,
#         "color" : planet.color,
#         })
#     return jsonify(planet_response)
# @planets_bp.route("/<planet_id>", methods = ["GET"])
# def get_single_planet (planet_id):
#     #Make str into int because to compare == both datatype should be the same
#     given_planet_id = int(planet_id)
#     for planet in planets:
#         if planet.id == given_planet_id:
#             return {
#         "id" : planet.id,   
#         "name" : planet.name,
#         "description" : planet.description,
#         "color" : planet.color,
#             }
