# Wave 05: Writing Tests


## Setup

Complete the following requirements, with similar functionality to the Hello Books API:

1. Create a `.env` file.
1. Populate it with two environment variables: `SQLALCHEMY_DATABASE_URI` and `SQLALCHEMY_TEST_DATABASE_URI`. Set their values to the appropriate connection strings.
1. Create a test database with the correct, matching name.
1. Refactor the `create_app` method to:
   * Check for a configuration flag
   * Read the correct database location from the appropriate environment variables
1. Manually test that our development environment still works.
1. Create a `tests` folder with the files:
    -  `tests/__init__.py`
    -  `tests/conftest.py`
    -  `tests/test_routes.py`.
1. Populate `tests/conftest.py` with the recommended configuration.
1. Create a test to check `GET` `/planets` returns `200` and an empty array.
1. Confirm this test runs and passes.

## Writing Tests

Create test fixtures and unit tests for the following test cases:

1. `GET` `/planets/1` returns a response body that matches our fixture
1. `GET` `/planets/1` with no data in test database (no fixture) returns a `404`
1. `GET` `/planets` with valid test data (fixtures) returns a `200` with an array including appropriate test data
1. `POST` `/planets` with a JSON request body returns a `201`