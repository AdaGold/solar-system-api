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
        not in request_body or "distance_from_earth" not in request_body:

        abort(make_response("Invalid Request", 400))

def sort_helper(planet_query, atr = None, sort_method = "asc"): 
    if sort_method == "asc" and atr: 
        planet_query = planet_query.order_by(atr.asc())
    elif sort_method == "desc" and atr: 
        planet_query = planet_query.order_by(atr.desc())
    elif sort_method == "desc": 
        planet_query = planet_query.order_by(Planet.name.desc())
    else:
        #Sort by name in ascending order by default 
        planet_query = planet_query.order_by(Planet.name.asc())

    return planet_query

# ---------------------------------------------- Route Functions ----------------------------------------------
@planets_bp.route("", methods = ["POST"])
def create_planet(): 
    request_body =  request.get_json()
    validate_request_body(request_body)
    #use from_dict function to simplfied code
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit() 

    return make_response(jsonify(f"Planet: {new_planet.name} created successfully."), 201)

@planets_bp.route("", methods = ["GET"])
def read_planets(): 

    planet_query = Planet.query # Get a query object for later use 

    # Query planets use name argument 
    name_query = request.args.get("name")
    distance_query = request.args.get("distance_from_earth")
    gravity_query = request.args.get("gravity")
    # Sort argument passed by client 
    is_sort = request.args.get("sort")

    if name_query:
        planet_query = planet_query.filter_by(name = name_query) 

    if distance_query:
        planet_query = planet_query.filter_by(distance_from_earth = distance_query)

    if gravity_query:
        planet_query = planet_query.filter_by(gravity = gravity_query)

    if is_sort:
        attribute = None 
        sort_method = is_sort

        split_sort = is_sort.split(":") 

        if len(split_sort) == 2: # Case: ?sort=attribute:asc 
            attribute = split_sort[0] 
            sort_method = split_sort[1] 
        if len(split_sort) > 2: 
            abort(make_response("Too many parameters", 400))

        # Sort records by client's request 
        if attribute == "name":
            planet_query = sort_helper(planet_query, Planet.name, sort_method)
        elif attribute == "distance_from_earth":
            planet_query = sort_helper(planet_query, Planet.distance_from_earth, sort_method)
        elif attribute == "gravity":
            planet_query = sort_helper(planet_query, Planet.gravity, sort_method)
        else: # If user don't specify any attribute, we would sort by name 
            planet_query = sort_helper(planet_query, Planet.name, sort_method)

    planets = planet_query.all()
        
    planet_response = [] 
    for planet in planets: 
        planet_response.append(planet.to_dict())    #use to_dict function to make code more readable

    return make_response(jsonify(planet_response), 200)

@planets_bp.route("/<planet_id>", methods = ["GET"])
def read_one_planet_by_id(planet_id): 
    planet = validate_planet_id(planet_id) 
    #use to_dict function to make code more readable
    return (planet.to_dict(), 200)  

@planets_bp.route("/<planet_id>", methods = ["PUT"])
def update_planet_by_id(planet_id):
    planet = validate_planet_id(planet_id) 

    request_body = request.get_json() 
    validate_request_body(request_body)

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.gravity = request_body["gravity"]
    planet.distance_from_earth = request_body["distance_from_earth"]

    db.session.commit() 

    return make_response(jsonify(f"Planet: {planet_id} has been updated successfully."), 200) 

@planets_bp.route("/<planet_id>", methods = ["DELETE"])
def delete_planet_by_id(planet_id): 
    planet = validate_planet_id(planet_id)  

    db.session.delete(planet)
    db.session.commit()

    return make_response(jsonify(f"Planet: {planet_id} has been deleted successfully."), 200) 
