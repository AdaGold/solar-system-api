from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "POST":
        request_body = request.get_json()
        if "name" not in request_body or "description" not in request_body or "distance_from_sun_in_million_mi" not in request_body or "moon_count" not in request_body:
            # make_response is used to create header
            # jsonify use for send data response
            return make_response("Invalid Request", 400)

        new_planet = Planet(
            name=request_body["name"],
            description=request_body["description"],
            distance_from_sun_in_million_mi=request_body["distance_from_sun_in_million_mi"],
            moon_count=request_body["moon_count"]
        )
        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"{new_planet.name} is created", 201)


    elif request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append(
                {
                    "id": planet.id,
                    "name": planet.name,
                    "description": planet.description,
                    "distance_from_sun_in_million_mi": planet.distance_from_sun_in_million_mi,
                    "moon_count": planet.moon_count
                }
            )
        return jsonify(planets_response)



@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = Planet.query.get(planet_id)

    if planet is None:
        return make_response(f"Planet {planet_id} not found", 404)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "distance_from_sun_in_million_mi": planet.distance_from_sun_in_million_mi,
        "moon_count": planet.moon_count
    }
