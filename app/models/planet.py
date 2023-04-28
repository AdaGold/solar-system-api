from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    color = db.Column(db.String)
    # __tablename__ = "planets"

    def planet_to_dict(self):
        return {
        "id": self.id,
        "name": self.name,
        "description": self.description,
        "color": self.color }
        

    def to_string(self):
        return f"{self.id}: {self.name} Description {self.description} "
    
    