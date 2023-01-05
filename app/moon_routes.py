from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort


moons_bp = Blueprint("moons", __name__, url_prefix="/moons")