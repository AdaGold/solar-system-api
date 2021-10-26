from flask import Blueprint, jsonify, request, make_response
from app import db
from app.models.planet import Planet
from app.load_json import load
import jsonschema
from jsonschema import validate
import json

# loads json data as dictionaries
#planet_data = load('app/planets.json')

# primitive types: null, boolean, object, array, number, or string
# integer matches any number with a zero fractional part

planet_schema = {
    "title": "Planet Data",
    "description": "Contains planet name, description, and how many moons.",
    "required": ["name", "description", "num_of_moons"],
    "type": "object",
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
        return False
    return True

# def make_planet_objects():
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
    if not validate_json(request_body):
        return make_response("Invalid response", 404)

    new_planet = Planet(
        name=request_body["name"],
        description=request_body["description"],
        num_of_moons=request_body["num_of_moons"]
    )
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Successfully added {new_planet.name} to Solar System Database", 201)


@planets_bp.route("", methods=["GET"])
def get_planets():
    planets = Planet.query.all()
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "num_of_moons": planet.num_of_moons
        })
    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_planet(planet_id):
    # Sanitize input
    try:
        int(planet_id)
    except:
        return jsonify("ID given is not an integer.", 400)

    # planet_id = int(planet_id)
    planet = Planet.query.get(planet_id)

    if request.method == "GET":
        return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "num_of_moons": planet.num_of_moons
                }

    elif request.method == "PUT":
        request_body = request.get_json()
        if not validate_json(request_body):
            return jsonify("Invalid request.", 400)
        
        planet.name = request_body["name"]
        planet.description = request_body["description"]
        planet.num_of_moons = request_body["num_of_moons"]

        db.session.commit()

        return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "num_of_moons": planet.num_of_moons
                }

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()

        return jsonify({"message": f"Deleted {planet.name} with {planet.id}"}), 200