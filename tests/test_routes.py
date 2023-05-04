from app.models.planet import Planet
from app.routes import validate_model
from werkzeug.exceptions import HTTPException
import pytest


def test_get_planets_returns_empty_list_when_db_is_empty(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client, one_planet):
    
    response = client.get(f"/planets/{one_planet.id}")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body["id"] == one_planet.id
    assert response_body["name"] == one_planet.name
    assert response_body["description"] == one_planet.description
    assert response_body["distance"] == one_planet.distance


def test_get_one_empty_planet(client):

    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message":f"Planet 1 not found"}, 404

def test_create_planet_creates_planet(client):
    EXPECTED_PLANET = {
        "name" : "Draconis",
        "description" : "Arion",
        "distance" : "150 billion miles"
    }

    response = client.post("/planets", json=EXPECTED_PLANET)
    response_body = response.get_data(as_text=True)

    actual_planet = Planet.query.get(1)
    assert response.status_code == 201
    assert response_body == f"Planet {EXPECTED_PLANET['name']} successfully created"
    assert actual_planet.name == EXPECTED_PLANET["name"]
    assert actual_planet.description == EXPECTED_PLANET["description"]
    assert actual_planet.distance == EXPECTED_PLANET["distance"]

def test_validate_model_returns_invalid_with_invalid_id(client):
    with pytest.raises(HTTPException):
        result_planet = validate_model(Planet, "planet")

def test_delete_planet_missing_record(client, one_planet):
    response = client.delete("/planets/35")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message" : "Planet 35 not found"}
    