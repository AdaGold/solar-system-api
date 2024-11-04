def test_get_all_planets_with_no_records(client):
    #Act
    response = client.get("/planets")
    response_body = response.get_json()
    
    #Assert
    assert response.status_code == 200
    assert response_body == []
    
def test_get_one_planet(client, two_save_planets):
    #Act
    response = client.get(f"/planets/{two_save_planets[0].id}")
    response_body = response.get_json()
    
    #Assert
    assert response.status_code == 200
    assert response_body == {
        "id": two_save_planets[0].id,
        "name": "Pluto",
        "description": "Dwarf planet known for its complex orbit and atmosphere.",
        "diameter_in_km": 2376,
        "number_of_moons": 5   
    }
    
def test_create_one_planet_in_empty_database(client):
    #Act
    response = client.post("/planets", json={
        "name": "Pluto",
        "description": "Dwarf planet known for its complex orbit and atmosphere.",
        "diameter_in_km": 2376,
        "number_of_moons": 5
    })
    
    response_body = response.get_json()
    
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "Pluto",
        "description": "Dwarf planet known for its complex orbit and atmosphere.",
        "diameter_in_km": 2376,
        "number_of_moons": 5 
    }
    
def test_create_one_planet_already_in_database(client, two_save_planets):
    #Act
    response = client.post("/planets", json={
        "name": "Pluto",
        "description": "Dwarf planet known for its complex orbit and atmosphere.",
        "diameter_in_km": 2376,
        "number_of_moons": 5
    })
    
    response_body = response.get_json()
    
    assert response.status_code == 201
    assert response_body == {
        "id": 3,
        "name": "Pluto",
        "description": "Dwarf planet known for its complex orbit and atmosphere.",
        "diameter_in_km": 2376,
        "number_of_moons": 5 
    }