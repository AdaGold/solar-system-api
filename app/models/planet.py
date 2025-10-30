from sqlalchemy.orm import Mapped, mapped_column
from ..db import db
class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    size: Mapped[str]
    moons: Mapped[int]
    has_flag: Mapped[bool]


    def to_dict(self):
        return {
                "id" : self.id,
                "name" : self.name,
                "description" : self.description,
                "size" : self.size,
                "moons" :self.moons,
                "has_flag" : self.has_flag
            }
