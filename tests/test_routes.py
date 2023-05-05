from app.models.planet import Planet
from app.routes import validate_id


# get all planets
def test_get_all_planets_returns_empty_list_when_db_is_empty(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [] 


def test_get_all_planets_returns_list_of_planets_when_db_has_two_records(client, two_planets):
    response = client.get("/planets")
    response_body = response.get_json()


    assert response.status_code == 200
    assert response_body == [{"id": 1, "name" : "Jupiter",
                            "description": "King of the Roman gods, aka Zeus.",
                            "number_of_moons": 79},{"id":2, "name" : "Mars","description": "Roman god of war, aka Ares.","number_of_moons": 2}]
    assert len(response_body) == 2
    assert response_body[0]["id"] == two_planets[0].id
    assert response_body[0]["name"] == two_planets[0].name
    assert response_body[0]["description"] == two_planets[0].description
    assert response_body[0]["number_of_moons"] == two_planets[0].number_of_moons
    assert response_body[1]["id"] == two_planets[1].id
    assert response_body[1]["name"] == two_planets[1].name
    assert response_body[1]["description"] == two_planets[1].description
    assert response_body[1]["number_of_moons"] == two_planets[1].number_of_moons

# get one planet
def test_get_one_planet_returns_seeded_planet(client, one_planet):
    response = client.get(f"/planets/{one_planet.id}")
    response_body = response.get_json()
    assert response.status_code == 200
    assert response_body["id"] == one_planet.id
    assert response_body["name"] == one_planet.name
    assert response_body["description"] == one_planet.description
    assert response_body["number_of_moons"] == one_planet.number_of_moons
    assert response_body == {"id": one_planet.id,
                            "name": one_planet.name,
                            "description" : one_planet.description,
                            "number_of_moons" : one_planet.number_of_moons
                            }
    

def test_get_one_planet_with_invalid_id_returns_not_valid_id(client):
    response = client.get(f"/planets/n")
    response_body = response.get_json()
    assert response.status_code == 400
    assert response_body ==  {"message": "this is not a valid id: n"}


def test_get_one_planet_with_not_exsistance_id_returns_not_found(client):
    response = client.get(f"/planets/1")
    response_body = response.get_data(as_text=True)
    assert response.status_code == 404
    assert response_body == "id 1 not found!"

# create a planet
def test_create_one_planet_returns_successfully_created(client):
    expected_planet = {
        "name": "Venus",
        "description": "Roman goddess of love, aka Aphrodite.",
        "number_of_moons": 0
    }
    response=client.post("/planets",json = expected_planet)
    actual_planet = Planet.query.get(1)
    response_body = response.get_json()
    assert response.status_code == 201
    assert response_body == f"Planet Venus successfully created"
    assert actual_planet.name == expected_planet["name"]
    assert actual_planet.description== expected_planet["description"]
    assert actual_planet.number_of_moons == expected_planet["number_of_moons"]

def test_create_one_book_with_extra_keys_returns_successfully_created(client):
    # Arrange
    expected_planet = {"extra" : "wrong",
                "name" : "Jupiter",
                "description": "King of the Roman gods, aka Zeus.",
                "number_of_moons": 79}
    response = client.post("/planets", json=expected_planet)
    response_body = response.get_json()
    actual_planet = Planet.query.get(1)
    assert response.status_code == 201
    assert response_body == f"Planet Jupiter successfully created"
    assert actual_planet.name == expected_planet["name"]
    assert actual_planet.description== expected_planet["description"]
    assert actual_planet.number_of_moons == expected_planet["number_of_moons"]

# replace a planet
def test_replace_planet_returns_seeded_planet(client, one_planet):
    replaced_planet = {
        "name": "Venus",
        "description": "Roman goddess of love, aka Aphrodite.",
        "number_of_moons": 0
    }
    response=client.put(f"/planets/{one_planet.id}", json = replaced_planet) # request
    actual_planet = Planet.query.get(1) # what we have in our database
    response_body = response.get_json()
    assert response.status_code == 200
    assert response_body == f"planet #{one_planet.id} successfully replaced"
    assert actual_planet.id == one_planet.id
    assert actual_planet.name == replaced_planet["name"]
    assert actual_planet.description == replaced_planet["description"]
    assert actual_planet.number_of_moons == replaced_planet["number_of_moons"]

def test_replace_planet_with_extra_key_returns_successfully_replaced(client, one_planet):
    updated_planet = {"extra" : "wrong",
                "name" : "Jupiter",
                "description": "King of the Roman gods, aka Zeus.",
                "number_of_moons": 79}
    response = client.put(f"/planets/{one_planet.id}", json = updated_planet) 
    actual_planet = Planet.query.get(1) 
    response_body = response.get_json()
    assert response.status_code == 200
    assert response_body == f"planet #{one_planet.id} successfully replaced"
    assert actual_planet.name == updated_planet["name"]
    assert actual_planet.id == one_planet.id 
    assert actual_planet.description == one_planet.description
    assert actual_planet.number_of_moons == one_planet.number_of_moons

def test_replace_one_planet_with_invalid_id_returns_not_valid_id(client):
    response = client.put(f"/planets/n")
    response_body = response.get_json()
    assert response.status_code == 400
    assert response_body ==  {"message": "this is not a valid id: n"}


def test_replace_one_planet_with_not_exsistance_id_returns_not_found(client):
    response = client.put(f"/planets/1")
    response_body = response.get_data(as_text=True)
    assert response.status_code == 404
    assert response_body == "id 1 not found!"

# Update a planet
def test_update_planet_returns_seeded_planet(client, one_planet):
    updated_planet = {
        "name": "Venus",
    }
    response=client.patch(f"/planets/{one_planet.id}", json = updated_planet) 
    actual_planet = Planet.query.get(1) 
    response_body = response.get_json()
    assert response.status_code == 200
    assert response_body == f"planet #{one_planet.id} successfully updated"
    assert actual_planet.name == updated_planet["name"]
    assert actual_planet.id == one_planet.id 
    assert actual_planet.description == one_planet.description
    assert actual_planet.number_of_moons == one_planet.number_of_moons

def test_update_planet_with_extra_keys_returns_successfully_replaced(client, one_planet):
    # Arrange
    updated_planet = {"extra" : "wrong",
                "name" : "Jupiter",
                "description": "King of the Roman gods, aka Zeus.",
                "number_of_moons": 79}
    response = client.patch(f"/planets/{one_planet.id}", json = updated_planet) 
    actual_planet = Planet.query.get(1) 
    response_body = response.get_json()
    assert response.status_code == 200
    assert response_body == f"planet #{one_planet.id} successfully updated"
    assert actual_planet.name == updated_planet["name"]
    assert actual_planet.id == one_planet.id 
    assert actual_planet.description == one_planet.description
    assert actual_planet.number_of_moons == one_planet.number_of_moons

def test_update_one_planet_with_invalid_id_returns_not_valid_id(client):
    response = client.patch(f"/planets/n")
    response_body = response.get_json()
    assert response.status_code == 400
    assert response_body ==  {"message": "this is not a valid id: n"}


def test_update_one_planet_with_not_exsistance_id_returns_not_found(client):
    response = client.patch(f"/planets/1")
    response_body = response.get_data(as_text=True)
    assert response.status_code == 404
    assert response_body == "id 1 not found!"

# Delete a planet
def test_delete_one_planet_returns_successfylly_deleted(client, one_planet):
    response = client.delete(f"/planets/{one_planet.id}")
    actual_planet = Planet.query.get(1)
    assert response.status_code == 200
    assert actual_planet == None

def test_delete_one_planet_with_invalid_id_returns_not_valid_id(client):
    response = client.delete(f"/planets/n")
    response_body = response.get_json()
    assert response.status_code == 400
    assert response_body ==  {"message": "this is not a valid id: n"}


def test_delete_one_planet_with_not_exsistance_id_returns_not_found(client):
    response = client.delete(f"/planets/1")
    response_body = response.get_data(as_text=True)
    assert response.status_code == 404
    assert response_body == "id 1 not found!"

