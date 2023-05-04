from app.models.planet import Planet

# WAVE 6 TEST 1
def test_read_one_planet_returns_seeded_planet(client, one_planet):
    # Act 
    response = client.get(f"/planets/{one_planet.id}")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body["name"] == one_planet.name
    assert response_body["description"] == one_planet.description
    assert response_body["color"] == one_planet.color

# WAVE 6 TEST 2
def test_empty_database_returns_404(client):
    # ACT
    response = client.get(f"planets/1")
    response_body = response.get_json()

    # ASSERT
    assert response.status_code == 404
    assert response_body == {"message": f"Planet with id 1 was not found"}


# WAVE 6 TEST 3
def test_valid_data_returns_data_and_200(client, two_planets):
    # ACT
    response = client.get("/planets")
    response_body = response.get_json()

    observed_planet_one = response_body[0]
    observed_planet_two = response_body[1]

    # ASSERT
    assert response.status_code == 200
    assert len(response_body) == 2

    assert observed_planet_one["name"] == "Mars"
    assert observed_planet_one["color"] == "red"
    assert observed_planet_one["description"] == "3rd planet from the Sun"

    assert observed_planet_two["name"] == "Venus"
    assert observed_planet_two["color"] == "orange"
    assert observed_planet_two["description"] == "2nd planet from the Sun"


# WAVE 6 TEST 4
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


def test_read_all_planets_return_empty_list_when_db_is_empty(client):
    # Act
    response = client.get("/planets")
    
    # Assert
    assert response.status_code == 200
    assert response.get_json() == []