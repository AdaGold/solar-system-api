from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    color = db.Column(db.String)
    description = db.Column(db.String)
    moons = db.relationship("Moon", back_populates="planets")

    def to_dict(self):
        return dict(
            id=self.id,
            name = self.name,
            color = self.color,
            description=self.description,
        )

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            name=data_dict["name"],
            color=data_dict["color"],
            description=data_dict["description"]
        )