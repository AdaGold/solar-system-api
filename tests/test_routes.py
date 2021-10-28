def get_empty_list_of_planets(client, list_of_planets):

    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []
    