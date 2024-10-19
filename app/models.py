class Planet:
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color

planets = [
    Planet(1, "Mercury", "The closest planet to the Sun.", "Gray"),
    Planet(2, "Venus", "The second planet from the Sun.", "Yellowish-white"),
    Planet(3, "Earth", "The third planet from the Sun.", "Blue and green"),
    Planet(4, "Mars", "The fourth planet from the Sun.", "Red"),
    Planet(5, "Jupiter", "The largest planet in the solar system.", "Brown and white striped"),
    Planet(6, "Saturn", "Known for its rings.", "Pale gold"),
    Planet(7, "Uranus", "An ice giant with a blue color.", "Light blue"),
    Planet(8, "Neptune", "The furthest planet from the Sun.", "Deep blue"),
]