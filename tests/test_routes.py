def test_read_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_read_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id":1,
        "name":"ceres",
        "description":"rocky",
        "num_moons": 0
        }

def test_create_planet(client):
    #Act
    response = client.post("/planets", json={
        "name": "New Planet",
        "description": "Cool new planet!",
        "num_moons": 5
    })
    response_body = response.get_data(as_text=True)

    assert response.status_code == 201
    assert response_body == "Planet New Planet successfully created"
    
def test_read_all_planets_with_two_records(client, two_saved_planets):
    #ACT
    response = client.get("/planets")
    response_body = response.get_json()

    #ASSERT
    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0] == {
        "id": 1,
        "name": "ceres",
        "description": "rocky",
        "num_moons": 0
    }
    assert response_body[1] == {
        "id": 2,
        "name": "eris",
        "description": "rocky",
        "num_moons": 1
    }

def test_read_all_planets_with_name_query_matching_none(client, two_saved_planets):
    #ACT
    data = {'name': 'nonexisting planet'}
    response = client.get("/planets", query_string = data)
    response_body = response.get_json()

    #ASSERT
    assert response.status_code == 200
    assert response_body == []

def test_read_all_planets_with_name_query_matching_one(client, two_saved_planets):
    #ACT
    data = {'name': 'ceres'}
    response = client.get("/planets", query_string = data)
    response_body = response.get_json()

    #ASSERT
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body[0] == {
        "id": 1,
        "name": "ceres",
        "description": "rocky",
        "num_moons": 0
    }

def test_read_one_planet_id_not_found(client, two_saved_planets):
    # Act
    response = client.get("/planets/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message":"Planet 3 is not found. Find a planet in our solar system!"}

def test_read_one_planet_id_invalid(client, two_saved_planets):
    # Act
    response = client.get("/planets/dagon")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message":"Planet dagon is invalid. Find a planet in our solar system!"}
