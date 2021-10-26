from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "POST":
        # get request body
        request_body = request.get_json()
        if "name" not in request_body or "description" not in request_body or "distance_from_sun_in_million_mi" not in request_body or "moon_count" not in request_body:
            return jsonify("Invalid Request"), 400

        new_planet = Planet(
            name=request_body["name"],
            description=request_body["description"],
            distance_from_sun_in_million_mi=request_body["distance_from_sun_in_million_mi"],
            moon_count=request_body["moon_count"]
        )

        # collect changes and sent to database
        db.session.add(new_planet)
        db.session.commit()

        return jsonify(f"{new_planet.name} is created"), 201
    elif request.method == "GET":
        query = request.args.get("name")
        if query:
            # planets = Planet.query.filter(Planet.name.contains(query))
            planets = Planet.query.filter_by(name=query)
        else:
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


@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_planet(planet_id):
    planet = Planet.query.get(planet_id)
    # planet = Planet.query.get_or_404(planet_id)

    if planet is None:
        return jsonify(f"Planet {planet_id} not found"), 404

    if request.method == "GET":
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "distance_from_sun_in_million_mi": planet.distance_from_sun_in_million_mi,
            "moon_count": planet.moon_count
        }
    elif request.method == "PUT":
        if planet is None:
            return jsonify(f"Planet {planet_id} is not found"), 404

        request_body = request.get_json()
        if "name" not in request_body or "description" not in request_body or "distance_from_sun_in_million_mi" not in request_body or "moon_count" not in request_body:
            return jsonify(f"Invalid Request"), 400

        planet.name = request_body["name"]
        planet.description = request_body["description"]
        planet.distance_from_sun_in_million_mi = request_body["distance_from_sun_in_million_mi"]
        planet.moon_count = request_body["moon_count"]

        db.session.commit()

        return jsonify(f"Planet {planet_id} was successfully updated"), 201

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return jsonify(f"Planet {planet_id} is deleted"), 200
