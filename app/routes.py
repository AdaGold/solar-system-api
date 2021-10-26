from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planet_bp.route("", methods=["GET", "POST"])
def get_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "moon": planet.moon
            })
        return jsonify(planets_response)
    if request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
        description = request_body["description"],
        moon = request_body["moon"])

    db.session.add(new_planet)
    db.session.commit()

    new_planet_response = {
        "id": new_planet.id,
        "name": new_planet.name,
        "description": new_planet.description,
        "moon": new_planet.moon
        }

    return make_response(new_planet_response, 201)

@planet_bp.route("/<id>", methods=["GET", "PUT", "DELETE"])
def single_planet(id):
    id = int(id)
    planet = Planet.query.get(id)
    if planet is None:
        return make_response("", 404)
    if request.body == "GET":
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "moon": planet.moon
            }
    if request.method == "PUT":
        form_data = request.get_json()

        planet.name = form_data["name"]
        planet.description = form_data["description"]
        planet.moon = form_data["moon"]

        db.session.commit()
    if request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return make_response(f"Planet #{planet.id} successfully deleted")
