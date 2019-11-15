# API Documentation

## Authentication

---

**URL** : `http://localhost:8000/api/token/`

**Method** : `POST`

**Authentication Pequired** : No

**Request Parameters**

```json
{
    "username": {
        "type": "field",
        "required": true,
        "read_only": false,
        "label": "Username"
    },
    "password": {
        "type": "field",
        "required": true,
        "read_only": false,
        "label": "Password"
    }
}
```

**Example Request** :

```shell
$ curl -X POST "http://localhost:8000/api/token/" -H "accept: application/json" -d '{"username":"teacher","password":"password123"}'
```

**Example Response** :

```json
HTTP 200 OK

{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4"
}
```

---

**URL** : `http://localhost:8000/api/token/refresh/`

**Method** : `POST`

**Authentication Pequired** : No

**Request Parameters**

```json
{
    "refresh": {
        "type": "field",
        "required": true,
        "read_only": false,
        "label": "Refresh Token"
    }
}
```

**Example Request** :

```shell
$ curl -X POST "http://localhost:8000/api/token/refresh/" -H "accept: application/json" -d '{ "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4" }'
```

**Example Response** :

```json
HTTP 200 OK

{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNTY3LCJqdGkiOiJjNzE4ZTVkNjgzZWQ0NTQyYTU0NWJkM2VmMGI0ZGQ0ZSJ9.ekxRxgb9OKmHkfy-zs1Ro_xs1eMLXiR17dIDBVxeT-w"
}
```

---

## Resources

- **Subjects** : `http://localhost:8000/api/subjects/`    ***[view details](api/subjects.md)***.
- **Courses** : `http://localhost:8000/api/courses/`    ***[view details](api/courses.md)***.
- **Lessons** : `http://localhost:8000/api/lessons/`    ***[view details](api/lessons.md)***.
- **Questions** : `http://localhost:8000/api/questions/`    ***[view details](api/questions.md)***.
- **Answers** : `http://localhost:8000/api/answers/`    ***[view details](api/answers.md)***.