from flask import Blueprint

class Planet:
    def __init__(self,id,name,description,temperature):
        self.id = id
        self.name = name
        self.description = description
        self.temperature = temperature

planets = [
    Planet(1,"Jupiter",)
]