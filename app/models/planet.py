from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    moons = db.Column(db.Integer)

    def to_json(self):
        return {
            "id": self.id,
            "name" : self.name,
            "decription": self.description,
            "moons": self.moons
        }


# class Planet():
#     def __init__(self, id, name, description, moons = None):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.moons = moons

#     def to_json(self):
#         return {
#             "id": self.id,
#             "name" : self.name,
#             "decription": self.description,
#             "moons": self.moons
#         }
