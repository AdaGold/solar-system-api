from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods = ["GET"])
def read_all_planets():
    planets_response = []
    query_params = request.args.to_dict()

    if query_params:
        query_params = {k.lower(): v.title() for k, v in query_params.items()}
        planets = Planet.query.filter_by(**query_params).all()
    else:
        planets = Planet.query.all()

    planets_response = [planet.planet_to_dict() for planet in planets]
    return jsonify(planets_response)


@planets_bp.route("", methods = ["POST"])
def create_planets():
    request_body = request.get_json()
    try:
        new_planet = Planet.create_new_planet(request_body)
        db.session.add(new_planet)
        db.session.commit()

        message = f"Planet {new_planet.name} successfully created"
        return make_response(jsonify(message), 201)

    except KeyError as e:
        abort(make_response(f"Invalid request. Missing required value: {e}"), 400)


@planets_bp.route("/<id>", methods=["GET"])
def read_one_planet(id):
    planet = validate_model(Planet, id)
    planet = Planet.query.get(id)
    return jsonify(planet.planet_to_dict()), 200

@planets_bp.route("/<id>", methods=["PUT"])
def update_planet(id):
    planet = validate_model(Planet, id)
    
    planet.update(request.get_json())

    db.session.commit()
    message = f"Planet #{id} successfully updated"
    return make_response(jsonify(message))
          
@planets_bp.route("/<id>", methods=["DELETE"])
def delete_planet(id):
    planet= validate_model(Planet, id)

    db.session.delete(planet)
    db.session.commit()

    message = f"Planet #{id} successfully deleted"
    return make_response(jsonify(message), 200)
def validate_model(cls, id):
     try:
         id = int(id)
     except:
         message = f"{cls.__name__} {id} is invalid"
         abort(make_response({"message": message}, 400))

     model = cls.query.get(id)

     if not model:
         message = f"{cls.__name__} {id} not found"
         abort(make_response({"message": message}, 404))

     return model


