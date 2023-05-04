from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    color = db.Column(db.String)

    # WAVE 5 _______
    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            name = data_dict["name"],
            description = data_dict["description"],
            color = data_dict["color"]
        )
    #___________________

    
    def make_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            color=self.color,
        )