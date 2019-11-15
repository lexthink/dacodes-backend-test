# Resource: answers

## Answers

---

**URL** : `http://localhost:8000/api/answers/`

**Method** : `GET`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X GET "http://localhost:8000/api/answers/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 200 OK

[
    {
        "id": 1,
        "question": 1,
        "content": "True",
        "correct": false
    },
    {
        "id": 2,
        "question": 1,
        "content": "False",
        "correct": true
    },
    ...
]
```

---

**URL** : `http://localhost:8000/api/answers/`

**Method** : `POST`

**Authentication Pequired** : Yes

**Request Parameters**

```json
{
    "question": {
        "type": "field",
        "required": true,
        "read_only": false,
        "label": "Question"
    },
    "content": {
        "type": "string",
        "required": true,
        "read_only": false,
        "label": "Content",
        "help_text": "Enter the answer text that you want displayed",
        "max_length": 1000
    },
    "correct": {
        "type": "boolean",
        "required": false,
        "read_only": false,
        "label": "Correct",
        "help_text": "Is this a correct answer?"
    }
}
```

**Example Request** :

```shell
$ curl -X POST "http://localhost:8000/api/answers/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "question": 1, "content": "True", "correct": false }'
```

**Example Response** :

```json
HTTP 201 Created

{
    "id": 1,
    "question": 1,
    "content": "True",
    "correct": false
}
```

---

**URL** : `http://localhost:8000/api/answers/{id}/`

**Method** : `GET`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X GET "http://localhost:8000/api/answers/1/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 200 OK

{
    "id": 1,
    "question": 1,
    "content": "True",
    "correct": false
}
```

---

**URL** : `http://localhost:8000/api/answers/{id}/`

**Method** : `PUT`

**Authentication Pequired** : Yes

**Request Parameters** :

```json
{
    "question": {
        "type": "field",
        "required": true,
        "read_only": false,
        "label": "Question"
    },
    "content": {
        "type": "string",
        "required": true,
        "read_only": false,
        "label": "Content",
        "help_text": "Enter the answer text that you want displayed",
        "max_length": 1000
    },
    "correct": {
        "type": "boolean",
        "required": false,
        "read_only": false,
        "label": "Correct",
        "help_text": "Is this a correct answer?"
    }
}
```

**Example Request** :

```shell
$ curl -X PUT "http://localhost:8000/api/answers/1/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "question": 1, "content": "True", "correct": false }'
```

**Example Response** :

```json
HTTP 200 OK

{
    "id": 1,
    "question": 1,
    "content": "True",
    "correct": false
}
```

---

**URL** : `http://localhost:8000/api/answers/{id}/`

**Method** : `PATCH`

**Authentication Pequired** : Yes

**Request Parameters** :

```json
{
    "question": {
        "type": "field",
        "required": true,
        "read_only": false,
        "label": "Question"
    },
    "content": {
        "type": "string",
        "required": true,
        "read_only": false,
        "label": "Content",
        "help_text": "Enter the answer text that you want displayed",
        "max_length": 1000
    },
    "correct": {
        "type": "boolean",
        "required": false,
        "read_only": false,
        "label": "Correct",
        "help_text": "Is this a correct answer?"
    }
}
```

**Example Request** :

```shell
$ curl -X PATCH "http://localhost:8000/api/answers/1/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "question": 1, "content": "True", "correct": false }'
```

**Example Response** :

```json
HTTP 200 OK

{
    "id": 1,
    "question": 1,
    "content": "True",
    "correct": false
}
```

---

**URL** : `http://localhost:8000/api/answers/{id}/`

**Method** : `DELETE`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X DELETE "http://localhost:8000/api/answers/1/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 204 No Content
```

---