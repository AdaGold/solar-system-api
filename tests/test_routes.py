def test_get_all_planets_with_no_records(client):
    response = client.get('/planets')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_planets_with_one_record(one_planet, client):
    response = client.get('/planets')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [{
        "description": "Mercury has 0 moon(s).",
        "id": 1,
        "name": "Mercury",
        "num_of_moons": 0
    }]