from app import db
from app.models import planet
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


''' Helper functions - check if is_valid_integer'''

def valid_int(number, parameter_type):
    try:
        int(number)
    except:
        abort(make_response({"error": f'{parameter_type} must be an integer'}, 400))


def get_planet_from_id(planet_id):
    valid_int(planet_id, "planet_id")
    return Planet.query.get_or_404(planet_id, description='{Planet not found}')


''' Routes: planets'''

@planets_bp.route("", methods =["POST"])
def create_planets():
    form_data = request.get_json()


    if "title" not in form_data or "planet_type" not in form_data or "description" not in form_data or "moons" not in form_data:
        return {"error": "incomplete request body"}, 400

    new_planet = Planet(title=form_data["title"], 
                        planet_type= form_data["planet_type"],
                        description=form_data["description"],
                        moons = form_data["moons"])


    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet { new_planet.title} successfully created", 201)



@planets_bp.route("", methods =["GET"])
def read_planets():
# TODO  create logic to handle a 404 error

    planet_title_query = request.args.get("title")
    number_of_moons_query = request.args.get("moons")
    most_moons_query = request.args.get("most")
    planet_type_query = request.args.get("planet_type")
    sort_query = request.args.get("sort")


    if number_of_moons_query:
        valid_int(number_of_moons_query, "moons")
        planets = Planet.query.filter_by(moons=number_of_moons_query)
    elif planet_title_query:
        planets = Planet.query.filter_by(title=planet_title_query)
    elif planet_type_query:
        planets = Planet.query.filter_by(planet_type=planet_type_query)
    elif most_moons_query:
        valid_int(most_moons_query, "most")
        planets = Planet.query.filter(Planet.moons > most_moons_query)
    elif sort_query == "asc":
        planets = Planet.query.order_by(Planet.moons.asc())
    elif sort_query == "desc":
        planets = Planet.query.order_by(Planet.moons.desc())
    else:
        planets = Planet.query.all()

    planet_response = []
    
    if not planets:
        return make_response(f"Planets do not exist: Please Post some Planets into the database", 404)

    for planet in planets:
            planet_response.append(
            planet.to_dict()
        )
    return jsonify(planet_response), 200


@planets_bp.route("/<planet_id>", methods=["GET"])
def get_planet(planet_id):
    planet= get_planet_from_id(planet_id)

    return  planet.to_dict()


@planets_bp.route("/<planet_id>", methods=["PATCH"])
def update_planet(planet_id):
    planet = get_planet_from_id(planet_id)
    form_data = request.get_json()

    if not form_data:
        return {"error": "incomplete request body"}, 400

    if "title" in form_data:
        planet.title = form_data["title"]
    if "planet_type" in form_data:    
        planet.type = form_data["planet_type"]
    if "description" in form_data:
        planet.description = form_data["description"]
    if "moons" in form_data:
        planet.moons = form_data["moons"]


    db.session.commit()
    return make_response(f"Planet {planet.id} successfully updated", 200)

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = get_planet_from_id(planet_id)
    db.session.delete(planet)
    db.session.commit()
    return make_response(f"Planet {planet.id} successfully deleted", 200)
