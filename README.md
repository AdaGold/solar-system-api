# Solar System API

## Goal

Our coding skills improve with repetition.

Our goal is to practice creating a minimal Flask API in a pair or group setting.

Pairing with other programmers will help create stronger understanding of the material, and improved skill at working with others. Software teams thrive on collaboration, so working side-by-side with someone while coding is vital!

In this activity, we will build a Solar System API. This API will store information about different planets.

We will focus on creating RESTful endpoints for CRUD operations.

## Tips

- Don't forget to work in a virtual environment
- Put endpoints in `app/routes.py`
- Add configuration, such as registering blueprints or configuring databases, in `app/__init__.py`
- Commit and push often

## Github Setup

1. Choose one member to fork the Solar System API repo 
1. Add all members to the forked repo as collaborators (through the repo settings)
1. All group members should clone this new, forked, group repo and `cd` into it
1. Discuss good git hygiene: 
    * Make regular commits
    * Push commits before switching driver
    * Pull before starting to drive

## Guidelines for Pair-Programming

- The driver is the person who is at the keyboard and mouse
- The navigator is the person who is thinking out loud, actively collaborating with the driver about the next step, and helping guide the development
- Trade-off driver and navigator roles often, at least daily
- Take time to make sure you're on the same page

## Project Directions

### Part 1
1. [Wave 1: Read Endpoints](#wave-01-read-endpoints)


### Part 2
2. [Wave 2: Connecting the Database, Read and Create Endpoints](#wave-02-connecting-the-database-read-and-create-endpoints)
3. [Wave 3: Update and Delete](#wave-03-update-and-delete)
4. [Wave 4: Handling 404s](#wave-04-handling-404s)
5. [Wave 5: Writing Tests](#wave-05-writing-tests)

## Wave 01: Read Endpoints

### Database Setup
For each wave in Part 2, the new driver may need to setup their database. Follow these steps:

1. Pull down all new git commits
1. Activate the virtual environment
1. Create the database `solar_system_development`
1. Run `flask db upgrade`
1. Run `flask run` to confirm that the API is running as expected

### RESTful Endpoints: Read
Create the following endpoints, with similar functionality presented in the Hello Books API:

As a client, I want to send a request...

1. ...to get all existing `planets`, so that I can see a list of `planets`, with their `id`, `name`, `description`, and other data of the `planet`.
1. ...to get one existing `planet`, so that I can see the `id`, `name`, `description`, and other data of the `planet`.

## Wave 02: Connecting the Database, Read and Create Endpoints

### Database Setup

Complete the following setup steps of the Solar System API repo:
1. Activate the virtual environment
1. Create the database `solar_system_development`
    * *Every member of the group must create the database on their computer*
1. Setup the `Planet` model with the attributes `id`, `name`, and `description`, and one additional attribute
1. Create a migration to add a table for the `Planet` model and then apply it. 
    * *Confirm that the `planet` table has been created as expected in postgres*.

### RESTful Endpoints: Create and Read
Create or refactor the following endpoints, with similar functionality presented in the Hello Books API:

As a client, I want to send a request...

1. ...with new valid `planet` data and get a success response, so that I know the API saved the planet data
1. ...to get all existing `planets`, so that I can see a list of planets, with their `id`, `name`, `description`, and other data of the `planet`.
1. ...to get one existing `planet`, so that I can see the `id`, `name`, `description`, and other data of the `planet`.

## Wave 03: Update and Delete

### RESTful Endpoints: Update and Delete
Create the following endpoints, with similar functionality presented in the Hello Books API:

As a client, I want to send a request...

1. ... with valid planet data to update one existing`planet` and get a success response, so that I know the API updated the `planet` data.
1. ... to delete one existing `planet` and get a success response, so that I know the API deleted the `planet` data..

## Wave 04: Handling 404s

### RESTful Endpoints: Update and Delete
Create the following endpoints, with similar functionality presented in the Hello Books API:

As a client, I want to send a request...

1. ... trying to get one non-existing `planet` and get a 404 response, so that I know the `planet` resource was not found.
1. ... trying to update one non-existing `planet` and get a 404 response, so that I know the `planet` resource was not found.
1. ... trying to delete one non-existing `planet` and get a 404 response, so that I know the `planet` resource was not found.

## Wave 05: Writing Tests

### Setup
Complete the following requirements, with similar functionality to the Hello Books API:

1. Create a `.env` file.
1. Populate it with two environment variables: `SQLALCHEMY_DATABASE_URI` and `SQLALCHEMY_TEST_DATABASE_URI`. Set their values to the appropriate connection strings.
1. Create a test database with the correct, matching name.
1. Refactor the `create_app` method to:
   * Check for a configuration flag
   * Read the correct database location from the appropriate environment variables
1. Manually test that our development environment still works.
1. Create a `tests` folder with the files `tests/__init__.py`, `tests/conftest.py`, and `tests/test_routes.py`.
1. Populate `tests/conftest.py` with the recommended configuration.
1. Create a test to check `GET` `/planets` returns `200` and an empty array.
1. Confirm this test runs and passes.

### Writing Tests
Create test fixtures and unit tests for the following test cases:

1. `GET` `/planets/1` returns a response body that matches our fixture
1. `GET` `/planets/1` with no data in test database (no fixture) returns a `404`
1. `GET` `/planets` with valid test data (fixtures) returns a `200` with an array including appropriate test data
1. `POST` `/planets` with a JSON request body returns a `201`