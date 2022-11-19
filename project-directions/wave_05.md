# Wave 05: Review, Refactor, Query Params

## Query Params

### Sorting Planets by Name Ascending
As a client, I want to be able to make a `GET` request to `/planets?sort=asc` when there is more than one saved planet and get an array of planets sorted by name. The names should be in _ascending order_, where a planet with name "A" is sorted before a planet with name "B".

I want to get this response:
`200 OK`

```json
[
    {
        "id": 1,
        "name": "Earth",
        "description": "home"
    },
    {
        "id": 2,
        "name": "Mercury",
        "description": "smallest planet"
    }
]
```

### Sorting Planets by Name Descending
As a client, I want to be able to make a `GET` request to `/planets?sort=desc` when there is more than one saved planet and get an array of planets sorted by name. The names should be in _descending order_, where a planet with name "B" is sorted before a planet with name "A".

I want to get this response:
`200 OK`

```json
[
    {
        "id": 2,
        "name": "Mercury",
        "description": "smallest planet"
    } ,
    {
        "id": 1,
        "name": "Earth",
        "description": "home"
    }
]
```

### Filtering Planets by Name
As a client, I want to be able to make a `GET` request to `/planets?name=myPlanet` and get an array of all planets with the name `myPlanet`. If there are no planets with the given name, I should receive an empty array. 

I want to get this response:
`200 OK`

```json
[
    {
        "id": 1,
        "name": "Earth",
        "description": "home"
    }
]
```
### Multiple Query Params
I should still receive a `200 OK` response when I make a request to both filter by name and sort in either ascending or descending order. For example, `/planets?sort=asc&name=Earth` should return a `200 OK` response. 

## Review and Refactor
Review the requirements for Wave 01 - 04
* Test the endpoints using postman
* Complete or fix any incomplete or broken endpoints
* Look for opportunities to refactor
