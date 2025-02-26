def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_all_planets(client, saved_all_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [ {
        "description": "Hottest planet",
        "has_flag": False,
        "id": 1,
        "moons": 0,
        "name": "Venus",
        "size": "small"
    },
    {
        "description": "Closest to the Sun, very hot",
        "has_flag": False,
        "id": 2,
        "moons": 0,
        "name": "Mercury",
        "size": "Small"
    },
    {
        "description": "Thick atmosphere, hottest planet",
        "has_flag": False,
        "id": 3,
        "moons": 0,
        "name": "Venus",
        "size": "Small"
    },
    {
        "description": "Home to life, oceans and land",
        "has_flag": True,
        "id": 4,
        "moons": 1,
        "name": "Earth",
        "size": "Medium"
    },
    {
        "description": "Known as the Red Planet",
        "has_flag": True,
        "id": 5,
        "moons": 2,
        "name": "Mars",
        "size": "Small"
    },
    {
        "description": "Largest planet, gas giant",
        "has_flag": False,
        "id": 6,
        "moons": 79,
        "name": "Jupiter",
        "size": "Large"
    },
    {
        "description": "Known for its rings",
        "has_flag": False,
        "id": 7,
        "moons": 83,
        "name": "Saturn",
        "size": "Large"
    },
    {
        "description": "Icy gas giant, tilted axis",
        "has_flag": False,
        "id": 8,
        "moons": 27,
        "name": "Uranus",
        "size": "Large"
    }
    ]

def test_get_one_planet_with_records(client, saved_all_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "description": "Hottest planet",
        "has_flag": False,
        "id": 1,
        "moons": 0,
        "name": "Venus",
        "size": "small"
        }
    
def test_get_one_planet_with_no_records(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"msg": "Planet id 1 not found."}
    
def test_get_one_planet_with_no_matching_id(client, saved_all_planets):
    # Act
    response = client.get("/planets/125")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"msg": "Planet id 125 not found."}

def test_create_planet_with_valid_data(client):
    # Act
    response = client.post("/planets", json={"name":"9ND-87", "description":"black, almost invisible", "size":"small", "moons":42, "has_flag":False})
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id":1,
        "name":"9ND-87", 
        "description":"black, almost invisible", 
        "size":"small", 
        "moons":42, 
        "has_flag":False
        }

    

