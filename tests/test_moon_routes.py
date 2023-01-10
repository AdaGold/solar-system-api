from app.models.moon import Moon

MOON_NAME = "Test Moon"
MOON_SIZE = 100
MOON_DESCRIPTION = "This is a test moon."
MOON_GRAVITY = 0.1

def test_get_one_moon_with_no_records(client):
    response = client.get("moons/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {'message': 'Moon id 1 is Not Found'}

def test_get_one_moon_with_records(client, one_planet_with_two_moons):
    response = client.get("moons/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body["name"] == "Phobos" 

def test_get_one_moon_with_moon_name_query(client, one_planet_with_two_moons):
    response = client.get("moons?moon_name=Phobos")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body[0]["name"] == "Phobos"

def test_get_all_moons_with_desc_sort(client, one_planet_with_two_moons):
    response = client.get("/moons?sort=desc")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body[0]["name"] == "Phobos"

def test_get_all__moons_with_asc_sort(client, one_planet_with_two_moons):
    response = client.get("/moons?sort=asc")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body[0]["name"] == "Deimos"

def test_get_one_planet_with_no_records(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message":"Planet id 1 is Not Found" }

def test_get_one_planet_invalid_id(client):
    response = client.get("/planets/hello")
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {"message":"Planet id hello is Invalid" }

def test_update_moon_valid_input(client, one_planet_with_two_moons):
    test_data = {
        "name":MOON_NAME,
        "size": MOON_SIZE,
        "description":MOON_DESCRIPTION,        
        "gravity": MOON_GRAVITY
    }

    response = client.put("/moons/1", json=test_data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == f"Moon {MOON_NAME} successfully updated"

    updated_moon = Moon.query.get(1)

    assert updated_moon.name == MOON_NAME
    assert updated_moon.size == MOON_SIZE
    assert updated_moon.description == MOON_DESCRIPTION
    assert updated_moon.gravity == MOON_GRAVITY

def test_delete_planet_valid_id(client, one_planet_with_two_moons):
    deleted_moon = Moon.query.get(1)
    response = client.delete("moons/1")
    response_body = response.get_json()
    

    assert response.status_code == 200
    assert response_body ==f"Moon {deleted_moon.name} successfully deleted"