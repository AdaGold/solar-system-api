from app import db

class Moon(db.Model): 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"))
    planet = db.relationship("Planet", back_populates = "moons")

    def to_dict(self): 
        return{
            "id" : self.id, 
            "name" : self.name,
            "planet_id" : self.planet.id, 
            "planet" : self.planet.name
        }
        