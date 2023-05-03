from app.models.planet import Planet

def test_get_all_cats_returns_empty_list_when_db_is_empty(client):
    #act
    response = client.get("/planets")

    #assert 
    assert response.status_code == 200
    assert response.get_json() == []

def test_get_one_planet_returns_seeded_planet(client, one_planet):
    response = client.get(f"/planets/{one_planet.id}")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body["id"] == one_planet.id
    assert response_body["name"] == one_planet.name
    assert response_body["description"] == one_planet.description

def test_create_planet_happy_path(client):
    #arrange, a lil bit
    EXPECTED_PLANET = {
        "name":"magicland",
        "description":"I want to live here"
    }

    response = client.post("/planets", json=EXPECTED_PLANET)
    response_body = response.get_data(as_text=True)

    actual_planet = Planet.query.get(1)
    assert response.status_code == 201
    assert response_body == f"Planet {EXPECTED_PLANET['name']} successfully created."
    assert actual_planet.name == EXPECTED_PLANET["name"]