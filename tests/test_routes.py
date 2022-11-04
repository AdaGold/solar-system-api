import pytest
from app.models.planet import Planet

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Venus",
        "description": "a fun planet to be on",
        "diameter":"2,374 km",
    }

def test_get_one_planet_with_no_records(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == { "message": "Planet 1 not found"}

def test_get_all_planets(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [
        {
        "id": 1,
        "name": "Venus",
        "description": "a fun planet to be on",
        "diameter":"2,374 km"
        },
        {
        "id": 2,
        "name": "Mars",
        "description": "home of the martians",
        "diameter":"3,456 km"
        }
        ]
    
def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Saturn",
        "description": "rings of gold shine bright",
        "diameter": "5,467 km"
    })
    response_body = response.get_json()


    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Saturn successfully created"