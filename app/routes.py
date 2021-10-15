from flask import Blueprint

class Planet:
    def __init__(self,id, name, description, number_of_moons):
        self.id = id
        self.name = name
        self.description = description
        self.number_of_moons = number_of_moons

planets = [
            Planet(1,'Earth', 'water planet', 1), 
            Planet(2, 'Mercury', 'fastest', 0),
            Planet(3, 'Jupiter', 'biggest', 79),
            Planet(4, 'Saturn', 'gaseous', 82),
            Planet(5, 'Mars', 'red', 2),
            Planet(6, 'Uranus', 'coldest', 27),
            Planet(7, 'Neptune', 'farthest from the sun', 14),
            Planet(8, 'Venus', 'hottest', 0)
          ]

