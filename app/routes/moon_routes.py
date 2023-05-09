from app import db
from app.models.moon import Moon
from app.models.planet import Planet
from app.routes.planet_routes import validate_model
from flask import Blueprint, jsonify, abort, make_response, request

moons_bp = Blueprint("moons", __name__, url_prefix="/moons")


@moons_bp.route("", methods = ["GET"])
def read_all_moons():
    moons_response = []
    query_params = request.args.to_dict()

    if query_params:
        query_params = {k.lower(): v.title() for k, v in query_params.items()}
        moons = Moon.query.filter_by(**query_params).all()
    else:
        moons = Moon.query.all()

    moons_response = [moon.moon_to_dict() for moon in moons]
    return jsonify(moons_response)

@moons_bp.route("", methods=["POST"])
def create_moon():
    # Retrieve the request body
    request_body = request.get_json()

    # Validate the request body
    if not request_body:
        return make_response(jsonify({"error": "Request body must be provided"}), 400)
    if "name" not in request_body:
        return make_response(jsonify({"error": "Name field is required"}), 400)

    # Create a new Moon instance
    new_moon = Moon(
        name=request_body["name"]
    )

    # Add the new Moon instance to the database session
    db.session.add(new_moon)
    db.session.commit()

    # Return a JSON response indicating success
    return make_response(jsonify({"message": f"New moon '{new_moon.name}' created"}), 201)