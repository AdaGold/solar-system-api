from flask import Blueprint, jsonify
from .satellites_class import Satellite
from .load_json import load
import pprint

satellite_data = load('app/satellites.json')

def make_satellites_objects():
    satellites_list = []

    for satellite in satellite_data:
        description = f'{satellite["name"]} is the {satellite["id"]} satellite that belongs to {satellite["planet_id"]}.'
        satellite_object = satellite(satellite["id"], satellite["name"], description, satellite["planet_id"])
        satellites_list.append(satellite_object)

    return 

satellites = make_satellites_objects()
satellite_bp = Blueprint("satellites", __name__, url_prefix="/satellites")
