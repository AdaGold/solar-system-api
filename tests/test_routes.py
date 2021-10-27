# file holds the tests for the code in app/routes.py file
from app.models.planet import Planet

def test_get_one_planet_no_data(client):
    # Act
    response = client.get("/planets/1")

    # Assert
    assert response.status_code == 404

def test_get_all_planets_with_no_data(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_one_planet(client, one_saved_planet):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Red Planet",
        "description": "The best planet in the universe!",
        "color": "Red"
    }

def test_get_all_planets(client, all_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()
    planet_1 = {
        "id": 1,
        "name": "Red Planet",
        "description": "The best planet in the universe!",
        "color": "Red"
    }
    planet_2 = {
        "id": 2,
        "name": "Ada Planet",
        "description": "An invisible rock in our solar system",
        "color": "Let your imagination run wild with this one."
    }

    # Assert
    assert response.status_code == 200
    assert isinstance(response_body, list)
    assert planet_1 in response_body
    assert planet_2 in response_body

    
def test_create_one_planet(client):
    response = client.post("/planets", json = ({"name": "Unique Space Rock", "description": "Super somber place in the universe.", "color": "The greyest Grey"}))
    response_body = response.get_json()
    assert response.status_code == 201 
    assert response_body == f"Planet Unique Space Rock successfully created"