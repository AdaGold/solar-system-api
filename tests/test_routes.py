import pytest
from werkzeug.exceptions import HTTPException
from app.planet_routes import validate_model
from app.models.planet import Planet 
from app.models.moon import Moon

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
    assert response_body == {"message": "Planet hello is invalid"}


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
def test_create_one_planet_no_name_return_400(client):
    
    response = client.post("/planets",
                        json={"description": "This is planet: Venus",
                                "gravity": 9.87,
                                "distance_from_earth": 67.685})

    assert response.status_code == 400


def test_create_one_planet_no_description_return_400(client):
    response = client.post("/planets",
                    json={"name": "Mars",
                    "gravity": 9.87,
                    "distance_from_earth": 67.685})

    assert response.status_code == 400

def test_create_one_planet_no_gravity_return_400(client):
    test_data = {"name": "Mars",
                "description": "This is planet: Venus",
                "distance_from_earth": 67.685
                }
    response = client.post("/planets", json = test_data)
    assert response.status_code == 400 

def test_create_one_planet_with_extra_keys_return_201(client, saved_two_planets):
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
    assert response_body == "Planet: Venus created successfully."

def test_put_planet_with_id_1_return_200_planet_successfully_replaced(client, saved_two_planets):
    resposne = client.put("/planets/1",
                        json={"name": "New Planet",
                                "description": "This a New Planet",
                                "gravity": 20.0,
                                "distance_from_earth": 55.99})
    response_body = resposne.get_json()

    assert resposne.status_code == 200
    assert response_body == "Planet: 1 has been updated successfully." 

def test_put_non_existing_planet_return_404_not_found_error(client, saved_two_planets):
    # with pytest.raises(HTTPException):
    #     resposne = client.put("/planets/9",
    #                     json={"name": "New Planet",
    #                             "description": "This a New Planet",
    #                             "gravity": 20.0,
    #                             "distance_from_earth": 55.99})

    resposne = client.put("/planets/9",
                        json={"name": "New Planet",
                                "description": "This a New Planet",
                                "gravity": 20.0,
                                "distance_from_earth": 55.99})
    response_body = resposne.get_json()

    assert resposne.status_code == 404
    assert response_body == {"message":"Planet 9 not found"}

def test_put_invalid_planet__id_return_400_invalid_error(client, saved_two_planets):
    resposne = client.put("/planets/invalid_id",
                        json={"name": "New Planet",
                                "description": "This a New Planet",
                                "gravity": 20.0,
                                "distance_from_earth": 55.99})
    response_body = resposne.get_json()

    assert resposne.status_code == 400
    assert response_body == {"message":"Planet invalid_id is invalid"}

def test_delete_planet_with_id_1_return_200_planet_successfully_deleted(client, saved_two_planets):
    response = client.delete("planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == "Planet: 1 has been deleted successfully."

def test_delete_planet_with_non_exist_id_return_404_not_found_error(client, saved_two_planets):
    response = client.delete("planets/10")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message": "Planet 10 not found"}

def test_delete_planet_with_invalid_id_return_400_invalid_error(client, saved_two_planets):
    response = client.delete("planets/invalid_id")
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {"message": "Planet invalid_id is invalid"}

def test_validate_model(saved_two_planets):
    result_planet = validate_model(Planet, 1)

    assert result_planet.id == 1
    assert result_planet.name == "Mars"
    assert result_planet.description == "This is planet: Mars"
    assert result_planet.gravity == 3.721 
    assert result_planet.distance_from_earth == 60.81
    assert result_planet.moons == []

def test_validate_model_missing_record(saved_two_planets):
    # Calling `validate_model` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached 
    with pytest.raises(HTTPException):
        result_planet = validate_model(Planet, "3")
    
def test_validate_model_invalid_id(saved_two_planets):
    with pytest.raises(HTTPException):
        result_planet = validate_model(Planet, "invalid_id")

#---------------------------------------
#---------------------------------------
#---------Moon route tests--------------
#---------------------------------------
#---------------------------------------

def test_get_moon_by_id_return_200_successful_code(client, saved_two_moons):
    response = client.get("/moons/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body["name"] == "Moon1"


def test_get_moon_by_not_exist_id_return_404(client):
    response = client.get("/moons/1")
    response_body = response.get_json()

    assert response.status_code == 404

def test_get_moon_by_invalid_moon_id_return_400_bad_request_error(client, saved_two_moons): 
    response = client.get("/moons/hello")
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {"message": "Moon hello is invalid"}


def test_get_all_moons_with_no_records_return_empty_array(client):
    response = client.get("/moons/all")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []


def test_get_all_moons_with_two_records_return_array_with_size_2(client, saved_two_moons):
    response = client.get("/moons")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0]["id"] == 1 
    assert response_body[0]["name"]== "Moon1"
    assert response_body[0]["planet_id"] ==1
    assert response_body[0]["planet"] == "Mars"
    assert response_body[1]["id"] == 2
    assert response_body[1]["name"]== "Moon2"
    assert response_body[1]["planet_id"] == 1
    assert response_body[1]["planet"] =="Mars"


def test_create_one_moon_return_201_successfully_created(client):
    response = client.post("/moons",
                        json={"name": "Moon3",
                                "planet": "Jupiter",
                                "planet_id": 2})
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Moon Moon3 successfully created."

def test_create_one_moon_under_planet_return_201_successfully_created(client,saved_two_planets):
    response = client.post("/2/moon",
                        json= {"name": "Moon3",
                                "planet": "Jupiter",
                                "planet_id": 2})
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Moon Moon3 successfully created to planet 2"


def test_validate_moon_model(saved_two_moons):
    result_moon = validate_model(Moon, 1)

    assert result_moon.id == 1
    assert result_moon.name == "moon1"
    assert result_moon.planet_id == 1
    assert result_moon.planet == "Mars"

def test_validate_model_missing_moon_record(saved_two_moons):
    # Calling `validate_model` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached 
    with pytest.raises(HTTPException):
        result_planet = validate_model(Moon, "3")
    
def test_validate_model_invalid_moon_id(saved_two_moons):
    with pytest.raises(HTTPException):
        result_planet = validate_model(Moon, "invalid_id")

