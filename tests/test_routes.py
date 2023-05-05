from app.models.planet import Planet

def test_get_all_planets_returns_empty_list_when_db_is_empty(client):
    #act
    response = client.get("/planets")

    #assert 
    assert response.status_code == 200
    assert response.get_json() == []

def test_get_all_planets_with_two_records(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0] == {
        "id": 1,
        "name" : "Tatooine",
        "description" : "Teenage"
    }
    assert response_body[1] == {
        "id": 2,
        "name": "Hoth",
        "description": "You're a cold as ice"
    }

def test_get_all_planets_with_title_query_matching_none(client, two_saved_planets):
    # Act
    data = {"name": "Why can't this project due Monday?"}
    response = client.get("/planets", query_string = data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_all_books_with_title_query_matching_one(client, two_saved_planets):
    # Act
    data = {"name": "Hoth"}
    response = client.get("/planets", query_string = data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body[0] == {
        "id": 2,
        "name": "Hoth",
        "description": "You're a cold as ice"
    }


def test_get_one_planet_returns_seeded_planet(client, one_planet):
    response = client.get(f"/planets/{one_planet.id}")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body["id"] == one_planet.id
    assert response_body["name"] == one_planet.name
    assert response_body["description"] == one_planet.description

def test_get_one_book_id_not_found(client, two_saved_planets):
    # Act
    response = client.get("/planets/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Planet 3 not found"}

def test_get_one_book_id_invalid(client, two_saved_planets):
    # Act
    response = client.get("/planets/needsleep")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message":"Planet needsleep is invalid"}


def test_create_one_planet_happy_path(client):
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
