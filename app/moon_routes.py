from app import db
from app.models.moon import Moon
from app.route_helper_funcs import validate_model, validate_moon
from flask import Blueprint, jsonify, make_response, request, abort


moons_bp = Blueprint("moons", __name__, url_prefix="/moons")


@moons_bp.route("", methods=["GET"])
def get_all_moon():
    moons = Moon.query.all()
    moons_response = list()
    for moon in moons:
        moons_response.append(moon.to_dict())
    return jsonify(moons_response)


@moons_bp.route("/<moon_id>", methods=["GET"])
def get_moon_by_id(moon_id):
    moon = validate_model(Moon, moon_id)
    return moon.to_dict()


@moons_bp.route("/<moon_id>", methods=["DELETE"])
def delete_a_moon(moon_id):
    moon = validate_model(Moon, moon_id)
    db.session.delete(moon)
    db.session.commit()
    return moon.to_dict(), 200
