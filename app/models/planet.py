from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    position_from_sun = db.Column(db.Integer)

    def make_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            position_from_sun=self.position_from_sun
            )



