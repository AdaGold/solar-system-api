def test_get_all_planets_with_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_found(client, two_saved_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Pluto",
        "description": "The wise time guardian, responsible for protecting the gates of time and space.",
        "number_of_moons": 5
    }

def test_get_one_planet_not_found(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message": "id 1 not found"}

def test_get_all_planets_succeeds_with_records(client, two_saved_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [
        {
            "id": 1,
            "name": "Pluto",
            "description": "The wise time guardian, responsible for protecting the gates of time and space.",
            "number_of_moons": 5
        },
        {
            "id": 2,
            "name": "Mercury",
            "description": "The intelligent strategist, known for her analytical skills and love of books.",
            "number_of_moons": 0
        }
    ]

def test_create_one_planet(client):
    response = client.post("/planets", json={
        "name": "Ceres", 
        "description": "The nurturing spirit who brings harmony and balance, always caring for her friends.", 
        "number_of_moons": 0
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "Ceres", 
        "description": "The nurturing spirit who brings harmony and balance, always caring for her friends.", 
        "number_of_moons": 0
    }