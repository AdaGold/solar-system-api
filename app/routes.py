from flask import Blueprint

class Planet:
    def __init__(self, id, name, description, dist_from_sun):
        self.id = id
        self.name = name
        self.description = description
        self.dist_from_sun = dist_from_sun
