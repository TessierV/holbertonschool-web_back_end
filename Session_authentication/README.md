![image](https://github.com/TessierV/holbertonschool-web_back_end/assets/113889290/fd51e097-74ed-46fb-b32c-f2b7abff3d48)

# Simple API

Simple HTTP API for playing with `User` model.


## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


## Setup

```
$ pip3 install -r requirements.txt
```


## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)

## Tasks

0. Et moi et moi et moi!
1. Empty session
2. Create a session
3. User ID for Session ID
4. Session cookie
5. Before request
6. Use Session ID for identifying a User
7. New view for Session Authentication
8. Logout
   
<br>
<br/><hr>
<p align="right">Holberton TOULOUSE</p>
