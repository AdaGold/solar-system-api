from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "GET":
        name_query = request.args.get("name")
        description_query = request.args.get("description")
        moon_query = request.args.get("moons")
        if name_query:
            planets = Planet.query.filter(Planet.name.ilike('%'+name_query+'%'))
        elif description_query:
            planets = Planet.query.filter(Planet.description.ilike('%'+\
                description_query+'%'))
        elif moon_query:
            planets = Planet.query.filter_by(moons=moon_query)
        else:
            planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "moons": planet.moons
            })
        return jsonify(planets_response)
    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
        description=request_body["description"],
        moons=request_body["moons"])
    
        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} successfully created", 201)


@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet is None:
        return make_response(f"Planet {planet_id} not found", 404)
    if request.method == "GET":
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "moons": planet.moons
        }
    elif request.method == "PUT":
        request_body = request.get_json()
        planet.name = request_body["name"]
        planet.description = request_body["description"]
        planet.moons = request_body["moons"]
        db.session.commit()
        return make_response (f"Planet {planet.name} successfully updated", 200)
    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return {
            "Message": f"Planet with name {planet.name} has been deleted."
        }, 200




# planets = [
#     Planet(1, "Mercury", "the smallest planet in our solar system and closest \
#         to the Sun", 0),
#     Planet(2, "Venus","Venus spins slowly in the opposite direction from most \
#         planets. A thick atmosphere traps heat in a runaway greenhouse effect, \
#         making it the hottest planet in our solar system.", 0),
#     Planet(3, "Earth"," It's also the only planet in our solar system with liquid \
#         water on the surface.", 1),
#     Planet(4, "Mars","Mars is a dusty, cold, desert world with a very thin \
#         atmosphere.", 2),
#     Planet(5, "Jupiter","Jupiter is more than twice as massive than the other \
#         planets of our solar system combined.", 79),
#     Planet(6, "Saturn", "Adorned with a dazzling, complex system of icy rings, \
#         Saturn is unique in our solar system.", 62),
#     Planet(7, "Uranus", "Uranus rotates at a nearly 90-degree angle from the plane of its \
#         orbit. This unique tilt makes Uranus appear to spin on its side.", 27),
#     Planet(8, "Neptune", "Neptune is dark, cold and whipped by supersonic winds.", \
#         14)

# ]