from app.models.planet import Planet

def test_get_all_planets_with_no_records(client):
    #Act
    response = client.get("/planets")
    response_body = response.get_json()
    #Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_returns_planet(client, one_saved_planet):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body["id"] == one_saved_planet.id
    assert response_body["name"] == one_saved_planet.name
    assert response_body["rings"] == one_saved_planet.rings
    assert response_body["description"] == one_saved_planet.description

def test_get_one_planet_with_no_records(client):
    response = client.get("/planets/1")

    assert response.status_code == 404

def test_get_all_planets_returns_all_planets(client, all_planets):
    response = client.get("/planets")
    response_body = response.get_json()
    
    assert response.status_code == 200
    assert len(response_body) == 8

def test_create_planet_path(client):
    EXPECTED_PLANET = {
        "name": "Pluto",
        "description": "Not a planet :(",
        "rings": False
    }

    response = client.post("/planets", json=EXPECTED_PLANET)
    response_body = response.get_data(as_text=True)
    planet = Planet.query.get(1)

    assert response.status_code == 201
    assert response_body == f"Planet {EXPECTED_PLANET['name']} successfully created"
    assert planet.name == EXPECTED_PLANET["name"]
    assert planet.description == EXPECTED_PLANET["description"]
    assert planet.rings == EXPECTED_PLANET["rings"]
