from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "GET":
        name_query = request.args.get("name")
        if name_query:
            planets = Planet.query.filter(Planet.name.contains(f"%{name_query}%"))
        else:
            planets = Planet.query.all()

        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "cycle_len": planet.cycle_len
            })
        return jsonify(planets_response)

    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name = request_body["name"], 
                        description = request_body["description"], 
                        cycle_len = request_body["cycle_len"])
        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} successfully created", 201)
@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_planet(planet_id):
    planet = Planet.query.get(planet_id)

    if planet is None:
        return make_response("Planet not found.", 404)

    elif request.method == "GET":
        return {"id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "cycle_len": planet.cycle_len}

    elif request.method == "PUT":
        request_body = request.get_json()
        planet.name = request_body["name"]
        planet.description = request_body["description"]
        planet.cycle_len = request_body["cycle_len"]
        db.session.commit()
        return make_response("Planet successfully updated.", 200)

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return make_response("Planet successfully deleted.", 200)
        
