from app import create_app, db
from app.models.planet import Planet


my_app = create_app()
with my_app.app_context():
    db.session.add(Planet(name="43-HT3", description=" found in neighboring solar system", size = "medium", moons=12, has_flag=False))
    db.session.add(Planet(name="X65", description="Bigger than Jupiter", size = "large", moons=9, has_flag=False))
    db.session.add(Planet(name="33-UV2", description="purple with 3 rings", size = "medium", moons= 0, has_flag=False))
    db.session.add(Planet(name="9ND-87", description="black, almost invisible", size = "small", moons=42, has_flag=False))
    
    db.session.add(Planet(name="Venus", description="Hottest planet", size = "small", moons=0, has_flag=False))
    db.session.add(Planet(name="Mercury", description="Closest to the Sun, very hot", size="Small", moons=0, has_flag=False))
    db.session.add(Planet(name="Venus", description="Thick atmosphere, hottest planet", size="Small", moons=0, has_flag=False))
    db.session.add(Planet(name="Earth", description="Home to life, oceans and land", size="Medium", moons=1, has_flag=True))
    db.session.add(Planet(name="Mars",    description="Known as the Red Planet", size="Small", moons=2, has_flag=True))
    db.session.add(Planet(name="Jupiter", description="Largest planet, gas giant", size="Large", moons=79, has_flag=False))
    db.session.add(Planet(name="Saturn",  description="Known for its rings", size="Large", moons=83, has_flag=False))
    db.session.add(Planet(name="Uranus",  description="Icy gas giant, tilted axis", size="Large", moons=27, has_flag=False))
    db.session.commit()



