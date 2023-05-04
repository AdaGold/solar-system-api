from app.models.planet import Planet

def test_get_all_planets(client, two_saved_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0]["name"] == "Earth"
    assert response_body[0]["description"] == "humans live here"
    assert response_body[0]["position_from_sun"] == 3

def test_create_one_planet(client):
    EXPECTED_PLANET = {
        "name": "Venus",
        "description": "hottest planet in the solar system",
        "position_from_sun": 2
    }
    response = client.post("/planets", json=EXPECTED_PLANET)
    response_body = response.get_data(as_text=True)

    new_planet = Planet.query.get(1)

    assert response.status_code == 201
    assert response_body == f"Planet {EXPECTED_PLANET['name']} successfully created"

    EXPECTED_PLANET["name"] == new_planet.name
    EXPECTED_PLANET["description"] == new_planet.description
    EXPECTED_PLANET["position_from_sun"] == new_planet.position_from_sun


def test_get_one_planet(client, two_saved_planets):
    response = client.get("/planets/2")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body["name"] == "Mercury"
    assert response_body["description"] == "fastest planet"
    assert response_body["position_from_sun"] == 1


def test_get_nonexistent_planet_returns_404(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message": "planet not found"}


