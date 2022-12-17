class Moon:
    def __init__(self, id, name, description, planet_id):
        self.id=id
        self.name=name
        self.description=description
        self.planet_id = planet_id
        
    
    def get_siblings_moons(self):
        siblings_moons = []
        for moon in moons_list:
            if moon.planet_id == self.planet_id:
                siblings_moons.append(moon)
        return siblings_moons
                

moons_list = []
first_mon = Moon(1, "Luna", "Earths Moon", 3)
moons_list.append(first_mon)
second_moon = Moon(2,"Phobos", "Moon of mars discovered in 1877", 4)
third_moon = Moon(3, "Deimos", "Second moon of mars discovered in 1877", 4)
forth_moon = Moon(4, "Io", "discovered in 1610", 5)
fifth_moon = Moon(5, "Europa", "discovered 1610", 5)
sixth_moon = Moon(6, "Ganymede", "discovered 1610", 6)
seventh_moon = Moon(7, "Callisto", "Discovered 1610", 5)
eigth_moon = Moon(8, "Amalthea", "Discovered in 1982", 5)
moons_list.append(second_moon)
moons_list.append(third_moon)
moons_list.append(forth_moon)
moons_list.append(fifth_moon)
moons_list.append(sixth_moon)
moons_list.append(seventh_moon)
moons_list.append(eigth_moon)
