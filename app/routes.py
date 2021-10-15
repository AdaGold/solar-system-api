from flask import Blueprint

class Planet:
    def __init__(self, id, name, description, radius_size):
        self.id = id
        self.name = name
        self.description = description
        self.radius_size = radius_size

planets = [
    Planet(1, "Jupiter", "The fifth planet from our Sun and is the largest planet in the solar system.","43,441 mi"),
    Planet(2, "Saturn", "The most distant planet that can be seen with the naked eye.", "36,184 mi" ),
    Planet(3, "Mars", "The fourth planet from the Sun and is a dusty, cold, desert world with a very thin atmosphere", "2,10.61 mi")
] 