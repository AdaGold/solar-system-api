# Wave 05: Review and Refactor

## Update Endpoints

Update the read all planets endpoint with similar functionality presented in the Hello Books API:

As a client, I want to send a request...

1. ... to get a list of `planet`s, restricted to those with a match in the `description`, so that I can find a planet by a partial description.
2. ... to get a list of `planet`s, restricted to those with some kind of match to your additional attribute (e.g. larger/smaller than some size, partial match of a fun fact, etc), so that I can find planets with similar properties.

I should be able to combine the effects of the two filters in order to filter results by multiple properties at once.

If time allows, consider adding a non-filter query parameter, such as sorting by a specific attribute. Remember that sorting can be done by the database, so try not to sort the results in your application code.