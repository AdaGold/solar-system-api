# Wave 02: Connecting the Database, Read and Create Endpoints

## Database Setup

Complete the following setup steps of the Solar System API repo:
1. Activate the virtual environment
1. Create the database `solar_system_development`
    * *Every member of the group must create the database on their computer*
1. Setup the `Planet` model with the attributes `id`, `name`, and `description`, and one additional attribute
1. Create a migration to add a table for the `Planet` model and then apply it. 
    * *Confirm that the `planet` table has been created as expected in postgres*.

## RESTful Endpoints: Create and Read

Create or refactor the following endpoints, with similar functionality presented in the Hello Books API:

As a client, I want to send a request...

1. ...with new valid `planet` data and get a success response, so that I know the API saved the planet data
1. ...to get all existing `planets`, so that I can see a list of planets, with their `id`, `name`, `description`, and other data of the `planet`.
1. ...to get one existing `planet`, so that I can see the `id`, `name`, `description`, and other data of the `planet`.