from app import create_app, db
from app.models.planet import Planet


my_app = create_app()
with my_app.app_context():
    db.session.add(Planet(name="Earth", description=" third planet from the sun", size = "medium", moons=1, has_flag=True))
    db.session.add(Planet(name="Jupiter", description="the largest planet", size = "large", moons=4, has_flag=False))
    db.session.add(Planet(name="Mars", description="Red and hot", size = "medium", moons= 2, has_flag=False))
    db.session.add(Planet(name="Mercury", description="closet to the sun", size = "small", moons=0, has_flag=True))
    db.session.add(Planet(name="Venus", description="Hottest planet", size = "small", moons=0, has_flag=False))
    db.session.commit()


# | Planet     | Description                      | Size   | Moons | Has Flag? |
# |------------|----------------------------------|--------|-------|-----------|
# | Mercury    | Closest to the Sun, very hot     | Small  | 0     | No        |
# | Venus      | Thick atmosphere, hottest planet | Small  | 0     | No        |
# | Earth      | Home to life, oceans and land    | Medium | 1     | Yes       |
# | Mars       | Known as the Red Planet          | Small  | 2     | Yes       |
# | Jupiter    | Largest planet, gas giant        | Large  | 79    | No        |
# | Saturn     | Known for its rings              | Large  | 83    | No        |
# | Uranus     | Icy gas giant, tilted axis       | Large  | 27    | No        |
