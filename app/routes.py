from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["POST","GET"])
def get_planets():
    if request.method == "POST":
        request_body = request.get_json()
        
        if "title" not in request_body or "description" not in request_body:
            return make_response("Invalid Request",400)


        new_planet = Planet(title=request_body["title"],
                        description=request_body["description"])

        db.session.add(new_planet)
        db.session.commit()

        return make_response(f" Planet {new_planet.title} successfully created", 201)


    elif request.method == "GET":
        title_query = request.args.get("title")

        if title_query:
            planet = Planet.query.filter_by(title=title_query)

            planet_response = {
                "id": planet.id,
                "title": planet.title,
                "description": planet.description,
                "color": planet.color
                }

            return jsonify(planet_response),200


        planets = Planet.query.all()
        planet_responses = []

        for planet in planets:
            planet_responses.append(
                {
                    "id": planet.id,
                    "title": planet.title,
                    "description": planet.description,
                    "color": planet.color
                }
            )
        return jsonify(planet_responses)
        
@planets_bp.route("/<planet_id>",methods=["GET","PUT"])
def get_planet(planet_id):
    planet = Planet.query.get(planet_id)
    
    if request.method == "GET":
        return{
            "id":planet.id,
            "title":planet.title,
            "description":planet.description

                }
    elif request.method == "PUT":
        form_data = request.get_json()

        planet.title = form_data["title"]
        planet.description = form_data["description"]

        db.session.commit()

        return make_response(f"planet {planet.id} successfully updated")

    elif request.method == "DELETE": 
        db.session.delete(planet)
        db.session.commit()
        return {
            "Message": f"planet with id {planet_id} has abeen deleted"
    }




