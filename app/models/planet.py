from sqlalchemy.orm import Mapped, mapped_column
from app.db import db
from constants import ID, NAME, DESCRIPTION, NUMBER_OF_MOONS

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] 
    description: Mapped[str]
    number_of_moons: Mapped[int]

    def to_dict(self):
        return {
            ID: self.id, 
            NAME: self.name,
            DESCRIPTION: self.description,
            NUMBER_OF_MOONS: self.number_of_moons
        }