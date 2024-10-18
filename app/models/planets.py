class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
        

planets = [
    Planet(1, "Mercury", "Smallest planet and closest to the Sun."),
    Planet(2, "Venus", "Similar to Earth but with a thick, toxic atmosphere."),
    Planet(3, "Earth", "The only planet known to support life."),
    Planet(4, "Mars", "The Red Planet, known for its volcanoes."),
    Planet(5, "Jupiter", "The largest planet, famous for its Great Red Spot."),
    Planet(6, "Saturn", "Known for its stunning rings."),
    Planet(7, "Uranus", "An ice giant that rotates on its side."),
    Planet(8, "Neptune", "The farthest planet, known for strong winds.")
]