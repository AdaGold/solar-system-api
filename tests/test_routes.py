from app.models.planet import Planet

def test_read_all_planets_return_empty_list_when_db_is_empty(client):
    # Act
    response = client.get("/planets")
    
    # Assert
    assert response.status_code == 200
    assert response.get_json() == []

def test_read_one_planet_returns_seeded_planet(client, one_planet):
    # Act 
    response = client.get(f"/planets/{one_planet.id}")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body["name"] == one_planet.name
    assert response_body["description"] == one_planet.description
    assert response_body["color"] == one_planet.color

def test_create_planet_returns_201(client):
    EXPECTED_PLANET = dict(
        name = "Neptune",
        description = "8th planet from the Sun",
        color = "Aqua"
        )
    
    # Act
    response = client.post("/planets", json=EXPECTED_PLANET)
    response_body = response.get_data(as_text=True)

    actual_planet = Planet.query.get(1)


    # Assert
    assert response.status_code == 201
    assert response_body == f"Planet {EXPECTED_PLANET['name']} successfully created"
    assert EXPECTED_PLANET['name'] == actual_planet.name
    assert EXPECTED_PLANET['description'] == actual_planet.description
    assert EXPECTED_PLANET['color'] == actual_planet.color