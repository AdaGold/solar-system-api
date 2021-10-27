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
        "description": "home",
        "number_of_moons": 0
        }

def test_no_planet_in_test_database(client):
    # Act
    response = client.get("planets/2")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404

def test_get_all_planets_with_data(client, two_saved_planets):
    # Act
    response = client.get('/planets')
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "Earth",
        "description": "home",
        "number_of_moons": 0
        },
        {
        "id": 2,
        "name": "Mars",
        "description": "red",
        "number_of_moons": 0
        }]

def test_post_one_planet(client):
    # Act
    response = client.post('/planets', json = {
        "name": "Jupiter",
        "description": "huge",
        "number_of_moons": 0
    })
    response_body = response.get_json()
 
    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "Jupiter",
        "description": "huge",
        "number_of_moons": 0
    }