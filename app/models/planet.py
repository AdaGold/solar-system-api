from app import db

class Planet(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.Text)
    is_rocky = db.Column(db.Boolean)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "is_rocky" : self.is_rocky
        }
