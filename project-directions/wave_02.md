# Wave 02: Read One Book and 404s

## RESTful Endpoint(s): Read One Planet
Create the following endpoint(s), with similar functionality presented in the Hello Books API:

As a client, I want to send a request...

1. ...to get one existing `planet`, so that I can see the `id`, `name`, `description`, and other data of the `planet`.
1. ... such that trying to get one non-existing `planet` responds with get a `404` response, so that I know the `planet` resource was not found.
1. ... such that trying to get one `planet` with an invalid `planet_id` responds with get a `400` response, so that I know the `planet_id` was invalid.
    
