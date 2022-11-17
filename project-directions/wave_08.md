# Wave 08 - One-to-Many

## Moon Model

Define a `Moon` class with the attributes `id`, `name`, `planet_id` and `planet`. 

Modify the `Planet` class to add the attribute `moons`.

Make a Blueprint that groups the endpoints for the `Moon` model. Remember to register your blueprint in `create_app`. 

## RESTful endpoints: Read, Create for `Moon` model
Create the following endpoint(s), with similar functionality presented in the Hello Books API:

As a client, I want to send a request...
1. ...to get all existing `moons`, so that I can see a list of `moons`, with just their `name`s. 
2. ...to get one existing `moon` by `id`, so that I can see the `name` of Moon
3. ...with new valid `moon` data and get a success response, so that I know the API saved the moon data


## Nested routes: Read and Create routes connecting `Moon` to `Planet`
Create the following endpoint(s), with similar functionality presented in the Hello Books API:

As a client, I want to send a request...
1. ...with new valid `moon` data to create a new `moon` and connect it with a `planet` already found in the database
2. ... to get all `moons` by a particular `planet` in the database