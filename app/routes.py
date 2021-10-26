from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planet_bp = Blueprint("planet", __name__, url_prefix="/planets")


@planet_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append(planet.to_json())
        return jsonify(planets_response)
    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(
            name=request_body["name"],
            description=request_body["description"],
            color=request_body["color"],
        )

        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} successfully created", 201)


@planet_bp.route("/<planet_id>", methods=["GET", "PUT"])
def handle_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if request.method == "GET":
        return planet.to_json()
    elif request.method == "PUT":
        form_data = request.get_json()

        planet.name = form_data["name"]
        planet.description = form_data["description"]
        planet.color = form_data["color"]

        db.session.commit()

        return make_response(f"Planet #{planet.id} successfully updated")
