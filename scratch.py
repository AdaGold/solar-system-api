###########################
###########################
########planet.py##########
###########################
#########__init__.py#######
###########################
#########routes.py#########
###########################
# import json # maybe don't need 
# from unicodedata import name # maybe don't need

# planets = [
#     Planet(1, "Mercury", "rocky", 1),
#     Planet(2, "Venus", "rocky", 2),
#     Planet(3, "Earth", "water", 3),
#     Planet(4, "Mars", "red", 4),
#     Planet(5, "Jupiter", "big", 5),
#     Planet(6, "Saturn", "rings", 6),
#     Planet(7, "Uranus", "butt", 7),
#     Planet(8, "Neptune", "ice", 8),
#     Planet(9, "Pluto", "dwarf", 9)
# ]

# class Planet:
#     # def __init__(self, id, name, description, dist_from_sun):
#     #     self.id = id
#     #     self.name = name
#     #     self.description = description
#     #     self.dist_from_sun = dist_from_sun

#     def to_dict(self):
#         return {
#             "id" : self.id,
#             "name" : self.name,
#             "description" : self.description,
#             "distance from sun" : self.dist_from_sun
#         }

# from delete_planet_by_id endpoint
# planet_list = []
    # for planet in planets:
    #     planet_list.append({
    #     "id" : planet.id,
    #     "name" : planet.name,
    #     "description" : planet.description,
    #     "distance from sun" : planet.dist_from_sun
    #     }
    #     )
    # return jsonify(planet_list)

# @planets_bp.route("/<planet_id>", methods = ["GET"])
# def get_planet_by_id(planet_id):
#     planet = validate_planet(planet_id)
#     return planet.to_dict()

# from validate_planet() helper function
    # for planet in planets:
    #     if planet.id == planet_id:
    #         return planet











###########################
