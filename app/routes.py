from flask import Blueprint

planet_bp = Blueprint("planet_bp", __name__)


@planet_bp.route("/planets/sass", methods=["GET"])
def be_sassy():
    return "I'm a planet and you're not."