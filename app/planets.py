from .moon import Moon, moons_list
class Planet:
    def __init__(self, id, name, description, has_rings=False, moons=None):
        self.id=id
        self.name=name
        self.description=description
        self.has_rings=has_rings
        self.moons = moons if moons else []


solar_system=[]
mercurey = Planet(1, "Mercury", "First Planet near the Sun")
solar_system.append(mercurey)
venus = Planet(2, "Venus", "Second Planet from the sun")
solar_system.append(venus)
earth = Planet(3, "Earth", "Has Humans", False, [moons_list[0]])
solar_system.append(earth)
mars= Planet(4, "Mars", "Being explored by robots, considered for space colony")
solar_system.append(mars)
jupiter = Planet(5, "Jupiter", "Largest Gas Giant", has_rings=True)
solar_system.append(jupiter)
saturn = Planet(6, "Saturn", "Gas Giant", has_rings=True)
solar_system.append(saturn)
uranus = Planet(7, "Uranus", "Smells bad", has_rings=True)
neptune = Planet(8, "Neptue", "Named for the god of the sea because it is blue", has_rings=True)