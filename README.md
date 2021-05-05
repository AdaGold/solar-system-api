Here we will list every endpoint for this API.

Every endpoint must serve JSON data, and must use HTTP response codes to indicate the status of the request.

## Error Handling Requirements for Every Endpoint

It's crucial for all APIs to be able to handle errors. For every required endpoint described in this project, handle errors in this pattern.

If something goes wrong, your API should return:
- an appropriate [HTTP status code](http://billpatrianakos.me/blog/2013/10/13/list-of-rails-status-code-symbols/)
- a list of errors

For this project, the list of errors should be formatted like this:

```json
{
  "errors": {
    "available_inventory": [
      "can't be blank",
      "is not a number"
    ]
  }
}

// ...or...

{
    "errors": [
        "Not Found"
    ]
}

```

All errors your API can return should be covered by at least one controller test case.

# Wave 1: Customers and Videos

## `/customers` CRUD

Required endpoints:

1. GET `/customers`
1. GET `/customers/<id>`
1. POST `/customers`
1. PUT `/customers/<id>`
1. DELETE `/customers/<id>`

## `GET` `/customers` Details

Lists all existing customers and details about each customer.

#### Required Arguments

No arguments to this request

#### Response

Typical success response:

Status: `200`

```json
[
  {
    "id": 1,
    "name": "Shelley Rocha",
    "registered_at": "Wed, 29 Apr 2015 07:54:14 -0700",
    "postal_code": "24309",
    "phone": "(322) 510-8695",
    "videos_checked_out_count": 0
  },
  {
    "id": 2,
    "name": "Curran Stout",
    "registered_at": "Wed, 16 Apr 2014 21:40:20 -0700",
    "postal_code": "94267",
    "phone": "(908) 949-6758",
    "videos_checked_out_count": 0
  }
]
```

#### Errors & Edge Cases to Check

- The API should return an empty array and a status `200` if there are no customers.

## `/videos` CRUD

Required endpoints:

1. GET `/videos`
1. GET `/vidoes/<id>`
1. POST `/videos`
1. PUT `/videos/<id>`
1. DELETE `/videos/<id>`

## `GET /videos` Details
Lists all existing videos and details about each video.

#### Required Arguments

No arguments to this request

#### Response

Typical success response (this are the minimum required fields that the Postman tests will be looking for):

Status: `200`

```json
[
  {
    "id": 1,
    "title": "Blacksmith Of The Banished",
    "release_date": "1979-01-18",
    "total_inventory": 10,
    "available_inventory": 9
  },
  {
    "id": 2,
    "title": "Savior Of The Curse",
    "release_date": "2010-11-05",
    "total_inventory": 11,
    "available_inventory": 1
  }
]
```

#### Errors & Edge Cases to Check

- The API should return an empty array and a status `200` if there are no videos.

### `GET /video/:id` Details
Gives back details about specific video in the store's inventory.

#### Required Arguments

Arg | Type | Details
--- | --- | ---
`id` | integer | The id of the video

#### Response

Typical success response:

Status: `200`

```json
{
  "id": 1,
  "title": "Blacksmith Of The Banished",
  "release_date": "1979-01-18",
  "total_inventory": 10,
  "available_inventory": 9
}
```

#### Errors & Edge Cases to Check

- The API should return back detailed errors and a status `404: Not Found` if this video does not exist.

### `POST /videos`
Creates a new video with the given params.

#### Required Request Body Parameters

Request Body Param | Type | Details
--- | --- | ---
`title` | string | The title of the video
`overview` | string | An overview of the video
`release_date` | string | Represents the date of the video's release
`total_inventory` | integer | The total quantity of this video in the store

#### Response

Typical success response, where `id` is the id of the new video:

Status: `201: Created`

```json
{
  "id": 277419104
}
```

#### Errors & Edge Cases to Check

- The API should return back detailed errors and a status `400: Bad Request` if the video does not have any of the required fields to be valid.

#### Hint: Params Not Nested

Are you having trouble creating a new video? Look at the structure of the request body for the request. In Rails, the Rails convention for passing in params often relied on a specific nested structure. For example, when we created a book in Ada Books, our book params data from our new book form came in nested, like `{book: {title: 'Alice in Wonderland'}}`. How are the API expectations different?

# **Optional** Wave 2: Making Rentals with Checking In and Checking Out

## `POST /rentals/check-out`

[Checks out](https://www.merriam-webster.com/dictionary/checkout) a video to a customer, and updates the data in the database as such.

When successful, this request should:
- increase the customer's `videos_checked_out_count` by one
- decrease the video's `available_inventory` by one
- create a due date. The rental's due date is the seven days from the current date.

#### Required Request Body Parameters

Request Body Param | Type | Details
--- | --- | ---
`customer_id` | integer | ID of the customer attempting to check out this video
`video_id` | integer | ID of the video to be checked out

#### Response

Typical success response:

Status: `200`

```json
{
  "customer_id": 122581016,
  "video_id": 235040983,
  "due_date": "2020-06-31",
  "videos_checked_out_count": 2,
  "available_inventory": 5
}
```

#### Errors & Edge Cases to Check

- The API should return back detailed errors and a status `404: Not Found` if the customer does not exist
- The API should return back detailed errors and a status `404: Not Found` if the video does not exist
- The API should return back detailed errors and a status `400: Bad Request` if the video does not have any available inventory before check out

## `POST /rentals/check-in`
[Checks in](https://www.merriam-webster.com/dictionary/check-in) a video to a customer, and updates the data in the database as such.

When successful, this request should:
- decrease the customer's `videos_checked_out_count` by one
- increase the video's `available_inventory` by one

#### Required Request Body Parameters

Request Body Param | Type | Details
--- | --- | ---
`customer_id` | integer | ID of the customer attempting to check out this video
`video_id` | integer | ID of the video to be checked out

#### Response

Typical success response:

Status: `200`

```json
{
  "customer_id": 122581016,
  "video_id": 277419103,
  "videos_checked_out_count": 1,
  "available_inventory": 6
}
```

#### Errors & Edge Cases to Check

- The API should return back detailed errors and a status `404: Not Found` if the customer does not exist
- The API should return back detailed errors and a status `404: Not Found` if the video does not exist

# More Optional Enhancements
These really are **optional** - if you've gotten here and you have time left, that means you're moving speedy fast!

### Query Parameters
Any endpoint that returns a list should accept 3 _optional_ [query parameters](http://guides.rubyonrails.org/action_controller_overview.html#parameters):

| Name   | Value   | Description
|--------|---------|------------
| `sort` | string  | Sort objects by this field, in ascending order
| `n`    | integer | Number of responses to return per page
| `p`    | integer | Page of responses to return

So, for an API endpoint like `GET /customers`, the following requests should be valid:
- `GET /customers`: All customers, sorted by ID
- `GET /customers?sort=name`: All customers, sorted by name
- `GET /customers?n=10&p=2`: Customers 11-20, sorted by ID
- `GET /customers?sort=name&n=10&p=2`: Customers 11-20, sorted by name

Of course, adding new features means you should be adding new controller tests to verify them.

Things to note:
- Sorting by ID is the rails default
- Possible sort fields:
  - Customers can be sorted by `name`, `registered_at` and `postal_code`
  - Videos can be sorted by `title` and `release_date`
  - Overdue rentals can be sorted by `title`, `name`, `checkout_date` and `due_date`
- If the client requests both sorting and pagination, pagination should be relative to the sorted order
- Check out the [will_paginate gem](https://github.com/mislav/will_paginate)

### More Endpoints: Inventory Management
All these endpoints should support all 3 query parameters. All fields are sortable.

#### `GET /rentals/overdue`
List all customers with overdue videos

Fields to return:
- `video_id`
- `title`
- `customer_id`
- `name`
- `postal_code`
- `checkout_date`
- `due_date`

#### `GET /videos/:id/current`
List customers that have _currently_ checked out a copy of the video

URI parameters:
- `id`: Video identifier

Fields to return:
- `customer_id`
- `name`
- `postal_code`
- `checkout_date`
- `due_date`

#### `GET /videos/:id/history`
List customers that have checked out a copy of the video _in the past_

URI parameters:
- `id`: Video identifier

Fields to return:
- `customer_id`
- `name`
- `postal_code`
- `checkout_date`
- `due_date`

#### `GET /customers/:id/current`
List the videos a customer _currently_ has checked out

URI parameters:
- `id`: Customer ID

Fields to return:
- `title`
- `checkout_date`
- `due_date`

#### `GET /customers/:id/history`
List the videos a customer has checked out _in the past_

URI parameters:
- `id`: Customer ID

Fields to return:
- `title`
- `checkout_date`
- `due_date`
