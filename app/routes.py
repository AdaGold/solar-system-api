from flask import Blueprint, jsonify, make_response, request
from app import db
from app.models.planet import Planet

planets_bp = Blueprint('planets', __name__, url_prefix='/planets')

@planets_bp.route('', methods=["POST", "GET"])
def get_planets():
    if request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(
            name=request_body["name"],
            description=request_body["description"],
            radius_size=request_body["radius_size"])

        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} successfully created", 201)

    elif request.method == "GET":
        name_from_url = request.args.get('name')
        description_from_url = request.args.get('description')
        radius_size_from_url = request.args.get('radius_size')

        if name_from_url:
            # planets = Planet.query.filter_by(name=name_from_url)
            # Filter allows for more complex search queries/more customizable
            planets = Planet.query.filter(Planet.name.contains(name_from_url))
        elif description_from_url:
            planets = Planet.query.filter_by(description=description_from_url)
        elif radius_size_from_url:
            planets = Planet.query.filter_by(radius_size=radius_size_from_url)
        else:
            planets = Planet.query.all()
        
        planets_response =[]
        for planet in planets:
            planets_response.append({
                'id':planet.id,
                'name':planet.name,
                'description':planet.description,
                'radius_size':planet.radius_size
            })
        return jsonify(planets_response)

@planets_bp.route('/<planet_id>', methods=['GET', 'PUT', 'DELETE'])
def get_specific_planet(planet_id):
    planet = Planet.query.get(planet_id)
    
    if planet is None:
        return make_response(f"Planet {planet_id} not found", 404)
    
    elif request.method == "GET":
        return {
        'id':planet.id,
        'name':planet.name,
        'description':planet.description,
        'radius_size':planet.radius_size
        }
    
    elif request.method == 'PUT':
        request_body = request.get_json()

        planet.name = request_body["name"]
        planet.description = request_body["description"]
        planet.radius_size = request_body["radius_size"]

        db.session.commit()

        return make_response(f"Planet {planet.name} was successfully updated")

    elif request.method == 'DELETE':
        db.session.delete(planet)
        db.session.commit()
        return make_response(f"Planet {planet.name} was successfully deleted")