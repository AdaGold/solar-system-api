import pytest
from app.models.planet import Planet

def test_planet_from_dict_returns_planet():
    # Arrange
    planet_data = {
        "name": "Mercury",
        "description": "Mercury is the smallest planet of our solar system.",
        "is_rocky": True
    }

    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "Mercury"
    assert new_planet.is_rocky == True
    assert new_planet.description == "Mercury is the smallest planet of our solar system."

def test_planet_from_dict_with_no_name():
    # Arrange
    planet_data = {
        "description": "Mercury is the smallest planet of our solar system.",
        "is_rocky": True
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'name'):
        new_planet = Planet.from_dict(planet_data)

def test_planet_from_dict_with_no_description():
    # Arrange
    planet_data = {
        "name": "Mercury",
        "is_rocky": True
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'description'):
        new_planet = Planet.from_dict(planet_data)

def test_planet_from_dict_with_no_is_rocky():
    # Arrange
    planet_data = {
        "name": "Mercury",
        "description": "Mercury is the smallest planet of our solar system."
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'is_rocky'):
        new_planet = Planet.from_dict(planet_data)

def test_planet_from_dict_with_extra_keys():
    # Arrange
    planet_data = {
        "name": "Mercury",
        "description": "Mercury is the smallest planet of our solar system.",
        "is_rocky": True,
        "my_extra": 2
    }
    
    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "Mercury"
    assert new_planet.is_rocky == True
    assert new_planet.description == "Mercury is the smallest planet of our solar system."