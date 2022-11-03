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
        "name": "Planet number one",
        "description": "watr 4evr",
        "color": "color"
    }
# I have added this create function
def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "MelMash Planet",
        "description": "The Best!",
        "color": "Green"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Book New Book successfully created"
    
