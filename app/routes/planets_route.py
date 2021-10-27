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
    request_body = request.get_json()

    if "title" not in request_body or "planet_type" not in request_body or "description" not in request_body or "moons" not in request_body:
        return {"error": "incomplete request body"}, 400

    new_planet = Planet(title=request_body["title"], 
                        planet_type= request_body["planet_type"],
                        description=request_body["description"],
                        moons = request_body["moons"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet { new_planet.title} successfully created", 201)



@planets_bp.route("", methods =["GET"])
def read_planets():

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

    for planet in planets:
        planet_response.append({
            "id": planet.id,
            "title": planet.title,
            "description": planet.description,
            "planet_type": planet.planet_type,
            "moons": planet.moons,
        })   
    return jsonify(planet_response), 200


@planets_bp.route("/<planet_id>", methods=["GET"])
def get_planet(planet_id):
   #ADD404 IF STATEMENT
    planet =  Planet.query.filter_by(id=planet_id).first()
    
    if not planet:
        return make_response(f"Planet: {planet_id}  not found", 404)
    else:
        return {
            "title": planet.title,
            "description": planet.description,
            "planet_type": planet.planet_type,
            "moons": planet.moons,
        }, 200
        
@planets_bp.route("/<planet_id>", methods=["PATCH"])
def update_planet(planet_id):
    planet = Planet.query.get(planet_id)
    form_data = request.get_json()

    planet.title = form_data["title"]
    planet.description = form_data["description"]

    db.session.commit()
    return make_response(f"Planet {planet.id} successfully updated", 200)

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = Planet.query.get(planet_id)
    db.session.delete(planet)
    db.session.commit()
    return make_response(f"Planet {planet.id} successfully deleted", 200)
