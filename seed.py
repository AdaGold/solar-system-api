from app import create_app, db
from app.models.planet import Planet

my_app = create_app()
with my_app.app_context():
    db.session.add(Planet(name="Mercury", description="The intelligent strategist, known for her analytical skills and love of books.", number_of_moons=0)),
    db.session.add(Planet(name="Venus", description="The charming beauty who believes in love, often the peacemaker among her friends.", number_of_moons=0)),
    db.session.add(Planet(name="Earth", description="The cheerful leader who fights for love and justice, often clumsy but always brave.", number_of_moons=1)),
    db.session.add(Planet(name="Mars", description="The passionate warrior with a strong sense of justice and a fiery spirit.", number_of_moons=2)),
    db.session.add(Planet(name="Jupiter", description="The tough protector with a big heart, skilled in combat and cooking.", number_of_moons=95)),
    db.session.add(Planet(name="Saturn", description="The mysterious guardian with powerful abilities, often associated with destruction and rebirth.", number_of_moons=83)),
    db.session.add(Planet(name="Uranus", description="The confident and adventurous rebel, known for her speed and agility.", number_of_moons=27)),
    db.session.add(Planet(name="Neptune", description="The elegant and artistic fighter, with a deep connection to the ocean and intuition.", number_of_moons=14)),
    db.session.add(Planet(name="Pluto", description="The wise time guardian, responsible for protecting the gates of time and space.", number_of_moons=5)),
    db.session.add(Planet(name="Eris", description="The energetic and playful guardian, spreading warmth and positivity wherever she goes.", number_of_moons=1)),
    db.session.add(Planet(name="Haumea", description="The strategic thinker who uses her intelligence to solve problems and protect her friends.", number_of_moons=2)),
    db.session.add(Planet(name="Makemake", description="The fierce protector with strong instincts, known for her loyalty and bravery.", number_of_moons=1)),
    db.session.add(Planet(name="Ceres", description="The nurturing spirit who brings harmony and balance, always caring for her friends.", number_of_moons=0)),
    db.session.commit()