def test_get_all_planets_with_no_records(client):
    response = client.get('/planets')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_all_planets(many_planets, client):
    response = client.get('/planets')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [{
        "description": "Mercury has 0 moon(s).",
        "id": 1,
        "name": "Mercury",
        "num_of_moons": 0
    },
    {
        "description": "Venus has 0 moon(s).",
        "id": 2,
        "name": "Venus",
        "num_of_moons": 0
    }]

def test_get_planets_with_one_id(one_planet, client):
    response = client.get('/planets/1')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "description": "Mercury has 0 moon(s).",
        "id": 1,
        "name": "Mercury",
        "num_of_moons": 0
    }

def test_get_one_planet_404(client, one_planet):
    response = client.get('/planets/2')
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == None

def test_post_one_planet_success(client):
    response = client.post('/planets', json=[{
        "name": "Mercury",
        "num_of_moons": 0
    }])
    response_body = response.get_json()

    assert response.status_code == 201

def test_put_one_planet_success(client, one_planet):
    response = client.put('/planets/1', json={
        "num_of_moons": 5
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {
        "description": "Mercury has 0 moon(s).",
        "id": 1,
        "name": "Mercury",
        "num_of_moons": 5
    }

def test_delete_one_planet_success(client, one_planet):
    response = client.delete('/planets/1')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {"message": f"Deleted Mercury with 1"}