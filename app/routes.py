from flask import Blueprint

class Planet:
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color 
        
planets = [
    Planet(1, "mercury", "the littlest planet", "gray"),
    Planet(2, "venus", "the hottest planet", "maroon"),
    Planet(3, "earth", "the liveliest planet", "green"),
    Planet(4, "mars", "the reddest planet", "red" ),
    Planet(5, "jupiter", "the biggest planet", "orange"),
    Planet(6, "saturn", "the ring planet", "yellow"),
    Planet(7, "uranus", "the most sidways planet", "purple"),
    Planet(8, "neptune", "the boring planet", "blue"),
]

