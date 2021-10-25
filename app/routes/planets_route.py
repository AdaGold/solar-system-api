from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")



@planets_bp.route("", methods =["POST"])
def create_planets():
    request_body = request.get_json()
    new_planet = Planet(title=request_body["title"], 
                        planet_type= request_body["planet_type"],
                        description=request_body["description"],
                        moons = request_body["moons"])


    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet { new_planet.title} successfully created", 201)



@planets_bp.route("", methods =["GET"])
def read_planets():
    planets =  Planet.query.all()
    planet_response = []

    for planet in planets:
        planet_response.append({
            "id": planet.id,
            "title": planet.title,
            "description": planet.description,
            "planet_type": planet.planet_type,
            "moons": planet.moons,
        })
    
    return jsonify(planet_response), 200



@planets_bp.route("/<planet_id>", methods=["GET"])
def get_planet(planet_id):
    planet =  Planet.query.filter_by(id=planet_id).first()

    return {
        "title": planet.title,
        "description": planet.description,
        "planet_type": planet.planet_type,
        "moons": planet.moons,
    }, 200
    