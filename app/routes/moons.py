from flask import Blueprint, jsonify, abort, make_response,request
from app.models.moon import Moon
from app.models.planet import Planet

from app import db
from app.routes.helpers import validate_model

moons_bp = Blueprint("moons_bp", __name__, url_prefix="/moons")

def moon_validate_request_body(request_body):
    if not request_body:
        msg = "An empty or invalid json object was sent."
        abort(make_response(jsonify({"details":msg}),400))

    name = request_body.get("name")
    description = request_body.get("description")
    size = request_body.get("size")
    gravity = request_body.get("gravity")

    if not name:
        msg = "Request body must include name."
        abort(make_response(jsonify({"details":msg}),400))

    if not description:
        msg = "Request body must include description."
        abort(make_response(jsonify({"details":msg}),400))

    if size is None:
        msg = "Request body must include size."
        abort(make_response(jsonify({"details":msg}),400))

    if gravity is None:
        msg = "Request body must include gravity."
        abort(make_response(jsonify({"details":msg}),400))

    return request_body

@moons_bp.route("",methods=["POST"])
def create_moon():
    request_body = request.get_json(silent=True) 
    new_moon = Moon.from_dict(moon_validate_request_body(request_body))

    db.session.add(new_moon)
    db.session.commit()

    return make_response(jsonify(f"moon {new_moon.name} successfully created"), 201)

@moons_bp.route("",methods=["GET"])
def get_all_moons():
    moon_query = Moon.query  
    
    name_query = request.args.get("moon_name")
    if name_query:
        moon_query = moon_query.filter(moon.name.ilike(f"%{name_query}%"))

    sort_query = request.args.get("sort")
    if sort_query:
        if sort_query == "desc":
            moon_query = moon_query.order_by(moon.name.desc())
        else:
            moon_query = moon_query.order_by(moon.name.asc())

    moons = moon_query.all()
    moons_response = []
    for moon in moons:
        moons_response.append(moon.to_dict())
    return jsonify(moons_response)
                
@moons_bp.route("/<moon_id>",methods=["GET"])
def get_moon(moon_id):
    moon_info = validate_model(Moon, moon_id)
    return jsonify(moon_info.to_dict())

@moons_bp.route("/<moon_id>",methods=["PUT"])
def update_moon(moon_id):
    moon_info = validate_model(Moon, moon_id)
    request_body = request.get_json(silent=True)  
    moon_validate_request_body(request_body)

    moon_info.name = request_body["name"]
    moon_info.description= request_body["description"]
    moon_info.size = request_body["size"]

    db.session.commit()
    
    return make_response(jsonify(f"moon {moon_info.name} successfully updated"), 200)

@moons_bp.route("/<moon_id>",methods=["DELETE"])
def delete_moon(moon_id):
    moon_info = validate_model(Moon, moon_id)
    
    db.session.delete(moon_info)
    db.session.commit()
    
    return make_response(jsonify(f"moon {moon_info.name} successfully deleted"), 200)
