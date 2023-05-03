# get all planets and return no records
def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

# get one planet by id
def test_get_planet_by_id(client, two_saved_planets):
    # Act
    response1 = client.get('/planets/1')
    response2 = client.get('/planets/2')
    response_body1 = response1.get_json()
    response_body2 = response2.get_json()

    #Assert
    assert response1.status_code == 200
    assert response_body1 == {
        "id": 1,
        "name": "Ocean Planet",
        "description": "Smells fishy",
        "color": "Silver"
    }
    assert response_body2 == {
        "id": 2,
        "name": "Mark",
        "description": "Miniony",
        "color": "Yellow"
    }

def test_create_one_book(client):
    # Act
    response = client.post("/planets", json={
        "name": "New Planet",
        "description": "Fresh out the box"
    })
    response_body = response.get_json()
    # alternative if the return statement does not use jsonify
    # response_body = response.get_data(as_text=True)

    #Assert
    assert response.status_code == 201
    assert response_body == "Planet New Planet successfully created"

def test_planets_with_no_data_returns_404_status_code(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response_body == {"message": "Planet 1 not found"}
    assert response.status_code == 404
