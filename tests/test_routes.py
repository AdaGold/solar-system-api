from app.models.planet import Planet

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

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


def test_create_planet_can_create_planet_in_empty_db(client):
    #arrange
    EXPECTED_PLANET = {
        "name": "Created Planet",
        "description": "New watr 4evr",
        "color": "New color"
    }

    EXPECTED_ID = 1

    #act
    response = client.post("/planets", json = EXPECTED_PLANET)
    response_body = response.get_data(as_text=True)

    #actual_planet = Planet.query.get(EXPECTED_ID)

    assert response.status_code == 201
    assert response_body == f"planet {EXPECTED_PLANET['name']} successfully created"


# def test_create_one_planet(client):
#     # Act
#     response = client.post("/planets", json={
#         "name": "MelMash Planet",
#         "description": "The Best!",
#         "color": "Green"
#     })
#     response_body = response.get_json() 

#     # Assert
#     assert response.status_code == 201
#     assert response_body == "planet MelMash Planet successfully created"
    
