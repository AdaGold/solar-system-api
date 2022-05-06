def test_get_all_planets_with_no_records(client):
    # act
    response = client.get("/planets")
    response_body = response.get_json()

    # assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client, two_saved_planets):
    # act
    response = client.get("planets/1")
    response_body = response.get_json()

    # assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Neptune",
        "description": "ice",
        "distance_from_sun": 9
    }


def test_get_one_planet_with_no_records(client):
    # act
    response = client.get("planets/1")
    response_body = response.get_json()

    # assert
    assert response.status_code == 404
    assert response_body == {"message": "planet 1 not found"}


def test_get_all_planets_return_array(client, two_saved_planets):
    # act
    response = client.get("/planets")
    response_body = response.get_json()

    # assert
    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "Neptune",
        "description": "ice",
        "distance_from_sun": 9
    }, 
        {"id": 2,
        "name": "Earth",
        "description": "water",
        "distance_from_sun": 3
        }
    ]

def test_post_planet_returns_201(client):    
    # act
    response = client.post("/planets", json={
        "name": "Mercury",
        "description": "fast",
        "distance from sun": 1
    })
    response_body = response.get_json()

    # assert
    assert response.status_code == 201
    assert response_body == "planet Mercury successfully created!"