from app.models.planet import Planet

def test_get_all_planets_with_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client, two_saved_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id" : 1, 
        "name" : "Mars",
        "description" : "musty and cold",
        "cycle_len" : 780
    }

def test_plannet_no_data(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404

def test_get_all_planets_with_records(client, two_saved_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    planet_1 = {
        "id" : 1, 
        "name" : "Mars",
        "description" : "musty and cold",
        "cycle_len" : 780
    }

    planet_2 = {
        "id" : 2, 
        "name" : "Neptune",
        "description" : "its a planet",
        "cycle_len" : 1080
    }

    assert response.status_code == 200
    assert isinstance(response_body, list)
    assert planet_1 in response_body
    assert planet_2 in response_body

def test_post_data_201_and_in_db(client):
    planet = {
        "name": "Earth",
        "description": "green and blue thing with humans",
        "cycle_len": 365
    }

    response = client.post("/planets", json = planet)

    assert response.status_code == 201

    response = client.get("/planets")
    response_body = response.get_json()
    
    planet["id"] = 1
    assert planet in response_body