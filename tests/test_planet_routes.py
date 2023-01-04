from app.models.planet import Planet

PLANET_NAME = "Mercury"
PLANET_DESCRIPTION = "Mercury is the smallest planet of our solar system."
PLANET_IS_ROCKY = True

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

def test_get_one_planet_invalid_id(client):
    response = client.get("/planets/hello")
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {"message":"Planet id hello is Invalid" }

    
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
        "name":PLANET_NAME,
        "description":PLANET_DESCRIPTION,
        "is_rocky": PLANET_IS_ROCKY
    }
    response = client.post("/planets", json=test_data)
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Planet Mercury successfully created"

    new_planet = Planet.query.get(1)

    assert new_planet
    assert new_planet.name == PLANET_NAME
    assert new_planet.description == PLANET_DESCRIPTION
    assert new_planet.is_rocky == PLANET_IS_ROCKY

def test_create_planet_invalid_json(client):
    response = client.post("/planets", json=None)
    response_body = response.get_json()

    assert response.status_code == 400
    assert "details" in response_body
    assert "An empty or invalid json object was sent." in response_body["details"]
    assert Planet.query.all() == []

def test_create_planet_no_name_in_body(client):
    test_data = {
        "description":PLANET_DESCRIPTION,
        "is_rocky": PLANET_IS_ROCKY
    }
    response = client.post("/planets", json=test_data)
    response_body = response.get_json()

    assert response.status_code == 400
    assert "details" in response_body
    assert "Request body must include name." in response_body["details"]
    assert Planet.query.all() == []

def test_create_planet_no_description_in_body(client):
    test_data = {
        "name":PLANET_NAME,
        "is_rocky": PLANET_IS_ROCKY
    }

    response = client.post("/planets", json=test_data)
    response_body = response.get_json()

    assert response.status_code == 400
    assert "details" in response_body
    assert "Request body must include description." in response_body["details"]
    assert Planet.query.all() == []

def test_create_planet_no_is_rocky_in_body(client):
    test_data = {
        "name":PLANET_NAME,
        "description":PLANET_DESCRIPTION
    }

    response = client.post("/planets", json=test_data)
    response_body = response.get_json()

    assert response.status_code == 400
    assert "details" in response_body
    assert "Request body must include is_rocky." in response_body["details"]
    assert Planet.query.all() == []

def test_update_planet_valid_input(client,one_saved_planet):
    test_data = {
        "name":PLANET_NAME,
        "description":PLANET_DESCRIPTION,
        "is_rocky": PLANET_IS_ROCKY
    }
    response = client.put("/planets/1", json=test_data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == f"Planet {PLANET_NAME} successfully updated"

def test_delete_planet_valid_id(client,one_saved_planet):
    response = client.delete("planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == "Planet Mercury successfully deleted"