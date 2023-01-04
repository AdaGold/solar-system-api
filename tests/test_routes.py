from app.routes.planet import validate_planet

NEPTUNE_PLANET = {
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

URANUS_PLANET = {
        "name": "Uranus",
        "description": "Smells bad",
        "mass": 86.8,
        "diameter": 51118,
        "density": 1270,
        "gravity": 8.7,
        "escape_velocity": 21.3,
        "rotation_period": -17.2,
        "day_length": 17.2,
        "distance_from_sun": 2867,
        "orbital_period": 30589,
        "orbital_velocity": 6.8,
        "orbital_inclination": 0.8,
        "orbital_eccentricity": 0.047,
        "obliquity_to_orbit": 97.8,
        "mean_tempurature_c": -195,
        "surface_pressure": None,
        "global_magnetic_feild": True,
        "img": "https://solarsystem.nasa.gov/resources/605/keck-telescope-views-of-uranus/?category=planets_uranus",
        "has_rings": True,
}

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_all_planets_with_two_records(client, two_saved_planets):
    #Act
    response = client.get("/planets")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body[0] == NEPTUNE_PLANET
    assert response_body[1]["name"] == "number two"
    


def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == NEPTUNE_PLANET

def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json=URANUS_PLANET)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "New Planet Uranus created!"

def test_update_one_planet(client, two_saved_planets):
        # Act
    response = client.put("/planets/2", json=URANUS_PLANET)
    #Arrange
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == "Planet 2 successfully updated"

def test_delete_one_planet(client, two_saved_planets):
    #Arrange
    response = client.delete("/planets/2")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == "Planet 2 successfully deleted"

def test_get_one_nonexistent_planet(client, two_saved_planets):
    #Arrange
    response = client.get("/planets/3")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 404
    assert response_body == {"message": "Planet with 3 not found"}

def test_incorrect_id_format(client, two_saved_planets):
    #Arrange
    response = client.get("/planets/a")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 400
    assert response_body == {"message": "a invalid"}

def test_create_incomplete_planet(client):
    #Arrange
    response = client.post("/planets", json={
        "name": "Uranus",
        "mass": 86.8,
        "diameter": 51118,
        "density": 1270,
        "gravity": 8.7,
        "escape_velocity": 21.3,
        "rotation_period": -17.2,
        "day_length": 17.2,
        "distance_from_sun": 2867,
        "orbital_period": 30589,
        "orbital_velocity": 6.8,
        "orbital_inclination": 0.8,
        "orbital_eccentricity": 0.047,
        "obliquity_to_orbit": 97.8,
        "mean_tempurature_c": -195,
        "surface_pressure": None,
        "global_magnetic_feild": True,
        "img": "https://solarsystem.nasa.gov/resources/605/keck-telescope-views-of-uranus/?category=planets_uranus",
        "has_rings": True
    })
    response_body = response.get_json()

    #Assert
    assert response.status_code == 400
    assert response_body == {"message": "Bad request: description attribute is missing"}

def test_update_incomplete_planet(client, two_saved_planets):
    #Arrange
    response = client.put("/planets/2", json={
        "name": "Uranus"})
    response_body = response.get_json()

    #Assert
    assert response.status_code == 400
    assert response_body == {"message": "Bad request: description attribute is missing"}


def test_delete_one_nonexistent_planet(client, two_saved_planets):
    #Arrange
    response = client.get("/planets/3")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 404
    assert response_body == {"message": "Planet with 3 not found"}

#tests for moon here to refactor and increase code coverage. 

def test_all_moon_no_records(client):
    response = client.get("/moons")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []



def test_get_one_moon(client, two_saved_moons):
    response=client.get("/moons/1")
    response_body=response.get_json()

    assert response_body == {
        "id":1,
        "name":"Test Moon", 
        "description":"First Moon for Neptune",
        "image":"pretty_moon.jpg"
    }


def test_get_all_moons_with_two_records(client, two_saved_moons):
    #Act
    response = client.get("/moons")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body[0] == {
        "id":1,
        "name": "Test Moon",
        "description": "First Moon for Neptune",
        "image":"pretty_moon.jpg"
    }
    assert response_body[1]["name"] == "2 Test Moon"
    assert len(response_body) == 2
    


def test_get_one_moon(client, two_saved_moons):
    # Act
    response = client.get("/moons/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        
        "id":1,
        "name": "Test Moon",
        "description": "First Moon for Neptune",
        "image":"pretty_moon.jpg"
    }



def test_create_one_moon(client,two_saved_planets, two_saved_moons):
    # Act
    response = client.post("planets/1/moons", json={
        "name": "three moon",
        "description": "for testing",
        "image": "best_moon.jpb",
})

    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "New Moon three moon created!"

def test_update_one_moon(client, two_saved_moons):
        # Act
    response = client.put("/moons/2", json={
        "name": "moon",
        "description": "Smells bad",
        "image": "images.img"
})
    #Arrange
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == "Moon moon has been updated"

def test_delete_one_moon(client, two_saved_moons):
    #Arrange
    response = client.delete("/moons/2")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == "Moon 2 successfully deleted"



def test_all_moons_by_planet(client, two_saved_planets, two_saved_moons):
    response = client.get("/planets/1/moons")
    response_body = response.get_json()

    # Assert
    assert len(response_body) == 2


def test_validate_planet(two_saved_planets):
    #Act
    result_planet = validate_planet(1)
    
    #Assert
    for key, value in NEPTUNE_PLANET.items():
        assert getattr(result_planet, key) == value


    
