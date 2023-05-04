from app import db

class Planet(db.Model):

    id = db.Column(
        db.Integer, 
        primary_key=True, 
        autoincrement=True)
    
    name = db.Column(
        db.String,
        nullable = False)
    
    description = db.Column(
        db.String,
        nullable = False) 
    
    def to_dict(self):
        return dict(
            id = self.id,
            name = self.name,
            description = self.description
        )
    
    @classmethod
    def from_dict(cls, planet_data):
        return cls(
            name = planet_data["name"],
            description = planet_data["desription"]
        )
    
 
# planets = [
#     Planet(1, "Mercury", "The Morning star"),
#     Planet(2, "Venus", "The Evening star"),
#     Planet(3, "Mars", "The Red planet"),
#     Planet(4, "Earth", "The Blue Planet"),
#     Planet(5, "Jupiter", "The Giant Planet"),
#     Planet(6, "Saturn", "The Ringed Planet"),
#     Planet(7, "Uranus", "The Ice Giant"),
#     Planet(8, "Neptune", "Big Blue"),
#     Planet(9, "Pluto", "The Minor Planet")
#     ]
