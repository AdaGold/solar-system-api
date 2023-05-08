from app import db 
from app.models.planet import Planet
from app.models.moon import Moon
from flask import Blueprint, jsonify, abort, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        message = f"{cls.__name__} {model_id} is invalid"
        abort(make_response({"message" : message}, 400))
    
    model = cls.query.get(model_id)
    
    if not model:
        message = f"{cls.__name__} {model_id} not found"
        abort(make_response({"message": message}, 404))
    
    return model

#route functions
@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    try:
        new_planet = Planet.from_dict(request_body)
        db.session.add(new_planet)
        db.session.commit()

        message = f"Planet {new_planet.name} successfully created"
        return make_response(message, 201)
    
    except KeyError as e:
        abort(make_response({"message": f"missing required value: {e}"}, 400))

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    name_query = request.args.get("name")
    description_query = request.args.get("description")
    if name_query:
        planets = Planet.query.filter_by(name = name_query)
    elif description_query:
        planets = Planet.query.filter_by(description = description_query)
    else:
        planets = Planet.query.all()

    results = [planet.to_dict() for planet in planets]
    return jsonify(results)

@planets_bp.route("<planet_id>/moons", methods=["GET"])
def read_moons(planet_id):
    planet = validate_model(Planet, planet_id)

    planet_response = []
    for moon in planet.moons:
        planet_response.append(moon.to_dict())

    return(jsonify(planet_response))



@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    return planet.to_dict()

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet_data = request.get_json()
    planet_to_update = validate_model(Planet, planet_id)
    
    planet_to_update.name = planet_data["name"]
    planet_to_update.description = planet_data["description"]
    planet_to_update.distance = planet_data["distance"]
    
    db.session.commit()

    return make_response(f"Planet {planet_to_update.name} succesfully updated", 200)

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)
        
    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet_id} succesfully deleted")


@planets_bp.route("<planet_id>/moons", methods=["POST"])
def create_moon(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()
    try:
        new_moon = Moon.from_dict(request_body)
        new_moon.planet = planet

        db.session.add(new_moon)
        db.session.commit()

        return make_response(jsonify(f"Moon {new_moon.name} cared by {planet.name} successfully created"), 201)
    except KeyError as e:
        abort(make_response({"message": f"missing required value: {e}"}, 400))