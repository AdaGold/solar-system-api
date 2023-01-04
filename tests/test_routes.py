import pytest

def test_get_planet_by_id_return_200_successful_code(client, saved_two_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body["name"] == "Mars"


def test_get_planet_by_not_exist_id_return_404(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404

def test_get_planet_by_invalid_planet_id_return_400_bad_request_error(client, saved_two_planets): 
    response = client.get("/planets/hello")
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {"message": "Planet_id hello is invalid"}


def test_get_all_planets_with_no_records_return_empty_array(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []


def test_get_all_planets_with_two_records_return_array_with_size_2(client, saved_two_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0]["id"] == 1 
    assert response_body[0]["name"]== "Mars"
    assert response_body[0]["description"] =="This is planet: Mars"
    assert response_body[0]["gravity"] == 3.721
    assert response_body[0]["distance_from_earth"] == 60.81
    assert response_body[1]["id"] == 2 
    assert response_body[1]["name"]== "Jupiter"
    assert response_body[1]["description"] == "This is planet: Jupiter"
    assert response_body[1]["gravity"] == 24.79
    assert response_body[1]["distance_from_earth"] == 467.64

def test_create_one_planet_return_201_successfully_created(client):
    response = client.post("/planets",
                        json={"name": "Venus",
                                "description": "This is planet: Venus",
                                "gravity": 9.87,
                                "distance_from_earth": 67.685})
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Planet: Venus created successfully."

#####edge cases for create one planet
def test_create_one_planet_no_name(client):
    test_data = {"description": "This is planet: Venus",
                    "gravity": 9.87,
                    "distance_from_earth": 67.685}

    with pytest.raises(KeyError, match='name'):
        response = client.post("/planets", json=test_data)

def test_create_one_planet_no_description(client):
    test_data = {"name": "Mars",
                    "gravity": 9.87,
                    "distance_from_earth": 67.685}

    with pytest.raises(KeyError, match='description'):
        response = client.post("/planets", json=test_data)

def test_create_one_planet_no_gravity(client):
    test_data = {"name": "Mars",
                    "description": "This is planet: Venus",
                    "distance_from_earth": 67.685}

    with pytest.raises(KeyError, match='gravity'):
        response = client.post("/planets", json=test_data)

def test_create_one_book_with_extra_keys(client, two_saved_books):
    test_data = {
        "extra": "some stuff",
        "name": "Venus",
        "description": "This is planet: Venus",
        "gravity": 9.87,
        "distance_from_earth": 67.685,
        "another": "last value"
    }

    response = client.post("/planets", json=test_data)
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Planet Mars successfully created"

def test_put_planet_with_id_1_return_200_planet_successfully_replaced(client, saved_two_planets):
    resposne = client.put("/planets/1",
                        json={"name": "New Planet",
                                "description": "This a New Planet",
                                "gravity": 20.0,
                                "distance_from_earth": 55.99})
    response_body = resposne.get_json()

    assert resposne.status_code == 200
    assert response_body == "Planet: 1 has been updated successfully."
    assert response_body[0]["id"] == 1 
    assert response_body[0]["name"]== "New Planet"
    assert response_body[0]["description"] =="This a New Planet"
    assert response_body[0]["gravity"] == 20.0
    assert response_body[0]["distance_from_earth"] == 55.99   


def test_delete_planet_with_id_1_return_200_planet_successfully_deleted(client, saved_two_planets):
    response = client.delete("planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == "Planet: 1 has been deleted successfully."

def test_delete_planet_with_non_exist_id_return_404_not_found_error(client, saved_two_planets):
    response = client.delete("planets/10")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message": "Planet_id 10 not found"}



