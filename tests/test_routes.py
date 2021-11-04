def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_one_book(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Earth",
        "description": "Round and big",
        "color" : "Blue"
    }

def test_get_all_planets_with_records(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [
            {
            "id" : 1,
            "name": "Earth",
            "description": "Round and big",
            "color" : "Blue"
            },
            {
                "id" : 2,
                "name": "Mars",
                "description": "It is on fire",
                "color" : "Red"
            }
        ]
    


def test_post_one_planet(client):
    # Act
    new_planet = {
        "name" : "Mercury",
        "description" : "Aliens are found",
        "color" : "Blue"
    }
    request = client.post("/planets", json = new_planet)

    # Assert
    assert request.status_code == 201
    

# def test_post_two_books(client):
#     list_new_books = [
#         {
#         "title" : "Hello Mommy",
#         "description" : "You are cute"
#         },
#         {
#         "title" : "Hello Daddy",
#         "description" : "You are cute"
#         }
#     ]

#     response = client.post("/books", json = json.dumps(list_new_books))

#     # Assert
#     assert response.status_code == 201



