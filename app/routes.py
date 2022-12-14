from flask import Blueprint, jsonify
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def display_planets():
    return "Test Planets"
    

    

