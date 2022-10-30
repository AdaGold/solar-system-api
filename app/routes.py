from flask import Blueprint, jsonify, abort, make_response, request
from app.models.planet import Planet
from app import db


bp = Blueprint("planets", __name__, url_prefix="/planets")


@bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        rings=request_body["rings"])
    
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} succesfully created", 201)

@bp.route.route("", methods=["POST"])
def update_planet():
    request_body = request.get_json()
    new_planet = Planet(title=request_body["name"],
                    description=request_body["description"],
                    rings=request_body["rings"])



    db.session.add(new_planet)
    db.session.commit()

@bp.route("/guide/<id>", methods=["DELETE"])
def planet_delete(id):
    request_body = request.get_json()
    planet_delete = Planet(title=request_body["name"],
                    description=request_body["description"],
                    rings=request_body["rings"])

    return make_response(f"Planet {planet_delete} successfully deleted", 201)
