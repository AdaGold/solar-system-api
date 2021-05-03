# from flask import Blueprint

# planet_bp = Blueprint("planet blueprint", __name__)

# @planet_bp.route("/models/planet", methods=["POST"])
# def create_planet():
#     planet_response_body = "boom! planet successfully created"
#     return planet_response_body




from app import db
from app.models.planet import Planet
from flask import request, Blueprint, make_response, jsonify
planet_bp = Blueprint("planet", __name__, url_prefix="/planets")
# endpoint for user to retrieve all planet data & create planet
@planet_bp.route("", methods=["GET","POST"])
def handle_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description
            })
        return jsonify(planets_response)
    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
                        description=request_body["description"])
        db.session.add(new_planet)
        db.session.commit()
        return make_response(f"Planet {new_planet.name} successfully created", 201)


# @planet_bp.route("/<planet_id>", methods=["GET", "DELETE"])
# def handle_planet(planet_id):

    # planet_id = Planet.query.get(planet_id)

    # if request.method == "GET":
    #     if planet_id == Planet.query.get(planet_id):
    #         return {
    #             "id": planet.id,
    #             "name": planet.name,
    #             "description": planet.description
    #         }
    #     else:
    #         return make_response("planet does not exist")
    
# endpoint for user to gather planet info based on actual planet id 
@planet_bp.route("/<planet_id>", methods=["GET", "DELETE","PUT"])
def handle_planet(planet_id):
    planet = Planet.query.get(planet_id)
    # if the request method is GET, return planet id, name & description 
    if request.method == "GET":
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description
        }
    # if the request method is DELETE, delete the planet with the planet id user has indicated & print success message
    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return make_response(f"Planet #{planet.id} successfully deleted")

    elif request.method == "PUT":
        form_data = request.get_json()
        #planet is referencing our planet id that was given by the user in http request
        planet.name = form_data["name"]
        planet.description = form_data["description"]

        db.session.commit()

        return make_response(f"Planet #{planet.name} successfully updated") 