from flask import Blueprint, abort, make_response, request, Response
from app.models.planet import Planet
from app.db import db
from sqlalchemy import desc

planets_bp = Blueprint("planets_bp", __name__, url_prefix=("/planets"))


ORDER_BY_MAP = {
'id': Planet.id, 
'name': Planet.name, 
'description': Planet.description, 
'moons': Planet.moons,
"size": Planet.size,
"has_flag": Planet.has_flag
}



@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body['name']
    description = request_body['description']
    size = request_body['size']
    moons = request_body['moons']
    has_flag = request_body['has_flag']

    new_planet = Planet(name=name, description=description, size = size, moons = moons, has_flag = has_flag)
    db.session.add(new_planet)
    db.session.commit()

    response_body = new_planet.to_dict()

    return response_body, 201

@planets_bp.get("")
def get_all_planets():
    all_params = request.args
    query = db.select(Planet)

    if all_params.get("name"):
        query = query.where(Planet.name.ilike(f"%{all_params.get("name")}%"))
    
    if all_params.get("description"):
        query = query.where(Planet.description.ilike(f"%{all_params.get("description")}%"))

    if all_params.get("size"):
        query = query.where(Planet.size.ilike(f"%{all_params.get("size")}%"))
    
    if all_params.get("moons"):
        # query = query.where(Planet.moons == all_params.get("moons"))
        query = query.filter(Planet.moons >= all_params.get("moons"))

    if all_params.get("has_flag"):
        query =query.where(Planet.has_flag == all_params.get("has_flag"))

    if all_params.get("order_by"):
        attribute = all_params.get("order_by")
        if all_params.get("dir") == "desc":
            query = query.order_by(desc(ORDER_BY_MAP[attribute]))
        else:
            query = query.order_by(ORDER_BY_MAP[attribute])
    else:
        query = query.order_by(Planet.id)

    planets = db.session.scalars(query)

    response_body=[]
    for planet in planets:
        response_body.append(planet.to_dict())
    
    return response_body, 200

# all of the query param logic needs validation


@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet_id(planet_id)

    return planet.to_dict(), 200



@planets_bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_planet_id(planet_id)
    request_body = request.get_json()

    planet.name = request_body['name']
    planet.description = request_body['description']
    db.session.commit()

    return Response(status=204, mimetype="application/json")

@planets_bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_planet_id(planet_id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")


# Helper Functions
def validate_planet_id(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        response = {"msg": f"Planet id {planet_id} is invalid."}
        abort(make_response(response,400))
    
    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.scalar(query)

    if not planet:
        response = {"msg": f"Planet id {planet_id} not found."}
        abort(make_response(response,404))

    return planet