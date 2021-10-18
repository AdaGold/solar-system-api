from flask import Blueprint
import load_json
import pprint

# loads json data as dictionaries
planet_data = load_json.load('planets.json')
satellite_data = load_json.load('satellites.json')

