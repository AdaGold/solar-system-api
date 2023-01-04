from app.models.planet import Planet

def test_to_dict_no_missing_data():
    #Arrange
    test_planet = Planet(
        id = 1,
        name="Neptune",
        description="Named for the god of the sea because it is blue",
        mass=102,
        diameter=49528,
        density=1638,
        gravity=11.0,
        escape_velocity=23.5,
        rotation_period=16.1,
        day_length=16.1,
        distance_from_sun=4515,
        orbital_period=59800,
        orbital_velocity=5.4,
        orbital_inclination=1.8,
        orbital_eccentricity=0.01,
        obliquity_to_orbit=28.3,
        mean_tempurature_c=-200,
        surface_pressure=None,
        global_magnetic_feild=True,
        img="https://solarsystem.nasa.gov/resources/611/neptune-full-disk-view/?category=planets_neptune",
        has_rings=True,
    )
    #Act
    result = test_planet.to_dict()

    #assert
    assert result == {
        "id":1,
        "name": "Neptune",
        "description": "Named for the god of the sea because it is blue",
        "mass": 102,
        "diameter": 49528,
        "density": 1638,
        "gravity": 11.0,
        "escape_velocity": 23.5,
        "rotation_period": 16.1,
        "day_length": 16.1,
        "distance_from_sun": 4515,
        "orbital_period": 59800,
        "orbital_velocity": 5.4,
        "orbital_inclination": 1.8,
        "orbital_eccentricity": 0.01,
        "obliquity_to_orbit": 28.3,
        "mean_tempurature_c": -200,
        "surface_pressure": None,
        "global_magnetic_feild": True,
        "img": "https://solarsystem.nasa.gov/resources/611/neptune-full-disk-view/?category=planets_neptune",
        "has_rings": True,
        "moons": []
    }

def test_to_dict_missing_attributes():
    #Arrange
    complete_attributes = {
        "id":1,
        "name": "Neptune",
        "description": "Named for the god of the sea because it is blue",
        "mass": 102,
        "diameter": 49528,
        "density": 1638,
        "gravity": 11.0,
        "escape_velocity": 23.5,
        "rotation_period": 16.1,
        "day_length": 16.1,
        "distance_from_sun": 4515,
        "orbital_period": 59800,
        "orbital_velocity": 5.4,
        "orbital_inclination": 1.8,
        "orbital_eccentricity": 0.01,
        "obliquity_to_orbit": 28.3,
        "mean_tempurature_c": -200,
        "surface_pressure": None,
        "global_magnetic_feild": True,
        "img": "https://solarsystem.nasa.gov/resources/611/neptune-full-disk-view/?category=planets_neptune",
        "has_rings": True,
        "moons": []
    }

    for attribute in complete_attributes.keys():
        incomplete_attributes = complete_attributes.copy()
        del incomplete_attributes[attribute]
        test_planet = Planet(**incomplete_attributes)
        
        expected = complete_attributes.copy()
        if attribute == "moons":
            expected[attribute] = []
        else:
            expected[attribute] = None
    
        #Act
        result = test_planet.to_dict()

        #Assert
        assert result == expected
    