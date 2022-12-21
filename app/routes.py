from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name=request_body["name"],
        description=request_body["description"],
        feature=request_body["feature"]
    )
    db.session.add(new_planet)
    db.session.commit()
    return make_response(f"Book {new_planet} successfully created", 201)
            

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    planets_response = []
    planets = Planet.query.all()
    for planet in planets:
        planets_response.append(
            {
                "name": planet.name,
                "description": planet.description,
                "feature": planet.feature
            }
        )
    return jsonify(planets_response)

