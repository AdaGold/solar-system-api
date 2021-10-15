from flask import Blueprint

class Planet:
    def __init__(self,id, name, description, number_of_moons):
        self.id = id
        self.name = name
        self.description = description
        self.number_of_moons = number_of_moons

planets =[Planet(1,'Earth', 'water planet', 1),]

