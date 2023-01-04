from flask import Blueprint, jsonify, abort, make_response,request
from app.models.planet import Planet
from app import db

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

def validate_request_body(request_body):
    if not request_body:
        msg = "An empty or invalid json object was sent."
        abort(make_response(jsonify({"message":msg}),400))

    name = request_body.get("name")
    description = request_body.get("description")
    is_rocky = request_body.get("is_rocky")

    if not name:
        msg = "Request body must include name."
        abort(make_response(jsonify({"details":msg}),400))

    if not description:
        msg = "Request body must include description."
        abort(make_response(jsonify({"details":msg}),400))

    if is_rocky is None:
        msg = "Request body must include is_rocky."
        abort(make_response(jsonify({"details":msg}),400))

    return request_body

@planets_bp.route("",methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(validate_request_body(request_body))

    db.session.add(new_planet)
    db.session.commit()

    return make_response(jsonify(f"Planet {new_planet.name} successfully created"), 201)

@planets_bp.route("",methods=["GET"])
def get_all_planets():
    planet_query = Planet.query  
    
    name_query = request.args.get("planet_name")
    if name_query:
        planet_query = planet_query.filter(Planet.name.ilike(f"%{name_query}%"))

    sort_query = request.args.get("sort")
    if sort_query:
        if sort_query == "desc":
            planet_query = planet_query.order_by(Planet.name.desc())
        else:
            planet_query = planet_query.order_by(Planet.name.asc())

    planets = planet_query.all()
    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_dict())
    return jsonify(planets_response)

def validate_model(cls, model_id):
    print(cls, model_id)
    try:
        model_id = int(model_id)
    except:
        msg = f"{cls.__name__} id {model_id} is Invalid"
        abort(make_response({"message" : msg },400))

    model = cls.query.get(model_id)    

    if model:
        return model

    abort(make_response({"message":f"{cls.__name__} id {model_id} is Not Found" },404))
                
@planets_bp.route("/<planet_id>",methods=["GET"])
def get_planet(planet_id):
    planet_info = validate_model(Planet, planet_id)
    return jsonify(planet_info.to_dict())

@planets_bp.route("/<planet_id>",methods=["PUT"])
def update_planet(planet_id):
    planet_info = validate_model(Planet, planet_id)
    request_body = request.get_json()
    validate_request_body(request_body)

    planet_info.name = request_body["name"]
    planet_info.description= request_body["description"]
    planet_info.is_rocky = request_body["is_rocky"]

    db.session.commit()
    
    return make_response(jsonify(f"Planet {planet_info.name} successfully updated"), 200)

@planets_bp.route("/<planet_id>",methods=["DELETE"])
def delete_planet(planet_id):
    planet_info = validate_model(Planet, planet_id)
    
    db.session.delete(planet_info)
    db.session.commit()
    
    return make_response(jsonify(f"Planet {planet_info.name} successfully deleted"), 200)