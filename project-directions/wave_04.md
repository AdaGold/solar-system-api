# Wave 04: Read, Update, Delete

## RESTful Endpoints: Read, Update, and Delete

Create the following endpoints, with similar functionality presented in the Hello Books API:

As a client, I want to send a request...

1. ...to get one existing `planet`, so that I can see the `id`, `name`, `description`, and other data of the `planet`.
1. ... with valid planet data to update one existing `planet` and get a success response, so that I know the API updated the `planet` data.
1. ... to delete one existing `planet` and get a success response, so that I know the API deleted the `planet` data..
    * Each of the above endpoints should respond with a `404` for non-existing planets and a `400` for invalid `planet_id`.