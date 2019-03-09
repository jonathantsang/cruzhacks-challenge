# CruzHacks 2020 Backend Developer Code Challenge
## Bryan Ji, 03/05/2019

This is a simple CRUD app made for my application for CruzHacks 2020's development team.
Instructions for setup and usage are located in the docs folder.
Built in Flask for Python.

## Usage:

There are 4 endpoints, each of which corresponds to a CRUD (Create, Read, Update, Delete) operation.
You can start the server with the following command (assuming you setup already):
```python app.py```

By default, the app runs on port 8080, but this can be modified by changing app.py.

(By the way, it's far easier to send requests using the requests library for python, rather than CURL).

### GET /hackers/&lt; id &gt;

Corresponds to the R (read) in CRUD.

Example:

```
GET http://localhost:8080/ba2bc8f0-abbf-44b9-93ec-53cb9455aac4
```

Gets and returns the user's information with the corresponding id. If the user exists, data will be returned as a dictionary.
An example is as follows:

```
HTTP Status Code 200
{
    'result': 'Success',
    'msg': 'OK',
    'val':
        {
            'UserProfileId': 'ba2bc8f0-abbf-44b9-93ec-53cb9455aac4',
            'UserTypeCode': 'HCK',
            'Name': 'Jim Lahey',
            'School': 'UC Santa Cruz',
            'Major': 'Computer Science',
            'Street1': '123 Street St.',
            'Street2': 'Unit 123',
            'StateCode': 'CA',
            'ZipCode': 95064,
            'CountryCode': 'US',
            'Phone': '123-456-7890',
            'Email': 'coreytrevor@tpb.com',
            'BirthDate': 'Tue, 05 Mar 2019 00:00:00 GMT',
            'ProfileImageUrl': None
        }
}
```

If the user doesn't exist, the following will be returned:

```
HTTP Status Code 404
{
    'result': 'Error',
    'msg': 'Hacker does not exist'
}
```

### POST /hackers

Corresponds to the C (create) in CRUD.

Example:

```
POST http://localhost:8080/hackers -d UserTypeCode="ADM" -d Name="abc" ...
```

Creates a new UserProfile, aka makes a new user. Be careful about UserTypeCode; Note that I didn't add any safety checks, so anyone can give themselves 'ADM', or admin. 

Expects a payload with the following format:

```
{
    'UserTypeCode': 'ADM',
    'Name': 'Papa Lamport',
    'School': 'MIT',
    'Major': 'Mathematics',
    'Street1': '123 Street St.',
    'Street2': 'Unit 123',
    'StateCode': 'CA',
    'ZipCode': 95060,
    'CountryCode': 'US',
    'Phone': '123-456-7890',
    'Email': 'lamport@microsoft.com',
    'BirthDate': 'Tue, 05 Mar 2019 00:00:00 GMT',
    'ProfileImageUrl': None
}
```

A successful request will return

```
HTTP Status Code 201
{
    'result': 'Success',
    'msg': 'OK'
}
```

If one or more required fields is missing, it will return

```
HTTP Status Code 400
{
    'result': 'Error',
    'msg': 'One or more required fields is missing'
}
```

### PUT /hackers/&lt; id &gt;

Corresponds to the U (update) in CRUD.

```
PUT http://localhost:8080/hackers/ba2bc8f0-abbf-44b9-93ec-53cb9455aac4 -d UserTypeCode="ADM" -d Name="abc" ...
```

Updates a UserProfile. This returns OK even if the id didn't exist, so some checks will need to be added in the future. 

Takes in an id in the URL, and a payload of the following form:

```
{
    'UserTypeCode': 'JDG',
    'Name': 'Abed Nadir',
    'School': 'Greendale Community College',
    'Major': 'Film',
    'Street1': '123 Street St.',
    'Street2': 'Unit 123',
    'StateCode': 'CO',
    'ZipCode': 95060,
    'CountryCode': 'US',
    'Phone': '123-456-7890',
    'Email': 'anadir@greendale.edu',
    'BirthDate': 'Tue, 05 Mar 2019 00:00:00 GMT',
    'ProfileImageUrl': None
}
```

A successful request will return

```
HTTP Status Code 200
{
    'result': 'Success',
    'msg': 'OK'
}
```

If one or more required fields is missing, it will return

```
HTTP Status Code 400
{
    'result': 'Error',
    'msg': 'One or more required fields is missing'
}
```

### DELETE /hackers/&lt; id &gt;

Corresponds to the D (delete) in CRUD.

```
DELETE http://localhost:8080/hackers/ba2bc8f0-abbf-44b9-93ec-53cb9455aac4
```

Deletes a UserProfile given an id. Note that even if you pass in an invalid ID, this will return OK. Because you should only be allowing users to access this API through buttons, you crazy frontend dev.

A successful request will return

```
HTTP Status Code 200
{
    'result': 'Success',
    'msg': 'OK'
}
```