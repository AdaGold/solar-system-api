from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    distance_from_sun = db.Column(db.Integer, nullable=False)

    def to_dictionary(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            distance_from_sun=self.distance_from_sun
        )