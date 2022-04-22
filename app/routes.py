from flask import Blueprint

class Planet:
    def __init__(self, id, name, description, dist_from_sun):
        self.id = id
        self.name = name
        self.description = description
        self.dist_from_sun = dist_from_sun

planets = [
    Planet(1, "Mercury", "rocky", 1),
    Planet(2, "Venus", "gaseous", 2),
    Planet(3, "Earth", "water", 3),
    Planet(4, "Mars", "red", 4),
    Planet(5, "Jupiter", "big", 5),
    Planet(6, "Saturn", "rings", 6),
    Planet(7, "Uranus", "butt", 7),
    Planet(8, "Neptune", "blue", 8),
    Planet(9, "Pluto", "dwarf", 9)
]