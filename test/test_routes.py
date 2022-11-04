def test_get_all_planets(client):
    #Act
    response = client.get("/planets")
    response_body = response.get_json()
    #Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_one_planet(client,one_saved_planet):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == ["id"] == one_saved_planet.id
    assert response_body == ["name"] == one_saved_planet.name
    assert response_body == ["rings"] == one_saved_planet.rings
    assert response_body == ["description"] == one_saved_planet.rings
