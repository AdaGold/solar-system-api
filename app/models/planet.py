
class Planet:
    def __init__(self, id, name, description, flag= bool):
        self.id = id
        self.name = name
        self.description = description
        self.flag = flag


planets = [
    Planet(1, "Mercury", "The smallest planet in our solar system.", False),

    Planet(2, "Venus", "The hottest planet in the solar system.", False), 
    Planet(3, "Earth", "The only planet known to support life.", True ), 
    Planet(4, "Mars", "Known as the Red Planet.", True ), 
    Planet(5, "Jupiter", "The largest planet in our solar system.", False)
]   