from flask import Blueprint, jsonify, abort, make_response, request 
from app import db 
from app.models.planet import Planet 

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

#---------------------------------------------- Helper Functions----------------------------------------------
def validate_planet_id(planet_id):
    try:
        planet_id = int(planet_id)
    except: 
        abort(make_response({"message":f"Planet_id {planet_id} is invalid"}, 400)) 

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"Planet_id {planet_id} not found"}, 404))    
    return planet 

def validate_request_body(request_body): 
    if "name" not in request_body or "description" not in request_body or "gravity" \
        not in request_body or "distance" not in request_body:

        abort(make_response("Invalid Request", 400))

# def sort_helper(planet_query, atr, sort_method): 
#     if sort_method == "asc" and atr: 
#         planet_query = planet_query.order_by(atr.asc())
#     elif sort_method == "desc" and atr: 
#         planet_query = planet_query.order_by(atr.desc())
#     elif sort_method == "desc": 
#         planet_query = planet_query.order_by(Planet.name.desc())
#     else:
#         planet_query = planet_query.order_by(Planet.name.asc()) #Sort by name in ascending order by default 

#     return planet_query

# ---------------------------------------------- Route Functions ----------------------------------------------
@planets_bp.route("", methods = ["POST"])
def create_planet(): 
    request_body =  request.get_json()
    validate_request_body(request_body)
        
    new_planet = Planet(
        name = request_body["name"], 
        description = request_body["description"], 
        gravity = request_body["gravity"], 
        distance = request_body["distance"]
    )

    db.session.add(new_planet)
    db.session.commit() 

    return make_response(f"Planet: {new_planet.name} created successfully.", 201)

@planets_bp.route("", methods = ["GET"])
def read_planets(): 

    planet_query = Planet.query # Get a query object for later use 

    # Query planets use name argument 
    name_query = request.args.get("name")
    distance_query = request.args.get("distance")
    gravity_query = request.args.get("gravity")
    # Sort argument passed by client 
    is_sort = request.args.get("sort")

    # Attribute that users want to sort by
    # If it's none, then we sort by name in ascending order by default 
    # atr_to_be_sort = None 

    if name_query:
        planet_query = planet_query.filter_by(name = name_query) 
        # atr_to_be_sort = Planet.name

    if distance_query:
        planet_query = planet_query.filter_by(distance = distance_query)
        # atr_to_be_sort = Planet.distance

    if gravity_query:
        planet_query = planet_query.filter_by(gravity = gravity_query)
        # atr_to_be_sort = Planet.gravity

    if is_sort:
        attribute = None 
        sort_method = is_sort

        split_sort = is_sort.split(":") 

        if len(split_sort) == 2:
            attribute = split_sort[0] 
            sort_method = split_sort[1] 
        if len(split_sort) > 2:
            abort(make_response("Too many parameters", 400))

        # Sort records by client's request 
        if attribute == "name":
            if sort_method == "asc": 
                planet_query = planet_query.order_by(Planet.name.asc()) 
            else:
                planet_query = planet_query.order_by(Planet.name.desc()) 
        elif attribute == "distance":
            if sort_method == "asc": 
                planet_query = planet_query.order_by(Planet.distance.asc()) 
            else:
                planet_query = planet_query.order_by(Planet.distance.desc()) 
        elif attribute == "gravity":
            if sort_method == "asc": 
                planet_query = planet_query.order_by(Planet.gravity.asc()) 
            else:
                planet_query = planet_query.order_by(Planet.gravity.desc()) 
        elif sort_method == "desc":
            planet_query = planet_query.order_by(Planet.name.desc())
        else: # Sort by name in ascending order by default 
            planet_query = planet_query.order_by(Planet.name.asc())

    planets = planet_query.all()
        
    planet_response = [] 
    for planet in planets: 
        planet_response.append(
            {"id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "gravity": planet.gravity, 
            "distance": planet.distance}
        )
    return jsonify(planet_response), 200 

@planets_bp.route("/<planet_id>", methods = ["GET"])
def read_one_planet_by_id(planet_id): 
    planet = validate_planet_id(planet_id) 

    return ({
        "id" : planet.id,
        "name" : planet.name, 
        "description" : planet.description,
        "gravity": planet.gravity, 
        "distance": planet.distance
    }, 200)  

@planets_bp.route("/<planet_id>", methods = ["PUT"])
def update_planet_by_id(planet_id):
    planet = validate_planet_id(planet_id) 

    request_body = request.get_json() 
    validate_request_body(request_body)

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.gravity = request_body["gravity"]
    planet.distance = request_body["distance"]

    db.session.commit() 

    return (f"Planet: {planet_id} has been updated successfully.", 200) 

@planets_bp.route("/<planet_id>", methods = ["DELETE"])
def delete_planet_by_id(planet_id): 
    planet = validate_planet_id(planet_id)  

    db.session.delete(planet)
    db.session.commit()

    return (f"Planet: {planet_id} has been deleted successfully.", 200) 


# ----------------------- Hard coded routes for practice and notes ------------------------------
# class Planets:
#     def __init__(self, id, name, description, gravity):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.gravity = gravity

#     def to_dict(self): 
#         return {
#             "id": self.id,
#             "name": self.name,
#             "description": self.description,
#             "gravity": self.gravity
#         }


# planets = [
#     Planets(1, "Mercury",
#             "The smallest planet in our solar system and nearest to the Sun.", "3.7 m/s^2"),
#     Planets(2, "Earth", "The third planet from the Sun", "9.807 m/s^2"),
#     Planets(3, "Jupiter", "The largest planet in the solar system", "24.79 m/s^2")
# ]

# planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


# @planets_bp.route("", methods=["GET"])
# def planets_json():
#     planets_response = []
#     for planet in planets:
#         planets_response.append({
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description,
#             "gravity": planet.gravity
#         })
#     return jsonify(planets_response), 200


# def planet_validation(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"Message": "Planet id must be an integer."}, 401))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet

#     abort(make_response({"Message": f"Planet {planet_id} not found."}, 404))


# @planets_bp.route("/<planet_id>", methods=["GET"])
# def get_planet_by_id(planet_id):
#     planet = planet_validation(planet_id)
#     return jsonify(planet.to_dict()), 200

# @planets_bp.route("/name/<planet_name>", methods=["GET"])
# def get_planet_by_name(planet_name):
#     for planet in planets: 
#         if planet.name.lower() == planet_name.lower(): 
#             return jsonify(planet.to_dict()), 200

#     abort(make_response({"Message": f"Planet {planet_name} not found."}, 404))

# ----------------------- Hard coded routes for practice and notes ------------------------------
