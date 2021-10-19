from flask import Blueprint, jsonify
from app.satellites_class import Satellite
from app.load_json import load
import pprint

satellite_data = load('app/satellites.json')

def make_satellites_objects():
    satellites_list = []

    for satellite in satellite_data:
        description = f'{satellite["name"]} is the {satellite["id"]} satellite that belongs to {satellite["planetId"]}.'
        satellite_object = Satellite(satellite["name"], satellite["id"], satellite["planetId"], description)
        satellites_list.append(satellite_object)

    return satellites_list

satellites = make_satellites_objects()
satellite_bp = Blueprint("satellites", __name__, url_prefix="/satellites")

@satellite_bp.route("/", methods=["GET"])
def handle_satellites():
    satellites_response = []
    for satellite in satellites:
        satellites_response.append({
            "id" : satellite.id,
            "name": satellite.name,
            "planet_id": satellite.planet_id,
            "description": satellite.description
        })
    return jsonify(satellites_response)

@satellite_bp.route("/<satellite_id>", methods=["GET"])
def handle_satellite(satellite_id):
    satellite_id = int(satellite_id)

    satellite_response = {}

    for satellite in satellites:
        print(f"{satellite_id=}")
        print(f"{satellite.id=}")
        if satellite_id == satellite.id:
            print(satellite.name)
            satellite_response["id"] = satellite.id
            satellite_response["name"] = satellite.name
            satellite_response["planet_id"] = satellite.planet_id
            satellite_response["description"] = satellite.description

    return jsonify(satellite_response)