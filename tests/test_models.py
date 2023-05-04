from app.models.planet import Planet
import pytest

#TESTING TO_DICT ------------------------------------
def test_to_dict_no_missing_data():
    # Arrange
    test_data = Planet(id = 1,
                    name = "Tatooine",
                    description = "Teenage wasteland")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 3
    assert result["id"] == 1
    assert result["name"] == "Tatooine"
    assert result["description"] == "Teenage wasteland"

def test_to_dict_missing_id():
    #arrange
    test_data = Planet(
                        name = "Bespin", 
                        description = "It's a trap!")
    #act
    result = test_data.to_dict()

    #assert
    assert len(result) == 3
    assert result["id"] is None
    assert result["name"] == "Bespin"
    assert result["description"] == "It's a trap!"

def test_to_dict_missing_name():
    #arrange
    test_data = Planet(
        id = 1,
        description = "The Galaxy's Capital"
    )

    #act
    result = test_data.to_dict()

    #assert
    assert len(result) == 3
    assert result["id"] is 1
    assert result["name"] == None
    assert result["description"] == "The Galaxy's Capital"

def test_to_dict_missing_description():
    #arrange
    test_data = Planet(
        id = 1,
        name = "Naboo"
    )

    #act
    result = test_data.to_dict()

    #assert
    assert len(result) == 3
    assert result["id"] is 1
    assert result["name"] == "Naboo"
    assert result["description"] == None

#TESTING FROM DICT ------------------------------
def test_from_dict_returns_planet():
    # Arrange
    planet_data = {
        "name": "Hoth",
        "description": "You're as cold as ice."
    }

    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "Hoth"
    assert new_planet.description == "You're as cold as ice."

def test_from_dict_with_no_name():
    # Arrange
    planet_data = {
        "description": "The Final Frontier"
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'name'):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_with_no_description():
    # Arrange
    planet_data = {
        "name": "Endor"
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'description'):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_with_extra_keys():
    # Arrange
    planet_data = {
        "extra": "not a planet anymore",
        "name": "Alderaan",
        "description": "The planet of beauty",
        "another": "got destroyed by death star"
    }
    
    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "Alderaan"
    assert new_planet.description == "The planet of beauty"    
