from flask import Blueprint

class Planet:
    def __init__(self, id, name, description, cycle_len):
        self.id = id
        self.name = name
        self.description = description
        self.cycle_len = cycle_len

planets = [
    Planet(1, "Earth", "blue marble", 365),
    Planet(2, "Saturn", "ringed planet", 10220),
    Planet(3, "Mars", "musty, dusty and cold", 780),
    Planet(4, "Mercury", "teeny tiny", 88)
]

