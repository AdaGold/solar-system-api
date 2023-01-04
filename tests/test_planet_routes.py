def test_get_all_planets_with_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

#1 `GET` `/planets/1` returns a response body that matches our fixture
def test_get_one_planet(client, two_saved_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id":1,
        "name":"Mercury",
        "description":"Mercury is the smallest planet of our solar system.",
        "is_rocky":True
    }

#2 `GET` `/planets/1` with no data in test database (no fixture) returns a `404`
def test_get_one_planet_with_no_records(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message":"Planet id 1 is Not Found" }
    
#3 `GET` `/planets` with valid test data (fixtures) returns a `200` with an array including appropriate test data
def test_get_all_planets(client, two_saved_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [{
        "id":1,
        "name":"Mercury",
        "description":"Mercury is the smallest planet of our solar system.",
        "is_rocky":True
    },
    {
        "id": 2,
        "name": "Venus",
        "description": "Venus is the hottest planet in the solar system.",
        "is_rocky": True
    }]
