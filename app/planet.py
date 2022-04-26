class Planet():
    def __init__(self, id, name, description, moons = None):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons

    def to_json(self):
        return {
            "id": self.id,
            "name" : self.name,
            "decription": self.description,
            "moons": self.moons
        }
