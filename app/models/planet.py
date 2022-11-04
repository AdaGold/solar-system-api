from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    color = db.Column(db.String)


    def to_dict(self):

        return {
            "name": self.name,
            "color": self.color,
            "description": self.description,
            "id": self.id
        }
    @classmethod   
    def from_json(cls, req_body):
        return cls(
            name= req_body["name"],
            color= req_body["color"],
            description= req_body["description"]
        )
        
    def update(self, req_body):
        self.name= req_body["name"],
        self.color= req_body["color"],
        self.description= req_body["description"]