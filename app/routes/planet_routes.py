from flask import Blueprint, jsonify, request, make_response
from app import db
from app.models.planet import Planet
from app.load_json import load
import jsonschema
from jsonschema import validate
import json

# primitive types: null, boolean, object, array, number, or string
# integer matches any number with a zero fractional part

planet_schema = {
    "title": "Planet Data",
    "description": "Contains planet name, description, and how many moons.",
    "required": ["name", "num_of_moons"],
    "type": ["object"],
    "properties": {
        "name": {
            "type": "string",
        },
        "description": {
            "type": "string",
        },
        "num_of_moons": {
            "type": "number"
        }
    }
}


def validate_json(json_data):
    try:
        validate(instance=json_data, schema=planet_schema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        #return False
    return True

# def make_planet_objects():
#     # loads json data as dictionaries
#     planet_data = load('app/planets.json')
    
#     planets_list = []

#     for planet in planet_data:
#         description = f'{planet["name"]} is the {planet["id"]} planet and has {planet["numberOfMoons"]} moon(s).'
#         planet_object = Planet(planet["id"], planet["name"], description, planet["numberOfMoons"])
#         planets_list.append(planet_object)

#     return planets_list

# planets = make_planet_objects()

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def populate_planets():
    request_body = request.get_json()

    for data in request_body:
        if not validate_json(data):
            return make_response("Invalid response", 404)

        if 'description' in data:
            new_planet = Planet(
                name=data["name"],
                num_of_moons=data["num_of_moons"],
                description=data["description"]
            )
        else:
            new_planet = Planet(
                name=data["name"],
                num_of_moons=data["num_of_moons"],
                description=f'{data["name"]} has {data["num_of_moons"]} moon(s).'
            )
        db.session.add(new_planet)
    db.session.commit()

    return f"Successfully added {[data['name'] for data in request_body]} to Solar System Database", 201

@planets_bp.route("/load-json", methods=["POST"])
def loads_json():
    request_body = request.get_json()
    file_path = request_body["file"]
    new_data = load(file_path)
    for data in new_data:
        if not validate_json(data):
            return make_response("Invalid response", 404)

        if 'description' in data:
            new_planet = Planet(
                name=data["name"],
                num_of_moons=data["num_of_moons"],
                description=data["description"]
            )
        else:
            new_planet = Planet(
                name=data["name"],
                num_of_moons=data["num_of_moons"],
                description=f'{data["name"]} has {data["num_of_moons"]} moon(s).'
            )
        db.session.add(new_planet)
    db.session.commit()

    return f"Successfully added {[data['name'] for data in new_data]} to Solar System Database", 201

    # uploaded_file = request.files['file']
    # print(new_data)
    # Read file from request
    return jsonify(new_data), 200


@planets_bp.route("", methods=["GET"])
def get_planets():
    # query_params = [] TODO: Future
    if request.args.get("name"):
        planets = Planet.query.filter_by(name=request.args.get("name"))
    elif request.args.get("order_by") == "num_of_moons":
        planets = Planet.query.order_by(Planet.num_of_moons)
    else:
        planets = Planet.query.all()

    planets_response = []
    for planet in planets:
        planets_response.append(planet.get_dict())
    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_planet(planet_id):
    # Sanitize input
    try:
        int(planet_id)
    except:
        return jsonify("ID given is not an integer.", 400)

    planet = Planet.query.get_or_404(planet_id)

    if request.method == "GET":
        return jsonify(planet.get_dict()), 200

    elif request.method == "PUT":
        request_body = request.get_json()
        for key, value in request_body.items():
            if key in Planet.__table__.columns.keys():
                setattr(planet, key, value)

    # col_names = ObjectName.__table__.columns.keys()
    # required_values = {name: getattr(sample_row, name) for name in col_names}

        
        db.session.commit()

        return jsonify(planet.get_dict()), 201

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()

        return jsonify({"message": f"Deleted {planet.name} with {planet.id}"}), 200