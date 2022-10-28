from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    color = db.Column(db.String)


    # class Planet():
    # def __init__(self, id, name, description, color):
    #     self.id = id
    #     self.name = name
    #     self.description = description
    #     self.color = color
