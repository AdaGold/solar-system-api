from app.models.planet import Planet
from werkzeug.exceptions import HTTPException


def test_to_dict_no_missing_data():
    # Arrange
    test_data = Planet(
                    name="Earth", 
                    size=4,
                    description="Earth is the third planet from the Sun and the only astronomical object known to harbor life.",
                    distance_from_earth=0,
                    id=1 
                    )

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 5
    assert result["id"] == 1
    assert result["name"] == "Earth"
    assert result["description"] == "Earth is the third planet from the Sun and the only astronomical object known to harbor life."
    assert result["size"] == 4
    assert result["distance_from_earth"] == 0

def test_to_dict_missing_id():
    # Arrange
    test_data = Planet(
                    name="Earth",
                    size=4,
                    description="Earth is the third planet from the Sun and the only astronomical object known to harbor life.",
                    distance_from_earth=0
                    )

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 5
    assert result["id"] is None
    assert result["name"] == "Earth"
    assert result["description"] == "Earth is the third planet from the Sun and the only astronomical object known to harbor life."
    assert result["size"] == 4
    assert result["distance_from_earth"] == 0

def test_to_dict_missing_name():
    # Arrange
    test_data = Planet(
                    size=4,
                    description="Earth is the third planet from the Sun and the only astronomical object known to harbor life.",
                    distance_from_earth=0,
                    id=1 
                    )

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 5
    assert result["id"] == 1
    assert result["name"] is None
    assert result["description"] == "Earth is the third planet from the Sun and the only astronomical object known to harbor life."
    assert result["size"] == 4
    assert result["distance_from_earth"] == 0

def test_to_dict_missing_size():
    # Arrange
    test_data = Planet(
                    name="Earth",
                    description="Earth is the third planet from the Sun and the only astronomical object known to harbor life.",
                    distance_from_earth=0,
                    id=1,
    )

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 5
    assert result["id"] == 1
    assert result["name"] == "Earth"
    assert result["description"] == "Earth is the third planet from the Sun and the only astronomical object known to harbor life."
    assert result["distance_from_earth"] == 0

def test_to_dict_missing_description():
    # Arrange
    test_data = Planet(
                    name="Earth", 
                    size=4,
                    distance_from_earth=0,
                    id=1 
    )

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 5
    assert result["id"] == 1
    assert result["name"] == "Earth"
    assert result["description"] is None
    assert result["distance_from_earth"] == 0

def test_to_dict_missing_distance_from_earth():
    # Arrange
    test_data = Planet(
                    name="Earth", 
                    size=4,
                    description="Earth is the third planet from the Sun and the only astronomical object known to harbor life.",
                    id=1 
    )

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 5
    assert result["id"] == 1
    assert result["name"] == "Earth"
    assert result["description"] == "Earth is the third planet from the Sun and the only astronomical object known to harbor life."
    assert result["distance_from_earth"] is None
