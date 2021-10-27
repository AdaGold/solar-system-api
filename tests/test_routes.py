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
        "name": "First Planet",
        "description": "it's first",
        "moons": 7
    }

def test_get_one_planet_when_empty(client):
    # Act
    response = client.get("/planets/1")

    # Assert
    assert response.status_code == 404

def test_all_records_with_data(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "First Planet",
        "description": "it's first",
        "moons": 7
    },
    {
        "id": 2,
        "name": "Second Planet",
        "description": "it's second",
        "moons": 11
    }]

def test_post_returns_201(client):
    # Act
    planet = {
        "name": "Third Planet", 
        "description": "it's third", 
        "moons": 3}
    response = client.post("/planets", 
        json = planet)
    
    #Assert
    assert response.status_code == 201 

    response = client.get("/planets")
    response_body = response.get_json()
    planet["id"] = 1
    assert planet in response_body