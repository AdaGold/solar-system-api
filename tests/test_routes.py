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
        "name": "Earth",
        "description": "Inhabits life",
        "size": "7,917.5 mi"
    }

def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "New Planet",
        "description": "The Best!",
        "size": "10000 happy mi"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet New Planet successfully created"