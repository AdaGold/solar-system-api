from app.db import db
from sqlalchemy.orm import Mapped, mapped_column

# class Planet:
#     def __init__(self, id, name, description, moons):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.moons = moons

    # vvv don't delete, we'll use this vvv
    # def to_dict(self):
    #     return {
    #         "id": self.id, 
    #         "name": self.name,
    #         "description": self.description,
    #         "moons": self.moons
    #     }

# planets = [
#     Planet(1, "Mercury", "Small, hot, fast", []),
#     Planet(2, "Venus", "Thick atmosphere", []),
#     Planet(3, "Earth", "Supports life, very watery", ["Moon"]),
#     Planet(4, "Mars", "Red planet, biggest volcano", ["Phobos", "Deimos"])
# ]

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] 
    description: Mapped[str]
    number_of_moons: Mapped[int]

