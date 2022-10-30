from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request 

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                    description=request_body["description"],
                    moons=request_body["moons"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)


@planets_bp.route("", methods=["GET"])
def read_all_planets():
    planets_response = []
    planets = Planet.query.all()
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "moons": planet.moons
            }
        )
    return jsonify(planets_response)


# @books_bp.route("", methods=["GET"])
# def get_all_books():
#     books_response = [vars(planet) for planet in PLANETS] 

#     return jsonify(books_response)


# @books_bp.route("/<book_id>", methods=["GET"])
# def get_one_book(book_id):
#     book = validate_book(book_id)

#     return book

# def validate_book(book_id):
#     try:
#         book_id = int(book_id)
#     except ValueError:
#         return {
#             "message": "invalid planet id"
#         }, 400

#     for book in BOOKS:
#         if book.id == book_id:
#             return vars(book)

#     abort(make_response(jsonify(description="Resource not found"), 404))



# class Planet:
#     def __init__(self, id, name, description):
#         self.id = id
#         self.name = name
#         self.description = description
    
# PLANETS = [
#     Planet(1, "Mercury", "The smallest planet in our solar system and nearest to the Sun,\
#         Mercury is only slightly larger than Earth's Moon."),
#     Planet(2, "Earth", "Our home planet is the third planet from the Sun, and the only place we know of so far\
#         that is inhabited by living things."),
#     Planet(3, "Venus", "Venus is the second planet from the Sun and is Earths closest planetary neighbor."),
#     Planet(4, "Mars", "Mars is the fourth planet from the Sun, a dusty, cold, desert world with a very thin atmosphere."),
#     Planet(5, "Jupiter", "Fifth in line from the Sun, Jupiter is, by far, the largest planet in the solar system\
#         more than twice as massive as all the other planets combined."),
#     Planet(6, "Saturn", "Saturn is the sixth planet from the Sun and the second-largest planet in our solar system."),
#     Planet(7, "Uranus", "Uranus is the seventh planet from the Sun, and has the third-largest diameter in our solar system."),
#     Planet(8, "Neptune", "Dark, cold, and whipped by supersonic winds, ice giant Neptune is the eighth and most distant\
#         planet in our solar system."),
#     ]

# planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

# @planets_bp.route("", methods=["GET"])
# def get_all_planets():
#     planets_response = [vars(planet) for planet in PLANETS] 

#     return jsonify(planets_response)

# @planets_bp.route("<planet_id>", methods=["GET"])    
# def get_one_planet(planet_id):
#     planet = validate_planet(planet_id)

#     return planet
    
# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except ValueError:
#         return {
#             "message": "invalid planet id"
#         }, 400

#     for planet in PLANETS:
#         if planet.id == planet_id:
#             return vars(planet)

#     abort(make_response(jsonify(description="Resource not found"), 404))
