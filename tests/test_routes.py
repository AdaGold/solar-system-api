from app.models.planet import Planet

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_all_planets_with_fixture_records(client, many_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 4
    #assert


def test_get_one_planet_no_fixture(client):
    # Act
    response = client.get("/books/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body is None

def test_get_one_planet(client, one_planet):
    # Act
    response = client.get(f"/planets/{one_planet.id}")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Planet number one",
        "description": "watr 4evr",
        "color": "color"
    }

def test_get_one_planet_from_many_planets_valid_id(client, many_planets):
    #Arrange
    EXPECTED_ID = 3
    
    # Act
    response = client.get(f"/planets/{EXPECTED_ID}")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 3,
        "name": "Planet of butterflies",
        "description": "Butterflies and unicorns live there",
        "color": "Rainbow"
    }

def test_get_one_planet_from_many_planets_non_existing_id_returns_404(client, many_planets):
    #Arrange
    NON_EXISTING_ID = 7
    
    # Act
    response = client.get(f"/planets/{NON_EXISTING_ID}")
    response_body = response.get_data(as_text=True)

    # Assert
    assert response.status_code == 404
    assert response_body == "{\"message\":\"planet 7 not found\"}\n"

def test_get_one_planet_from_many_planets_invalid_id_returns_400(client, many_planets):
    #Arrange
    INVALID_ID = "ABC"
    
    # Act
    response = client.get(f"/planets/{INVALID_ID}")
    response_body = response.get_data(as_text=True)

    # Assert
    assert response.status_code == 400
    assert response_body == "{\"message\":\"planet ABC has an invalid planet_id\"}\n"

def test_create_planet_can_create_planet_in_empty_db(client):
    #arrange
    EXPECTED_PLANET = {
        "name": "Created Planet",
        "description": "New watr 4evr",
        "color": "New color"
    }

    #act
    response = client.post("/planets", json = EXPECTED_PLANET)
    response_body = response.get_data(as_text=True)

    assert response.status_code == 201
    assert response_body == f"planet {EXPECTED_PLANET['name']} successfully created"


def test_create_one_planet_if_there_are_planets_in_db(client, many_planets):
    #arrange
    EXPECTED_PLANET = {
        "name": "Created Planet",
        "description": "New watr 4evr",
        "color": "New color"
    }

    #act
    response = client.post("/planets", json = EXPECTED_PLANET)
    response_body = response.get_data(as_text=True)
    
    
    all_planets = Planet.query.all()
    planets_response = []

    for planet in all_planets:
        planets_response.append(planet.to_dict())

    # Assert
    assert response.status_code == 201
    assert response_body == "planet Created Planet successfully created"
    assert len(all_planets) == 5
    assert EXPECTED_PLANET["name"] == planets_response[4]["name"]