class Planet:
    def __init__(self, id, name, description, is_rocky):
        self.id = id
        self.name = name
        self.description = description
        self.is_rocky = is_rocky

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "is_rocky" : self.is_rocky
        }
