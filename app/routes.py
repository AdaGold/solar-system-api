from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "GET":
        planet_from_url = request.args.get("name")
        
        if planet_from_url is not None:
            planets = Planet.query.filter(Planet.name.contains(planet_from_url))
        else:
            planets = Planet.query.all()
        
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "color" : planet.color
            })
        return jsonify(planets_response)

    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        color=request_body["color"])
        db.session.add(new_planet)
        db.session.commit()
        return make_response(
        f"Planet {new_planet.name} created", 201
    )

            

@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def get_single_planet(planet_id):
    planet = Planet.query.get(planet_id)

    if planet is None:
        return make_response("Error" , 404)
    
    if request.method == "GET":
        return {    "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "color": planet.color
            }
    
    if request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return make_response(f"Planet #{planet.id} with planet name {planet.name} successfully deleted")
    
    if request.method == "PUT":
        request_body = request.get_json()
        try:
            planet.name = request_body['name']
            planet.description = request_body['description']

            db.session.add(planet)
            db.session.commit()
            return {    
                "id": planet.id,
                "name": planet.name,
                "description": planet.description
                }
        except KeyError:
            return {
                "message" : "requre both name and description"
                }, 400


