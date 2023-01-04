def test_get_all_planets_with_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []


def test_get_one_planet(client, two_saved_planets):
    response = client.get("/planets/2")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "name": "Saturn",
        "description": "Saturn is the sixth planet from the Sun and the second-largest in the Solar System, after Jupiter. It is a gas giant with an average radius of about nine and a half times that of Earth.",
        "size": 2,
        "distance_from_earth": 982,
        "id": 2
    }