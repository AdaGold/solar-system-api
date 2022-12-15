class Planet:
    def __init__(self, id, name, description, is_rocky):
        self.id = id
        self.name = name
        self.description = description
        self.is_rocky = is_rocky

    def to_dict(self):
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "is_rocky" : planet.is_rocky
        }
