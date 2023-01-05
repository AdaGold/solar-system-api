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

def test_create_planet_valid_input(client):
    test_data = {
        "name":"Mercury",
        "description":"Mercury is the smallest planet of our solar system.",
        "is_rocky": True
    }
    response = client.post("/planets", json=test_data)
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Planet Mercury successfully created"

def test_update_planet_valid_input(client,one_saved_planet):
    test_data = {
        "name":"Mercury",
        "description":"Mercury is the smallest planet of our solar system.",
        "is_rocky": True
    }
    response = client.put("/planets/1", json=test_data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == "Planet Mercury successfully updated"

def test_delete_planet_valid_id(client,one_saved_planet):
    response = client.delete("planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == "Planet Mercury successfully deleted"

# `GET` `/planets/a` returns a `400`
def test_get_a_planet_with_invalid_id_type(client, two_saved_planets):
    response = client.get("/planets/a")
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {'message': 'Planet id a is Invalid'}

# `PUT` `/planets/1` with extra attributes in valid json data returns a `500`
def test_put_a_planet_with_extra_attributes(client, one_saved_planet):
    test_data = {
            "gravity": 3.7,
            "name":"Mercury",
            "description":"Mercury is the smallest planet of our solar system.",
            "is_rocky": True
        }
    response = client.put("/planets/1", json=test_data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == "Planet Mercury successfully updated"

#'GET' '/planets?planet_name=Ven' returns a '200' with an array including appropriate test data
def test_get_a_planets_with_a_query_parameter(client, two_saved_planets):
    response = client.get("/planets?planet_name=Ven")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [
    {
        "id": 2,
        "name": "Venus",
        "description": "Venus is the hottest planet in the solar system.",
        "is_rocky": True
    }]