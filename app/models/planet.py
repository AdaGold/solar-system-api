#from .moon import Moon, moons_list
from app import db
class Planet(db.Model):
    __tablename__='planets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String)
    description=db.Column(db.String)
    mass=db.Column(db.Float)
    diameter=db.Column(db.Float)
    density=db.Column(db.Float)
    gravity=db.Column(db.Float)
    escape_velocity=db.Column(db.Float)
    rotation_period=db.Column(db.Float)
    day_length=db.Column(db.Float)
    distance_from_sun=db.Column(db.Float)
    orbital_period=db.Column(db.Float)
    orbital_velocity=db.Column(db.Float)
    orbital_inclination=db.Column(db.Float)
    orbital_eccentricity=db.Column(db.Float)
    obliquity_to_orbit=db.Column(db.Float)
    mean_tempurature_c=db.Column(db.Float)
    surface_pressure=db.Column(db.Float)
    global_magnetic_feild=db.Column(db.Boolean)
    img=db.Column(db.String)
    has_rings=db.Column(db.Boolean)
    moons = db.relationship("Moon", back_populates="planet")
#     def __init__(self, id, name, description, mass, diameter, density, gravity, escape_velocity,
#     rotation_period, day_length, distance_from_sun, orbital_period, orbital_velocity, orbital_inclination, orbital_eccentricity,
#     obliquity_to_orbit, mean_tempurature_c, surface_pressure, global_magnetic_feild,img,has_rings=False, moons=None):
#         self.id=id
#         self.name=name
#         self.description=description
#         self.mass=mass
#         self.diameter=diameter
#         self.density=density
#         self.gravity=gravity
#         self.escape_velocity=escape_velocity
#         self.rotation_period=rotation_period
#         self.day_length=day_length
#         self.distance_from_sun=distance_from_sun
#         self.orbital_period=orbital_period
#         self.orbital_velocity=orbital_velocity
#         self.orbital_inclination=orbital_inclination
#         self.orbital_eccentricity=orbital_eccentricity
#         self.obliquity_to_orbit=obliquity_to_orbit
#         self.mean_tempurature_c=mean_tempurature_c
#         self.surface_pressure=surface_pressure
#         self.global_magnetic_feild=global_magnetic_feild
#         self.img=img
#         self.has_rings=has_rings
#         self.moons = moons if moons else []
    
#     def add_moon(self, moon):
#         # validate if is a moon object
#         if moon.__class__.__name__ != "Moon":
#             raise ValueError(f"{moon} is not a moon.")
#         # validate if the planet_id of the moon is the same as self.id
#         if moon.planet_id != self.id:
#             raise ValueError(f"{moon} is not the moon of {self.name}")
#         self.moons.append(moon)

#     def serialize(self):
#         filtered_attributes = self.__dict__.copy()
#         new_value = []
#         for moon_object in filtered_attributes["moons"]:
#             new_value.append(moon_object.name)
#         filtered_attributes["moons"] = new_value
#         return filtered_attributes

# solar_system=[]{
            # "name": "Mercury", 
            # "description": First Planet near the Sun",
            # "mass": 0.330,
            # "diameter":4878,
            # "density": 5429,
            # "gravity": 3.7,
            # "escape_velocity": 4.3,
            # "rotation_period": 1407.6,
            # "day_length": 57.9,
            # "distance_from_sun":36.04,
            # "orbital_period": 88.0,
            # "orbital_velocity" : 47.4,
            # "orbital_inclination": 7.0,
            # "orbital_eccentricity":0.206,
            # "obliquity_to_orbit":0.034,
            # "mean_tempurature_c":167,
            # "surface_pressure":0,
            # "global_magnetic_feild":False,
            # "img":https://photojournal.jpl.nasa.gov/jpegMod/PIA16853_modest.jpg,
            # "has_Rings": False}
# mercurey =
# Planet(1, "Mercury", "First Planet near the Sun", .330, 4878, 5429, 3.7, 4.3, 1407.6, 4222.6,
# 57.9, 88.0, 47.4, 7.0, .206, .034, 167, 0, False, 'https://photojournal.jpl.nasa.gov/jpegMod/PIA16853_modest.jpg')
# solar_system.append(mercurey){
            # "name": "Mercury", 
            # "description": First Planet near the Sun",
            # "mass": 0.330,
            # "diameter":4878,
            # "density": 5429,
            # "gravity": 3.7,
            # "escape_velocity": 4.3,
            # "rotation_period": 1407.6,
            # "day_length": 57.9,
            # "distance_from_sun":36.04,
            # "orbital_period": 88.0,
            # "orbital_velocity" : 47.4,
            # "orbital_inclination": 7.0,
            # "orbital_eccentricity":0.206,
            # "obliquity_to_orbit":0.034,
            # "mean_tempurature_c":167,
            # "surface_pressure":0,
            # "global_magnetic_feild":False,
            # "img":https://photojournal.jpl.nasa.gov/jpegMod/PIA16853_modest.jpg,
            # "has_Rings": False}
# venus = Planet(2, "Venus", "Second Planet from the sun", 4.87, 12104, 5243, 8.9, 10.4, -5832.5, 2802.0, 108.2, 224.7, 35.0, 3.4, .0007, 177.4, 464, 92, False, 'https://solarsystem.nasa.gov/resources/2524/newly-processed-views-of-venus-from-mariner-10/?category=planets_venus')
# solar_system.append(venus)
# earth = Planet(3, "Earth", "Has Humans", 5.97, 12756, 5514, 9.8, 11.2, 23.9, 24.0, 149.6, 365.2, 29.8, 0.0, .017, 23.4, 15, 1, True, 'https://solarsystem.nasa.gov/resources/786/blue-marble-2002/?category=planets_earth', False, [moons_list[0]])
# solar_system.append(earth)
# mars= Planet(4, "Mars", "Being explored by robots, considered for space colony", .642, 6792, 3934, 3.7, 5, 24.6, 24.7, 228, 687, 24.1, 1.8, .094, 25.2, -65, .01, False, 'https://solarsystem.nasa.gov/resources/948/hubbles-close-up-view-of-mars-dust-storm/?category=planets_mars')
# solar_system.append(mars)
# jupiter = Planet(5, "Jupiter", "Largest Gas Giant", 1898, 142984, 1326, 23.1, 59.5, 9.9, 9.9, 778.5, 4331,13.1, 1.3, .049, 3.1, -110, None, True, 'https://solarsystem.nasa.gov/resources/2486/hubbles-new-portrait-of-jupiter/?category=planets_jupiter', has_rings=True)
# solar_system.append(jupiter)
# saturn = Planet(6, "Saturn", "Gas Giant", 568, 120536, 687, 9, 35.5, 10.7, 10.7, 1432.0, 10747, 9.7, 2.5, .052, 26.7, -140, None, True, 'https://solarsystem.nasa.gov/resources/2490/saturns-rings-shine-in-hubble-portrait/?category=planets_saturn', has_rings=True)
# solar_system.append(saturn)
# uranus = Planet(7, "Uranus", "Smells bad",86.8, 51118, 1270, 8.7, 21.3, -17.2, 17.2, 2867, 30589, 6.8, .8, .047, 97.8, -195, None, True, 'https://solarsystem.nasa.gov/resources/605/keck-telescope-views-of-uranus/?category=planets_uranus', has_rings=True)
# neptune = Planet(8, "Neptue", "Named for the god of the sea because it is blue", 102, 49528, 1638, 11.0, 23.5, 16.1, 16.1, 4515, 59800, 5.4, 1.8, .010, 28.3, -200, None, True, 'https://solarsystem.nasa.gov/resources/611/neptune-full-disk-view/?category=planets_neptune', has_rings=True)