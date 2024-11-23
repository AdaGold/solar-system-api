from sqlalchemy.orm import Mapped, mapped_column
from app.db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    diameter: Mapped[int] #in kilometers
    number_of_moons: Mapped[int]
    
    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            diameter=self.diameter,
            number_of_moons=self.number_of_moons
        )






