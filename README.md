# lexthink/dacodes-backend-test

## Requirements

* **Python** >= 3.5
* **Django** >= 2.2.x
* **django-dotenv** >= 1.4.x
* **django-positions** >= 0.6.x
* **djangorestframework** >= 3.10.x
* **djangorestframework-simplejwt** >= 4.3.x
* **drf-writable-nested** >= 0.5.x

## Installation

Install it by `git clone https://github.com/lexthink/dacodes-backend-test` or download zip file.

```shell
$ git clone https://github.com/lexthink/dacodes-backend-test
$ cd dacodes-backend-test
$ virtualenv venv && source venv/bin/activate # optional
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py loaddata fixtures # load fake data (default users, courses, lessons, etc.)
$ python manage.py runserver
```
The development web-server is running by default in http://localhost:8000.

> NOTE: This project includes 'django-dotenv', so you can just rename the .env.example to .env and override any variable if necessary

> NOTE: add rest_framework.renderers.BrowsableAPIRenderer to REST_FRAMEWORK.DEFAULT_RENDERER_CLASSES in config/settings.py file, to use the browsable api provided by djangorestframework

## Basic usage

You can easily test if the endpoint is working by doing the following in your terminal. (Default users with the usernames **teacher** and **student** both with password **password123**)

```shell
$ curl -X POST http://localhost:8000/api/token/ -d "username=teacher&password=password123"
```

Alternatively, you can use all the content types supported by the Django REST framework to obtain the auth token. For example:

```shell
$ curl -X POST http://localhost:8000/api/token/ -H "Content-Type: application/json" -d '{ "username": "teacher", "password": "password123" }'
```

Now in order to access protected api urls you must include the `Authorization: Bearer <your_token>` header.

```shell
$ curl http://localhost:8000/protected-url/ -H "Authorization: Bearer <your_token>"
```

When this short-lived access token expires, you can use the longer-lived refresh token to obtain another access token:

```shell
$ curl -X POST "http://localhost:8000/api/token/refresh/" -H "accept: application/json" -d '{ "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4" }'
```

## Documentation

Detailed documentation of all features can be found [here](docs/index.md).

## License

This project is licensed under [MIT license](http://opensource.org/licenses/MIT). Please see [LICENSE](LICENSE) for more information.
