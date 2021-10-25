from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

# planets = [
#     Planet(1, "mercury", "the littlest planet", "gray"),
#     Planet(2, "venus", "the hottest planet", "maroon"),
#     Planet(3, "earth", "the liveliest planet", "green"),
#     Planet(4, "mars", "the reddest planet", "red"),
#     Planet(5, "jupiter", "the biggest planet", "orange"),
#     Planet(6, "saturn", "the ring planet", "yellow"),
#     Planet(7, "uranus", "the most sidways planet", "purple"),
#     Planet(8, "neptune", "the boring planet", "blue"),
# ]

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


# localhost:5000/planets/<planet_id>
@planet_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    if request.method == "GET":
        planet = Planet.query.get(planet_id)
        return planet.to_json()


#    planets_return = []
#    for planet in planets:
#        planets_return.append(planet.to_json())
#    return jsonify(planets_return)


# one_planet_bp = Blueprint("one_planet", __name__, url_prefix="/planet")
# http://127.0.0.1:5000/planet/<planet_id>
# @one_planet_bp.route("/<planet_id>", methods=["GET"])
# def one_planet(planet_id):
#    planet_id = int(planet_id)
#    for planet in planets:
#        if planet.id == planet_id:
#            return planet.to_json()
