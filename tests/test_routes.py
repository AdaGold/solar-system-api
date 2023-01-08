from app.models.planet import Planet


def test_get_planets_optional_query_empty_db_returns_empty_list(client):
    # Act
    response = client.get("/planets")

    # Assert 
    assert response.status_code == 200
    assert response.get_json() == []

def test_get_planet_optional_query_returns_seeded_planet(client, one_planet):
    #Act
    response = client.get("/planets")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body[0] == {
        "description": "Earth is the third planet from the Sun and the only astronomical object known to harbor life.", 
        "distance_from_earth": 0, 
        "name": "Earth", 
        "size": 4,
        "id": 1
    }

def test_get_planet_by_id_returns_seeded_planet(client, one_planet):
    #Act
    response = client.get(f"/planets/{one_planet.id}")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body["id"] == 1
    assert response_body["name"] == "Earth"
    assert response_body["description"] == "Earth is the third planet from the Sun and the only astronomical object known to harbor life."
    assert response_body["size"] ==  4
    assert response_body["distance_from_earth"] ==  0

def test_get_one_planet_invalid_id(client, many_planets):
    # Act
    response = client.get("/planets/falifala")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message": f"Planet falifala invalid"}

def test_get_planet_by_name_with_partial_match_returns_seeded_planet(client, many_planets):
    #Act
    response = client.get("/planets?name=ma")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body[0] == {
        "description": "Mars is the fourth planet from the Sun a dusty, cold, desert world with a very thin atmosphere.",
        "distance_from_earth": 61,
        "id": 2,
        "name": "Mars",
        "size": 7
    }

def test_get_all_planets_with_many_planets(client, many_planets):
    #Act
    response = client.get("/planets")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert len(response_body) == 3
    assert response_body[0] == {
        "description": "Earth is the third planet from the Sun and the only astronomical object known to harbor life.", 
        "distance_from_earth": 0, 
        "name": "Earth", 
        "size": 4,
        "id": 1
    }
    assert response_body[1] == {
        "description": "Mars is the fourth planet from the Sun a dusty, cold, desert world with a very thin atmosphere.", 
        "distance_from_earth": 61, 
        "name": "Mars", 
        "size": 7,
        "id": 2
    }
    assert response_body[2] == {
        "description": "Jupiter is a gas giant with a mass more than two and a half times that of all the other planets combined.", 
        "distance_from_earth": 469,  
        "name": "Jupiter", 
        "size": 1,
        "id": 3
    }

def test_create_one_planet(client):
    #Act
    response = client.post("/planets", json={
        "description": "Venus has crushing air pressure at its surface - more than 90 times that of Earth", 
        "distance_from_earth": 61,  
        "name": "Venus", 
        "size": 6
    })

    response_body = response.get_json()

    #Assert
    assert response.status_code == 201
    assert response_body["size"] == 6

def test_delete_one_planet(client, one_planet):
    #Act
    response = client.delete(f"/planets/{one_planet.id}")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body["id"] == one_planet.id

def test_put_one_planet(client, one_planet):
    # Act
    response = client.put(f"/planets/1", json={
        "description": "Earth is the third planet from the Sun and the only astronomical object known to harbor life.", 
        "distance_from_earth": 0, 
        "name": "Earth", 
        "size": 4,
    })
    response_body = response.get_json()
    #Assert
    assert response.status_code == 200
    assert response_body["size"] == 4

def test_patch_one_planet(client, one_planet):
    # Act
    response = client.patch(f"/planets/1", json={
        "distance_from_earth": 1, 
    })
    response_body = response.get_json()
    #Assert
    assert response.status_code == 200
    assert response_body["distance_from_earth"] == 1

def test_patch_one_planet_with_not_existing_attribute(client, one_planet):
    # Act
    response = client.patch(f"/planets/1", json={
        "distance_from_sun": -1, 
    })
    response_body = response.get_json()
    #Assert
    assert response.status_code == 400
    assert response_body == {"message": f"Attribute distance_from_sun does not exist"}