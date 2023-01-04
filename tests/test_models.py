from app.models.planet import Planet

def test_to_dict_no_missing_data():
    # Arrange
    test_data = Planet(id = 1, 
                name="Mars",
                description="This is planet: Mars",
                gravity=3.721,
                distance_from_earth=60.81)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 5
    assert result["id"] == 1
    assert result["name"] == "Mars"
    assert result["description"] == "This is planet: Mars"
    assert result["gravity"] == 3.721
    assert result["distance_from_earth"] == 60.81

def test_to_dict_missing_id():
    # Arrange
    test_data = Planet(name="Mars",
                description="This is planet: Mars",
                gravity=3.721,
                distance_from_earth=60.81)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 5
    assert result["id"] is None
    assert result["name"] == "Mars"
    assert result["description"] == "This is planet: Mars"
    assert result["gravity"] == 3.721
    assert result["distance_from_earth"] == 60.81

def test_to_dict_missing_title():
    # Arrange
    test_data = Planet(id=1,
                description="This is planet: Mars",
                gravity=3.721,
                distance_from_earth=60.81)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 5
    assert result["id"] == 1
    assert result["name"] is None
    assert result["description"] == "This is planet: Mars"
    assert result["gravity"] == 3.721
    assert result["distance_from_earth"] == 60.81

def test_to_dict_missing_description():
    # Arrange
    test_data = Planet(id = 1,
                    name="Mars",
                    description="This is planet: Mars",
                    gravity=3.721,
                    distance_from_earth=60.81)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 5
    assert result["id"] == 1
    assert result["name"] == "Mars"
    assert result["description"] is None
    assert result["gravity"] == 3.721
    assert result["distance_from_earth"] == 60.81