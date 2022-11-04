def test_get_all_planets_with_no_records(client):
    #Act
    response = client.get("/planets")
    response_body = response.get_json()
    #Assert
    assert response.status_code == 200
    assert response_body == []

"""Create test fixtures and unit tests for the following test cases:

1. `GET` `/planets/1` returns a response body that matches our fixture
1. `GET` `/planets/1` with no data in test database (no fixture) returns a `404`
1. `GET` `/planets` with valid test data (fixtures) returns a `200` with an array including appropriate test data
1. `POST` `/planets` with a JSON request body returns a `201`"""

def test_get_one_planet(client, one_saved_planet):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body["id"] == one_saved_planet.id
    assert response_body["name"] == one_saved_planet.name
    assert response_body["rings"] == one_saved_planet.rings
    assert response_body["description"] == one_saved_planet.description

def test_no_data_returns_404(client):
    response = client.get("/planets/1")

    assert response.status_code == 404

def test_get_all_planets(client, all_planets):
    response = client.get("/planets")
    response_body = response.get_json()
    
    assert response.status_code == 200
    assert len(response_body) == 8