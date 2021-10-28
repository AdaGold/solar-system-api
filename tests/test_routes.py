def test_get_one_planet_with_record(client, create_two_planets):
    #Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body["name"] == "Not Planet"

def test_get_one_planets_with_no_record(client):
    #Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 404
    assert response_body == None

def test_get_all_planets_with_records(client, create_two_planets):
    #Act
    response = client.get("/planets")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert len(response_body) == 2

def test_post_new_planet(client):
    #Act
    data = {
        "name": "A really new planet", 
        "description": "Just discovered yesterday ;)",
        "mythology": "God of disbelief"
    }
    response = client.post("/planets", json = data)

    #Assert
    assert response.status_code == 201
