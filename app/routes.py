from flask import Blueprint

class Planet():
    def __init__(self, id, name, description, rings):
        self.id = id
        self.name = name
        self.description = description
        self.rings = rings

planets = [
        Planet(1, "Mercury", "The smallest and fastest planet", False),
        Planet(2, "Venus", "The hottest planet", False),
        Planet(3, "Earth", "The blue marble", False),
        Planet(4, "Mars", "The red planet", False),
        Planet(5, "Jupiter", "The gas giant", False),
        Planet(6, "Saturn", "The second largest planet", True),
        Planet(7, "Uranus", "This planet spins on its side", True),
        Planet(8, "Neptune", "The most distant planet from the sun", False)
        ]

