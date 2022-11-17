# Wave 07 - Refactoring

## Refactoring with `to_dict`

Refactor the `read_all_planets` and `read_one_planet` functions to use a single helper function `to_dict` to create their responses.

`to_dict` is a method of the `Planet` class that converts an instance of the `Planet` model into a dictionary. `to_dict` should return the resulting dictionary. 

Before refactoring:
- identify any dependencies on the code we are refactoring.
- review existing test cases for each dependency in `tests/test_routes.py` and expand tests written in Wave 06 as needed to ensure we have a robust test suite for each dependency
- create a `tests/test_models.py` file and write a strong test_suite for the `to_dict` function


## Refactoring with `from_dict`

Refactor the code for creating a `Planet` model in the `create_planet` route to use `from_dict`.

`from_dict` is a class method of the `Planet` class that converts a dictionary with keys `name` and `description` into an instance of the `Planet` model. `from_dict` should return the resulting instance. 

Before refactoring:
- identify any dependencies on the code we are refactoring.
- review existing test cases for each dependency in `tests/test_routes.py` and expand tests written in Wave 06 as needed to ensure we have a robust test suite for each dependency
- Write a strong test_suite for the `from_dict` function in `tests/test_models.py`
  
## Refactoring `validate_planet`

Refactor the `validate_planet` function into a `validate_model` function that can be used on any class. 

Before refactoring:
- identify any dependencies on the code we are refactoring.
- review existing test cases for each dependency in `tests/test_routes.py` and expand tests written in Wave 06 as needed to ensure we have a robust test suite for each dependency