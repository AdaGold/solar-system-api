class Moon:
    def __init__(self, id, name, description):
        self.id=id
        self.name=name
        self.description=description
        

moons_list = []
first_mon = Moon(1, "Moon", "Earths Moon")
moons_list.append(first_mon)