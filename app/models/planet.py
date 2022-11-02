from app import db



class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    size = db.Column(db.String)

    #def dict_planet(self):
        #return{
            #"id": self.id,
            #"name": self.name,
            #"description": self.description,
            #"size": self.size
            #}