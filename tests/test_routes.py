import pytest
from werkzeug.exceptions import HTTPException
from app.routes.planet_routes import validate_model
from app.models.planet import Planet
from app.models.moon import Moon

# ---------------------------------------
# ---------------------------------------
# ---------Planet route tests--------------
# ---------------------------------------
# ---------------------------------------


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
    assert response_body[0]["name"] == "Mars"
    assert response_body[0]["description"] == "This is planet: Mars"
    assert response_body[0]["gravity"] == 3.721
    assert response_body[0]["distance_from_earth"] == 60.81
    assert response_body[1]["id"] == 2
    assert response_body[1]["name"] == "Jupiter"
    assert response_body[1]["description"] == "This is planet: Jupiter"
    assert response_body[1]["gravity"] == 24.79
    assert response_body[1]["distance_from_earth"] == 467.64


def test_get_planets_no_param_sort_by_id_asc(saved_two_planets, client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body[0]["id"] == 1
    assert response_body[0]["name"] == "Mars"
    assert response_body[0]["description"] == "This is planet: Mars"
    assert response_body[0]["gravity"] == 3.721
    assert response_body[0]["distance_from_earth"] == 60.81
    assert response_body[1]["id"] == 2
    assert response_body[1]["name"] == "Jupiter"
    assert response_body[1]["description"] == "This is planet: Jupiter"
    assert response_body[1]["gravity"] == 24.79
    assert response_body[1]["distance_from_earth"] == 467.64


def test_get_planets_sort_desc_param_sort_by_name_desc(saved_two_planets, client):
    response = client.get("/planets?sort=desc")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body[0]["id"] == 1
    assert response_body[0]["name"] == "Mars"
    assert response_body[0]["description"] == "This is planet: Mars"
    assert response_body[0]["gravity"] == 3.721
    assert response_body[0]["distance_from_earth"] == 60.81
    assert response_body[1]["id"] == 2
    assert response_body[1]["name"] == "Jupiter"
    assert response_body[1]["description"] == "This is planet: Jupiter"
    assert response_body[1]["gravity"] == 24.79
    assert response_body[1]["distance_from_earth"] == 467.64


def test_get_planets_sort_desc_param_sort_by_name_asc(saved_two_planets, client):
    response = client.get("/planets?sort=asc")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body[0]["id"] == 2
    assert response_body[0]["name"] == "Jupiter"
    assert response_body[0]["description"] == "This is planet: Jupiter"
    assert response_body[0]["gravity"] == 24.79
    assert response_body[0]["distance_from_earth"] == 467.64
    assert response_body[1]["id"] == 1
    assert response_body[1]["name"] == "Mars"
    assert response_body[1]["description"] == "This is planet: Mars"
    assert response_body[1]["gravity"] == 3.721
    assert response_body[1]["distance_from_earth"] == 60.81


def test_get_planets_sort_by_gravity_desc(saved_two_planets, client):
    data = {"sort": "gravity:desc"}
    response = client.get("/planets", query_string=data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body[0]["id"] == 2
    assert response_body[0]["name"] == "Jupiter"
    assert response_body[0]["description"] == "This is planet: Jupiter"
    assert response_body[0]["gravity"] == 24.79
    assert response_body[0]["distance_from_earth"] == 467.64
    assert response_body[1]["id"] == 1
    assert response_body[1]["name"] == "Mars"
    assert response_body[1]["description"] == "This is planet: Mars"
    assert response_body[1]["gravity"] == 3.721
    assert response_body[1]["distance_from_earth"] == 60.81


def test_get_planets_sort_planets_by_name_desc_order(saved_two_planets, client):
    data = {"sort": "name:desc"}
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body[1]["id"] == 2
    assert response_body[1]["name"] == "Jupiter"
    assert response_body[1]["description"] == "This is planet: Jupiter"
    assert response_body[1]["gravity"] == 24.79
    assert response_body[1]["distance_from_earth"] == 467.64
    assert response_body[0]["id"] == 1
    assert response_body[0]["name"] == "Mars"
    assert response_body[0]["description"] == "This is planet: Mars"
    assert response_body[0]["gravity"] == 3.721
    assert response_body[0]["distance_from_earth"] == 60.81


def test_get_planets_sort_by_distance_from_earth_asc(saved_two_planets, client):
    data = {"sort": "distance_from_earth:asc"}
    response = client.get("/planets", query_string=data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body[1]["id"] == 2
    assert response_body[1]["name"] == "Jupiter"
    assert response_body[1]["description"] == "This is planet: Jupiter"
    assert response_body[1]["gravity"] == 24.79
    assert response_body[1]["distance_from_earth"] == 467.64
    assert response_body[0]["id"] == 1
    assert response_body[0]["name"] == "Mars"
    assert response_body[0]["description"] == "This is planet: Mars"
    assert response_body[0]["gravity"] == 3.721
    assert response_body[0]["distance_from_earth"] == 60.81


def test_get_planets_sort_planets_by_distance_from_earth_desc(saved_two_planets, client):
    data = {"sort": "distance_from_earth:desc"}
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body[1]["id"] == 2
    assert response_body[1]["name"] == "Jupiter"
    assert response_body[1]["description"] == "This is planet: Jupiter"
    assert response_body[1]["gravity"] == 24.79
    assert response_body[1]["distance_from_earth"] == 467.64
    assert response_body[0]["id"] == 1
    assert response_body[0]["name"] == "Mars"
    assert response_body[0]["description"] == "This is planet: Mars"
    assert response_body[0]["gravity"] == 3.721
    assert response_body[0]["distance_from_earth"] == 60.81


def test_get_planets_filter_by_planet_name_return_Mars_only(saved_two_planets, client):
    data = {"name": "Mars"}
    response = client.get("/planets", query_string=data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body[0]["id"] == 1
    assert response_body[0]["name"] == "Mars"
    assert response_body[0]["description"] == "This is planet: Mars"
    assert response_body[0]["gravity"] == 3.721
    assert response_body[0]["distance_from_earth"] == 60.81


def test_get_planets_filter_by_gravity_return_Mars_only(saved_two_planets, client):
    data = {"gravity": 3.721}
    response = client.get("/planets", query_string=data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body[0]["id"] == 1
    assert response_body[0]["name"] == "Mars"
    assert response_body[0]["description"] == "This is planet: Mars"
    assert response_body[0]["gravity"] == 3.721
    assert response_body[0]["distance_from_earth"] == 60.81


def test_get_planets_filter_by_distance_from_earth_return_Jupiter_only(saved_two_planets, client):
    data = {"distance_from_earth": 467.64}
    response = client.get("/planets", query_string=data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body[0]["id"] == 2
    assert response_body[0]["name"] == "Jupiter"
    assert response_body[0]["description"] == "This is planet: Jupiter"
    assert response_body[0]["gravity"] == 24.79
    assert response_body[0]["distance_from_earth"] == 467.64


def test_get_planets_filter_by_planet_Jupiter_return_Jupiter_only(saved_two_planets, client):
    data = {"name": "Jupiter"}
    response = client.get("/planets", query_string=data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body[0]["id"] == 2
    assert response_body[0]["name"] == "Jupiter"
    assert response_body[0]["description"] == "This is planet: Jupiter"
    assert response_body[0]["gravity"] == 24.79
    assert response_body[0]["distance_from_earth"] == 467.64


def test_get_planets_filter_by_planet_Mars_sort_by_id_asc(saved_three_planets_with_duplicate_planet_name, client):
    data = {"name": "Mars"}
    response = client.get("/planets", query_string=data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body[0]["id"] == 1
    assert response_body[0]["name"] == "Mars"
    assert response_body[0]["description"] == "This is planet: Mars"
    assert response_body[0]["gravity"] == 3.721
    assert response_body[0]["distance_from_earth"] == 60.81
    assert response_body[1]["id"] == 2
    assert response_body[1]["name"] == "Mars"
    assert response_body[1]["description"] == "This is planet: Mars2"
    assert response_body[1]["gravity"] == 4.721
    assert response_body[1]["distance_from_earth"] == 60.81


def test_get_planets_filter_by_planet_Mars_sort_by_gravity_asc(saved_three_planets_with_duplicate_planet_name, client):
    data = {"name": "Mars", "sort": "gravity"}
    response = client.get("/planets", query_string=data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body[0]["id"] == 1
    assert response_body[0]["name"] == "Mars"
    assert response_body[0]["description"] == "This is planet: Mars"
    assert response_body[0]["gravity"] == 3.721
    assert response_body[0]["distance_from_earth"] == 60.81
    assert response_body[1]["id"] == 2
    assert response_body[1]["name"] == "Mars"
    assert response_body[1]["description"] == "This is planet: Mars2"
    assert response_body[1]["gravity"] == 4.721
    assert response_body[1]["distance_from_earth"] == 60.81


def test_get_planets_filter_by_planet_Mars_sort_by_gravity_desc(saved_three_planets_with_duplicate_planet_name, client):
    data = {"name": "Mars", "sort": "gravity:desc"}
    response = client.get("/planets", query_string=data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body[1]["id"] == 1
    assert response_body[1]["name"] == "Mars"
    assert response_body[1]["description"] == "This is planet: Mars"
    assert response_body[1]["gravity"] == 3.721
    assert response_body[1]["distance_from_earth"] == 60.81
    assert response_body[0]["id"] == 2
    assert response_body[0]["name"] == "Mars"
    assert response_body[0]["description"] == "This is planet: Mars2"
    assert response_body[0]["gravity"] == 4.721
    assert response_body[0]["distance_from_earth"] == 60.81


def test_create_one_planet_return_201_successfully_created(client):
    response = client.post("/planets",
                           json={"name": "Venus",
                                 "description": "This is planet: Venus",
                                 "gravity": 9.87,
                                 "distance_from_earth": 67.685})
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Planet: Venus created successfully."

# edge cases for create one planet


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
    response = client.post("/planets", json=test_data)
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
    resposne = client.put("/planets/9",
                          json={"name": "New Planet",
                                "description": "This a New Planet",
                                "gravity": 20.0,
                                "distance_from_earth": 55.99})
    response_body = resposne.get_json()

    assert resposne.status_code == 404
    assert response_body == {"message": "Planet 9 not found"}


def test_put_invalid_planet__id_return_400_invalid_error(client, saved_two_planets):
    resposne = client.put("/planets/invalid_id",
                          json={"name": "New Planet",
                                "description": "This a New Planet",
                                "gravity": 20.0,
                                "distance_from_earth": 55.99})
    response_body = resposne.get_json()

    assert resposne.status_code == 400
    assert response_body == {"message": "Planet invalid_id is invalid"}


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


def test_delete_exist_planet_associate_moons_also_delete(client, saved_two_planets):
    create_moon_to_planet = client.post("/moons/1/moon",
                                        json={"name": "Moon1"
                                    })
    delete_planet = client.delete("/planets/1")
    delete_planet_response_body = delete_planet.get_json()

    get_moons = client.get("/moons")
    get_moons_response_body = get_moons.get_json()

    assert delete_planet.status_code == 200 
    assert delete_planet_response_body == "Planet: 1 has been deleted successfully."
    assert get_moons.status_code == 200 
    assert get_moons_response_body == []


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

