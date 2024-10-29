from sqlalchemy.orm import Mapped, mapped_column
from app.db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] 
    description: Mapped[str]
    number_of_moons: Mapped[int]

    def to_dict(self):
        return {
            "id": self.id, 
            "name": self.name,
            "description": self.description,
            "number_of_moons": self.number_of_moons
        }