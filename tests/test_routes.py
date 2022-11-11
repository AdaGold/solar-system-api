from app.models.planet import Planet
from app.routes.routes_helper import validate_model
import pytest


# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_planets_no_saved_planets(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_planets_one_saved_planet(client, one_planet):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body == [
        {
            "id": 1,
            "name": "Earth",
            "description": "Earth description",
            "moons": 2
        }
    ]


# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_planet(client, one_planet):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "planet" in response_body
    assert response_body == {
        "planet": {
            "id": 1,
            "name": "Earth",
            "description": "Earth description",
            "moons": 2
        }
    }


# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_planet_not_found(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": f"Planet 1 not found"}, 404


# @pytest.mark.skip(reason="No way to test this feature yet")
def test_create_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "A Brand New Planet",
        "description": "Planet Description",
        "moons": 2
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert "planet" in response_body
    assert response_body == {
        "planet": {
            "id": 1,
            "name": "A Brand New Planet",
            "description": "Planet Description",
            "moons": 2
        }
    }
    new_planet = Planet.query.get(1)
    assert new_planet
    assert new_planet.name == "A Brand New Planet"
    assert new_planet.description == "Planet Description"
    assert new_planet.moons == 2


# @pytest.mark.skip(reason="No way to test this feature yet")
def test_update_planet(client, one_planet):
    # Act
    response = client.put("/planets/1", json={
        "name": "Updated Planet Name",
        "description": "Updated Planet Description",
        "moons": 2
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "planet" in response_body
    assert response_body == {
        "planet": {
            "id": 1,
            "name": "Updated Planet Name",
            "description": "Updated Planet Description",
            "moons": 2
        }
    }
    planet = Planet.query.get(1)
    assert planet.name == "Updated Planet Name"
    assert planet.description == "Updated Planet Description"
    assert planet.moons == 2


# @pytest.mark.skip(reason="No way to test this feature yet")
def test_update_planet_not_found(client):
    # Act
    response = client.put("/planets/1", json={
        "name": "Updated Planet Name",
        "description": "Updated Planet Description",
        "moons": 1
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": f"Planet 1 not found"}, 404


# @pytest.mark.skip(reason="No way to test this feature yet")
def test_delete_planet(client, one_planet):
    # Act
    response = client.delete("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "details" in response_body
    assert response_body == {
        "details": 'planet 1 "Earth" successfully deleted'
    }
    assert Planet.query.get(1) == None


# @pytest.mark.skip(reason="No way to test this feature yet")
def test_delete_planet_not_found(client):
    # Act
    response = client.delete("/planets/1")
    response_body = response.get_json()

    # Assert
    assert Planet.query.all() == []
    assert response.status_code == 404

    # **Complete test with assertion about response body**
    assert response_body == {"message": f"Planet 1 not found"}, 404


# @pytest.mark.skip(reason="No way to test this feature yet")
def test_create_planet_must_contain_name(client):
    # Act
    response = client.post("/planets", json={
        "description": "Planet Description"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert "details" in response_body
    assert response_body == {
        "details": "Invalid data"
    }
    assert Planet.query.all() == []


# @pytest.mark.skip(reason="No way to test this feature yet")
def test_create_planet_must_contain_description(client):
    # Act
    response = client.post("/planets", json={
        "name": "A Brand New Planet"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert "details" in response_body
    assert response_body == {
        "details": "Invalid data"
    }
    assert Planet.query.all() == []


