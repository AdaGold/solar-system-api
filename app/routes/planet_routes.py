from flask import Blueprint, abort, make_response, request, Response
from app.db import db 
from app.models.planet import Planet
from constants import ID, NAME, DESCRIPTION, NUMBER_OF_MOONS, ORDER_BY, MESSAGE, MIMETYPE_JSON, INVALID, NOT_FOUND

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()

    new_planet = Planet(
        name=request_body[NAME],
        description=request_body[DESCRIPTION],
        number_of_moons=request_body[NUMBER_OF_MOONS]
    )
    
    db.session.add(new_planet)
    db.session.commit()

    return new_planet.to_dict(), 201

@planets_bp.get("")
def get_all_planets():
    query_params = get_query_params()
    query = db.select(Planet)
    query = filter_query(query, query_params)
    query = get_order_by_param(query)

    planets = db.session.scalars(query)

    return [planet.to_dict() for planet in planets]

@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    return validate_planet(planet_id).to_dict()

@planets_bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.name = request_body[NAME]
    planet.description = request_body[DESCRIPTION]
    planet.number_of_moons = request_body[NUMBER_OF_MOONS]

    db.session.commit()

    return Response(status=204, mimetype=MIMETYPE_JSON)

@planets_bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype=MIMETYPE_JSON)

def filter_query(query, params):
    if params[ID]:
        query = query.where(Planet.id == validate_cast_type(params[ID], int, ID))

    if params[NAME]:
        query = query.where(Planet.name == params[NAME])

    if params[DESCRIPTION]:
        query = query.where(Planet.description.ilike(f"%{params[DESCRIPTION]}%"))

    if params[NUMBER_OF_MOONS]:
        query = query.where(Planet.number_of_moons == validate_cast_type(
            params[NUMBER_OF_MOONS], int, NUMBER_OF_MOONS))
        
    return query

def get_query_params():
    return {
        ID: request.args.get(ID),
        NAME: request.args.get(NAME),
        DESCRIPTION: request.args.get(DESCRIPTION),
        NUMBER_OF_MOONS: request.args.get(NUMBER_OF_MOONS)
    }

def get_order_by_param(query):
    order_by_param = request.args.get(ORDER_BY)
    if order_by_param:
        query = validate_order_by_param(query, order_by_param)
    else:
        query = query.order_by(Planet.id)

    return query

def validate_cast_type(value, target_type, param_name):
    try:
        return target_type(value)
    except (ValueError, TypeError):
        abort(make_response({MESSAGE: f"{param_name} '{value}' {INVALID}"}, 400))

def validate_order_by_param(query, order_by_param):
    try:
        return query.order_by(getattr(Planet, order_by_param))
    except AttributeError:
        abort(make_response({MESSAGE: f"{ORDER_BY} '{order_by_param}' {INVALID}"}, 400))

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        abort(make_response({MESSAGE: f"{ID} {planet_id} {INVALID}"}, 400))

    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.scalar(query)

    if not planet:
        abort(make_response({MESSAGE: f"{ID} {planet_id} {NOT_FOUND}"}, 404))
    
    return planet