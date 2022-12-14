from .moon import Moon, moons_list
class Planet:
    def __init__(self, id, name, description, has_rings=False, moons=None):
        self.id=id
        self.name=name
        self.description=description
        self.has_rings=has_rings
        self.moons = moons if moons else []
