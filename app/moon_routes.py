from app import db
from app.models.moon import Moon
from app.route_helper_funcs import validate_model, validate_moon
from flask import Blueprint, jsonify, make_response, request, abort


moons_bp = Blueprint("moons", __name__, url_prefix="/moons")


@moons_bp.route("", methods=["POST"])
def create_moon():
    request_body = request.get_json()
    validate_request = validate_moon(request_body)
    if validate_request:
        abort(make_response(jsonify(validate_request), 400))
    new_moon = Moon.from_dict(request_body)
    db.session.add(new_moon)
    db.session.commit()
    db.session.refresh(new_moon)
    return new_moon.to_dict(), 201


@moons_bp.route("", methods=["GET"])
def get_all_moon():
    moons = Moon.query.all()
    moons_response = list()
    for moon in moons:
        moons_response.append(moon.to_dict())
    return jsonify(moons_response)


@moons_bp.route("/<moon_id>", methods=["GET"])
def get_moon_by_id(moon_id):
    moon = validate_model(moon_id)
    return moon.to_dict()

