from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    distance = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return ({"id": self.id,
                "name": self.name,
                "description": self.description,
                "distance": self.distance})
    
    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            name = data_dict["name"],
            description = data_dict["description"],
            distance = data_dict["distance"]
        )