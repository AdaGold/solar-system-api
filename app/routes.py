from flask import Blueprint

planet_bp = Blueprint("planet_bp", __name__)


@planet_bp.route("/planets", methods=["GET"])
def get_planet_info():
    return "I'm a planet and you're not."