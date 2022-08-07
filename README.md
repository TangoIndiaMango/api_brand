
# Backend - Brand API

## Setting up the Backend

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/BrandApi` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Django](http://flask.pocoo.org/) is a backend framework. Django is required to handle requests and responses.

- [cloudinary_storage](https://cloudinary.com/) is the storage to store user uploads. 

- 

### Using Django default Database


- Add to settings.py
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

```

Populate the database using the `python manage.py makemigrations`

```bash
- python manage.py makemigrations
- python manage.py migrate
```

### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
python manage.py runserver
```

## To Do Tasks

These are the files:

1. `django_brand/customer/`
2. `django_brand/django_brand/ --contains the default setup provided by django`
2. `django_brand/gateway/`
2. `django_brand/user/`

One note before you delve into each endpoint, 

### Endpoints


- Add to settings.py
```bash
URLS = {
    path('admin/', admin.site.urls),
    path('gateway/', include("gateway.urls")),
    path("user-main/",include("user.urls")),
    path("", include("customer.urls")),
}
```

## Documenting Endpoints

Here is a detailed documentation of the API endpoints including the URL, request parameters, and the response body. Use the example below as a reference.

### Documentation Example

`POST '/gateway/login'`

- Login a user
- Request Arguments: POST
- Returns: A refresh token which can be verified on jwt.io.

```json
{
  "succes": true,
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTk3MTI1ODUsInVzZXIiOjJ9.OQtEB3hltEmIa2c5tZkfld583gJbV833hZFkXWyckhI",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2OTEyNDgyODUsImRhdGEiOiJGUUdXNkk5RVI1In0.Ww60EADUoe-IS8RNG-HxUTadlIJHRgo4rv1BkfNOUt8",
}
```
`POST '/gateway/register'`

- Register a user
- Request Arguments: POST
- Returns: The user

```json
{
  "success": "user created",
}


```
`GET '/customer'`

- Fetches a dictionary of customer message in which the keys are the ids and the value is the corresponding string
- Request Arguments: None
- Returns: An object with a key and value.

```json
{
  "id": "1",
  "name": "Art",
  "email": "admin@admin.com",
  "message": "I  have some openings for a new brand i'll love to introduce you to",
}
```

`POST '/customer'`

- Add a dictionary of customer message into the database
- Request Arguments: POST
- Returns: An object with a key and value.

```json
{
  "id": "1",
  "name": "Throw",
  "email": "admin@admin.com",
  "message": "I  have some openings for a new brand i'll love to introduce you to",
}
```

`POST '/gateway/refresh'`

- Get refresh token
- Request Arguments: POST
- Returns: A new refresh and access token

```json
{
  "succes": true,
  "access": "Art",
  "refresh": "admin@admin.com",
  "message": "I  have some openings for a new brand i'll love to introduce you to",
}
```

`GET '/user-main/uploads'`
- To post on Postman, use form-data
- Fetches a dictionary of currrent user logged in with uploads
- Request Arguments: None
- Returns: An object with a key and value.

```json
{
  "id": "1",
  "user": "admin@admin.com",
  "title": "A new Canon",
  "image": "canon_ilos.jpg",
  "Date": "2022-08-05",
}
```
`POST '/user-main/uploads'`

- Post a dictionary of files to be uploaded with current user
- protected endpoint
- Request Arguments: POST
- Returns: An object with a key and value.

```json
{
  "success" : true
}
```

## Testing

Pass

