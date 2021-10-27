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
        "name": "Mars",
        "description": "red_planet ",
        "distance_from_sun_in_million_mi": 1000,
        "moon_count": 1
    }

def test_post_one_planet(client, two_saved_planets):
    # Act
    response = client.post("/planets", json = {

        "name": "Mars",
        "description": "red_planet ",
        "distance_from_sun_in_million_mi": 1000,
        "moon_count": 1
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 3,
        "name": "Mars",
        "description": "red_planet ",
        "distance_from_sun_in_million_mi": 1000,
        "moon_count": 1
    }