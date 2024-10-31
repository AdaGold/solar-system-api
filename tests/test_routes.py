def test_get_all_planets_with_no_records(client):
    #Act
    response = client.get("/planets")
    response_body = response.get_json()

    #Assert

    assert response.status_code == 200
    assert response_body == []

def test_get_planet_by_id_returns_404(client): 
    response = client.get("/planets/1") 
    assert response.status_code == 404

def test_get_one_book_succeeds(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mercury",
        "description": "First planet",
        "flag": False
    }

def test_create_one_book(client):
    # Act
    response = client.post("/planets", json={
        "name": "Mercury",
        "description": "First planet",
        "flag": False
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "Mercury",
        "description": "First planet",
        "flag": False
    }