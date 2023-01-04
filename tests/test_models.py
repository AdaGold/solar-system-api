from app.models.planet import Planet
import pytest

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

def test_to_dict_missing_name():
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


def test_from_dict_returns_book():
    # Arrange
    planet_data = {
        "id":1,
        "name": "Mars",
        "description": "This is planet: Mars",
        "gravity" : 3.721,
        "distance_from_earth" : 60.81
    }

    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "Mars"
    assert new_planet.description == "This is planet: Mars"
    assert new_planet.gravity == 3.721
    assert new_planet.distance_from_earth == 60.81

def test_from_dict_with_no_name():
    # Arrange
    planet_data = {
        "description": "This is planet: Mars!",
        "gravity" : 3.721,
        "distance_from_earth" : 60.81
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'name'):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_with_no_description():
    # Arrange
    planet_data = {
        "name": "Mars",
        "gravity" : 3.721,
        "distance_from_earth" : 60.81
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'description'):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_with_extra_keys():
    # Arrange
    planet_data = {
        "extra": "some stuff",
        "name": "Mars",
        "description": "This is planet: Mars",
        "gravity" : 3.721,
        "distance_from_earth" : 60.81,
        "another": "last value"
    }
    
    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "Mars"
    assert new_planet.description == "This is planet: Mars"
    assert new_planet.gravity == 3.721
    assert new_planet.distance_from_earth == 60.81