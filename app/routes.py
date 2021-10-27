from flask import Blueprint, jsonify, make_response, request
from app import db
from app.models.planet import Planet


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["GET", "POST"])
def find_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "color": planet.color
            })
        return jsonify(planets_response)

    elif request.method == "POST":
        request_body = request.get_json()
        if "name" not in request_body or "description" not in request_body:
            return jsonify("Not Found"), 404

        new_planet = Planet(name=request_body["name"], description=request_body["description"], color=request_body["color"])

        db.session.add(new_planet)
        db.session.commit()

        return jsonify(f"Planet {new_planet.name} successfully created"), 201


@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def find_planet(planet_id):
    planet_id = int(planet_id)
    planet = Planet.query.get(planet_id)

    if planet is None:
        return jsonify("Not Found"), 404

    if request.method == "GET":
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "color": planet.color
        }

    elif request.method == "PUT":
        request_body = request.get_json()

        planet.name = request_body["name"]
        planet.description = request_body["description"]
        planet.color = request_body["color"]

        db.session.commit()
        return jsonify(f"Planet {planet.name} successfully updated"), 200

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return jsonify(f"Planet {planet.name} successfully deleted"), 200