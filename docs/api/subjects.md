# Resource: subjects

## Subjects

---

**URL** : `http://localhost:8000/api/subjects/`

**Method** : `GET`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X GET "http://localhost:8000/api/subjects/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 200 OK

[
    {
        "id": 1,
        "title": "Python 3 Programming Specialization"
    },
    ...
]
```

---

**URL** : `http://localhost:8000/api/subjects/`

**Method** : `POST`

**Authentication Pequired** : Yes

**Request Parameters**

```json
{
    "title": {
        "type": "string",
        "required": true,
        "read_only": false,
        "label": "Title",
        "max_length": 100
    }
}
```

**Example Request** :

```shell
$ curl -X POST "http://localhost:8000/api/subjects/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "title": "Python 3 Programming Specialization" }'
```

**Example Response** :

```json
HTTP 201 Created

{
    "id": 1,
    "title": "Python 3 Programming Specialization"
}
```

---

**URL** : `http://localhost:8000/api/subjects/{id}/`

**Method** : `GET`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X GET "http://localhost:8000/api/subjects/1/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 200 OK

{
    "id": 1,
    "title": "Python 3 Programming Specialization"
}
```

---

**URL** : `http://localhost:8000/api/subjects/{id}/`

**Method** : `PUT`

**Authentication Pequired** : Yes

**Request Parameters** :

```json
{
    "title": {
        "type": "string",
        "required": true,
        "read_only": false,
        "label": "Title",
        "max_length": 100
    }
}
```

**Example Request** :

```shell
$ curl -X PUT "http://localhost:8000/api/subjects/1/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "title": "Python 3 Programming Specialization" }'
```

**Example Response** :

```json
HTTP 200 OK

{
    "id": 1,
    "title": "Python 3 Programming Specialization"
}
```

---

**URL** : `http://localhost:8000/api/subjects/{id}/`

**Method** : `PATCH`

**Authentication Pequired** : Yes

**Request Parameters** :

```json
{
    "title": {
        "type": "string",
        "required": true,
        "read_only": false,
        "label": "Title",
        "max_length": 100
    }
}
```

**Example Request** :

```shell
$ curl -X PATCH "http://localhost:8000/api/subjects/1/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "title": "Python 3 Programming Specialization" }'
```

**Example Response** :

```json
HTTP 200 OK

{
    "id": 1,
    "title": "Python 3 Programming Specialization"
}
```

---

**URL** : `http://localhost:8000/api/subjects/{id}/`

**Method** : `DELETE`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X DELETE "http://localhost:8000/api/subjects/1/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 204 No Content
```

---

## Resources

- **Courses** : `http://localhost:8000/api/courses/`    ***[view details](courses.md)***.
- **Lessons** : `http://localhost:8000/api/lessons/`    ***[view details](lessons.md)***.
- **Questions** : `http://localhost:8000/api/questions/`    ***[view details](questions.md)***.
- **Answers** : `http://localhost:8000/api/answers/`    ***[view details](answers.md)***.