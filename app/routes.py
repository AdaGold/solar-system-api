from flask import abort, Blueprint, jsonify, request
from app.models.planet import Planet
from app import db

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_data = request.get_json()

    if "name" not in request_data or "description" not in request_data \
        or "proximity" not in request_data:
        return jsonify({"message": "Missing data"}), 400

    new_planet = Planet(name=request_data["name"], description=request_data["description"],
                proximity=request_data["proximity"])
    
    db.session.add(new_planet)
    db.session.commit()

    return f"Planet {new_planet.name} created", 201

@planets_bp.route("", methods=["GET"])
def list_all_planets():
    planets_response = []
    #Can't be jsonified
    if request.args.get("description"):
        planets = Planet.query.filter_by(description=request.args.get("description"))
    else:
        planets = Planet.query.all()
    for planet in planets:
        planets_response.append(planet.to_dict())
    return jsonify(planets_response), 200

@planets_bp.route("/<id>", methods=["GET", "PUT"])
def handle_planet(planet_id):
    print(planet_id)
    planet_id = int(planet_id)
    planet = Planet.query.get(planet_id)
    if not planet:
        return{ "Error": f"Planet {planet_id} was not found"}, 404

    if request.method == "GET":
        return jsonify(planet.to_dict()), 200
    elif request.method == "PUT":
        input_data = request.get_json()
        input_data = sanitize_data(input_data)
        planet.name = input_data["name"]
        planet.description = input_data["description"]
        planet.proximity = input_data["proximity"]
        db.session.commit()
        return jsonify(planet.to_dict()), 200

def sanitize_data(input_data):
    data_types = {"name": str, "description": str, "proximity": str}
    for name, val_type in data_types.items():
        try:
            val = input_data[name]
            val_type(val)
        except Exception as e:
            print(e)
            abort(400, "Bad Data")
    return input_data


@planets_bp.route("/<id>", methods=["DELETE"])
def delete_planet(planet_id):
    print(planet_id)
    try:
        planet_id = int(planet_id)
    except ValueError:
        return {"Error": "ID must be a number"}, 404
    planet = Planet.query.get(planet_id)

    if planet:
        db.session.delete(planet)
        db.session.commit()
        return {"Success": f"Deleted Planet {planet_id}"}, 200
    else:
        return {"Error": f" No Planet with ID matching {planet_id}"}, 404
