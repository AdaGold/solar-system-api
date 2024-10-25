from sqlalchemy.orm import Mapped, mapped_column
from app.db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    diameter: Mapped[int]
    number_of_moons: Mapped[int]
    
# def to_dict(self):
#     return dict(
#         id=self.id,
#         name=self.name,
#         description=self.description,
#         diameter=self.diameter,
#         number_of_moons=self.number_of_moons
#     )










# class Planet:
#     def __init__(self, id, name, description, diameter, number_of_moons):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.diameter = diameter
#         self.number_of_moons = number_of_moons
        
#     def to_dict(self):
#         return dict(
#             id=self.id,
#             name=self.name,
#             description=self.description,
#             diameter=self.diameter,
#             number_of_moons=self.number_of_moons
#         )
        
# planets = [
#     Planet(1, "Mercury", "Smallest planet and closest to the Sun.", 4879, 0),
#     Planet(2, "Venus", "Similar to Earth but with a thick, toxic atmosphere.", 12104, 0),
#     Planet(3, "Earth", "The only planet known to support life.", 12742, 1),
#     Planet(4, "Mars", "The Red Planet, known for its volcanoes.", 6779, 2),
#     Planet(5, "Jupiter", "The largest planet, famous for its Great Red Spot.", 139820, 79),
#     Planet(6, "Saturn", "Known for its stunning rings.", 116460, 83),
#     Planet(7, "Uranus", "An ice giant that rotates on its side.", 50724, 27),
#     Planet(8, "Neptune", "The farthest planet, known for strong winds.", 49244, 14),
#     Planet(9, "Pluto", "Dwarf planet known for its complex orbit and atmosphere.", 2376, 5)
# ]