from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

# planets_db = {
#     1: {"name": "Mercury", "description": "1st planet from the Sun", "color": "light blue"},
#     2: {"name": "Venus", "description": "2nd planet from the Sun", "color": "orange"},
#     3: {"name": "Earth", "description": "3rd planet from the Sun", "color": "black"},
#     4: {"name": "Mars", "description": "4th planet from the Sun", "color": "red"},
#     5: {"name": "Jupiter", "description": "5th planet from the Sun", "color": "green"},
#     6: {"name": "Saturn", "description": "6th planet from the Sun", "color": "purple"},
#     7: {"name": "Uranus", "description": "7th planet from the Sun", "color": "dark blue"},
#     8: {"name": "Neptune", "description": "8th planet from the Sun", "color": "aqua"},
# }

# planets = [
#     Planet(1, "Mercury", "1st planet from the Sun", "light blue"),
#     Planet(2, "Venus", "2nd planet from the Sun", "orange"),
#     Planet(3, "Earth", "3rd planet from the Sun", "black"),
#     Planet(4, "Mars", "4th planet from the Sun", "red"),
#     Planet(5, "Jupiter", "5th planet from the Sun", "green"),
#     Planet(6, "Saturn", "6th planet from the Sun", "purple"),
#     Planet(7, "Uranus", "7th planet from the Sun", "dark blue"),
#     Planet(8, "Neptune", "8th planet from the Sun", "aqua"),
# ]

bp = Blueprint("planets", __name__, url_prefix="/planets")

# ______________________________________________
def validate_planet(id):
    try:
        id = int(id)
    except:
        abort(make_response({"message": f"Planet {id} is invalid."}, 400))

    planet = Planet.query.get(id)

    if not planet:
        abort(make_response({"message": f"Planet {id} not found."}, 404))

    return planet

@bp.route("", methods=["GET"])
def read_all_planets():
    planets = Planet.query.all()
    planets_list = []
    for planet in planets:
        planets_list.append(planet.make_dict())

    return jsonify(planets_list), 200   

@bp.route("/<id>", methods=["GET"])
def read_one_planet(id):
    planet = validate_planet(id)
    
    return planet.make_dict(), 200

@bp.route("", methods=["POST"])
def create_planet():
    if request.method == "POST":
        request_body = request.get_json()
        if "name" not in request_body or "description" not in request_body or "color" not in request_body:
            return make_response("Invalid Request", 400)

        new_planet = Planet(
            name = request_body["name"],
            description = request_body["description"],
            color = request_body["color"]
            )

        db.session.add(new_planet)
        db.session.commit()

        return make_response(
            f"Planet {new_planet.name} successfully created", 201
        )
    
@bp.route("/<id>", methods=["PUT"])
def update_planet(id):
    planet = validate_planet(id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.color= request_body["color"]
    
    db.session.commit()

    return make_response(
        f"Planet #{id} successfully updated", 200
    )

@bp.route("/<id>", methods=["DELETE"])
def delete_planet(id):
    planet = validate_planet(id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f'Planet #{id} successfully deleted'), 200