
def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get('/planets/1')
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mercury",
        "description": "Mercury description",
        "moons": 1
    }

def test_create_one_planet(client):
    # Act
    response = client.post('/planets', json={
        "name": "New Planet",
        "description": "The Best planet!",
        "moons": 1
    })
    response_body = response.get_json() # the response in my app/routes.py when creating a book has to return a jsonify version otherwise it will return None

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet New Planet successfully created"
