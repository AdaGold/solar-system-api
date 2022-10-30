from app import db

# db.Model is defined in our app __init__.py  
#  __tablename__  = "any_table_name" property to change the name of the table in postgres

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    moons = db.Column(db.Integer)
