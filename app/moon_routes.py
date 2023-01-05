from app import db
from app.models.planet import Planet
from app.models.moon import Moon
from flask import Blueprint, jsonify, make_response, request, abort


moons_bp = Blueprint("moons", __name__, url_prefix="/moons")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except: 
        abort(make_response({"message": f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message": f"{cls.__name__} {model_id} is not found"}, 404))
    return model


def validate_moon(planet):
    invalid_dict = dict()
    if "name" not in planet or not isinstance(planet["name"], str) or planet["name"] is None:
        invalid_dict["details"] = "Request body must include name."
    if "size" not in planet or not isinstance(planet["size"], int) or planet["size"] is None:
        invalid_dict["details"] = "Request body must include size."
    if "description" not in planet or not isinstance(planet["description"], str) or \
        planet["description"] is None:
        invalid_dict["details"] = "Request body must include description."
    if "distance_from_earth" not in planet or not isinstance(planet["distance_from_earth"]) or \
        planet["distance_from_earth"] is None:
        invalid_dict["details"] = "Request body must include distance_from_earth."
    return invalid_dict

@moons_bp.route("", methods=["POST"])
def create_moon():
    moon_data = request.get_json()
    new_moon = Moon.from_dict(moon_data)

    db.session.add(new_moon)
    db.session.commit()

    return make_response(f"Caretaker {new_moon.name} created", 201)

@moons_bp.route("", methods=["GET"])
def get_moon_optional_query():
    moon_query = Moon.query

    sort_query = request.args.get("sort")
    if sort_query:
        if sort_query == "desc":
            moon_query = moon_query.order_by(Moon.size.desc())
        else:
            moon_query = moon_query.order_by(Moon.size.asc())

    moons = moon_query.all()
    moon_response = []
    for moon in moons:
        moon_response.append(moon.to_dict())

    return jsonify(moon_response)

@moons_bp.route("/<caretaker_id>", methods=["GET"])
def get_moon_by_id(moon_id):
    caretaker_to_return = validate_model(Moon, moon_id)

    return jsonify(caretaker_to_return.to_dict())

@moons_bp.route("/<moon_id>/moons", methods=["POST"])
def add_new_planet_to_moon(moon_id):
    moon = validate_model(Moon, moon_id)

    request_body = request.get_json()
    new_planet = Moon.from_dict(request_body)
    new_planet.moon = moon

    db.session.add(new_planet)
    db.session.commit()

    message = f"Planet {new_planet.name} created with Moon {moon.name}"
    return make_response(jsonify(message), 201)

@moons_bp.route("/<moon_id>/planets", methods=["GET"])
def get_all_planet_for_moon(moon_id):
    moon = validate_model(Moon, moon_id)

    planet_response = []
    for planet in moon.planets:
        planet_response.append(planet.to_dict())

    return jsonify(planet_response)