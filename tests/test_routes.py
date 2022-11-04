
#`GET` /planets; returns 200 and empty array
from urllib import response


def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

#`GET` /planets/1 returns a response body that matches our fixture
#check if one planet exists, check that status code == 200
def test_get_one_planet(client, one_saved_planet):
    #Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1, 
        "name": "Posh", 
        "description": "very posh"

    }

# `GET`/planets/1  with no data in test database (no fixtures) returns 404
def test_get_one_planet_with_no_records(client):
    #Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 404


# `GET` /planets with valid data (fixtures), returns 200 and populated array
def test_get_one_planet_with_two_records(client, two_saved_planets):
    #Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == {
        "id" : 1,
        "name": "Baby",
        "description": "very smol"
    }

# `POST` /planets with JSON request body, returns 201
def test_create_one_planet(client):
    #Act
    new_planet = {"name": "Sporty", "description": "very sporty"}
    response = client.post("/planets", json = new_planet)
    response_body = response.get_data(as_text = True)

    #Assert
    assert response.status_code == 201
    assert response_body == f"Planet {new_planet['name']} successfully created"