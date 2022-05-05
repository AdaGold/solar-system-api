

def test_get_all_planets_with_no_records(client):
    # act
    response = client.get("/planets")
    response_body = response.get_json()

    # assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client, two_saved_planets):
    # act
    response = client.get("planets/1")
    response_body = response.get_json()

    # assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Neptune",
        "description": "ice",
        "distance_from_sun": 9
    }