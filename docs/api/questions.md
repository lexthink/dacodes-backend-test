# Resource: questions

## Questions

---

**URL** : `http://localhost:8000/api/questions/`

**Method** : `GET`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X GET "http://localhost:8000/api/questions/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 200 OK

[
    {
        "id": 1,
        "lesson": 1,
        "content": "True or False? In Python 3, the maximum value for an integer is 2^63 - 1?",
        "explanation": "In Python 2, there was an internal limit to how large an integer value could be. But that limit was removed in Python 3.\r\n\r\nThis means there is no explicitly defined limit, but the amount of available address space forms a practical limit depending on the machine Python runs on.",
        "answer_order": null,
        "score": 1,
        "answers": [...]
    },
    {
        "id": 2,
        "lesson": 1,
        "content": "How would you express the hexadecimal value a5 as a base-16 integer constant in Python?",
        "explanation": "",
        "answer_order": null,
        "score": 1,
        "answers": [...]
    },
    ...
]
```

---

**URL** : `http://localhost:8000/api/questions/`

**Method** : `POST`

**Authentication Pequired** : Yes

**Request Parameters**

```json
{
    "lesson": {
        "type": "field",
        "required": true,
        "read_only": false,
        "label": "Lesson"
    },
    "content": {
        "type": "string",
        "required": true,
        "read_only": false,
        "label": "Question",
        "help_text": "Enter the question text that you want displayed",
        "max_length": 1000
    },
    "explanation": {
        "type": "string",
        "required": false,
        "read_only": false,
        "label": "Explanation",
        "help_text": "Explanation to be shown after the question has been answered.",
        "max_length": 2000
    },
    "answer_order": {
        "type": "choice",
        "required": false,
        "read_only": false,
        "label": "Answer Order",
        "help_text": "The order in which the posible answers are displayed to the user",
        "choices": [
            {
                "value": "content",
                "display_name": "Content"
            },
            {
                "value": "random",
                "display_name": "Random"
            },
            {
                "value": "none",
                "display_name": "None"
            }
        ]
    },
    "score": {
        "type": "integer",
        "required": false,
        "read_only": false,
        "label": "Score"
    }
}
```

**Example Request** :

```shell
$ curl -X POST "http://localhost:8000/api/questions/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "lesson": 1, "content": "True or False? In Python 3, the maximum value for an integer is 2^63 - 1?", ... }'
```

**Example Response** :

```json
HTTP 201 Created

{
    "id": 1,
    "lesson": 1,
    "content": "How would you express the hexadecimal value a5 as a base-16 integer constant in Python?",
    "explanation": "",
    "answer_order": null,
    "score": 1,
    "answers": []
}
```

---

**URL** : `http://localhost:8000/api/questions/{id}/`

**Method** : `GET`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X GET "http://localhost:8000/api/questions/1/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 200 OK

{
    "id": 1,
    "lesson": 1,
    "content": "True or False? In Python 3, the maximum value for an integer is 2^63 - 1?",
    "explanation": "In Python 2, there was an internal limit to how large an integer value could be. But that limit was removed in Python 3.\r\n\r\nThis means there is no explicitly defined limit, but the amount of available address space forms a practical limit depending on the machine Python runs on.",
    "answer_order": null,
    "score": 1,
    "answers": [...]
}
```

---

**URL** : `http://localhost:8000/api/questions/{id}/`

**Method** : `PUT`

**Authentication Pequired** : Yes

**Request Parameters** :

```json
{
    "lesson": {
        "type": "field",
        "required": true,
        "read_only": false,
        "label": "Lesson"
    },
    "content": {
        "type": "string",
        "required": true,
        "read_only": false,
        "label": "Question",
        "help_text": "Enter the question text that you want displayed",
        "max_length": 1000
    },
    "explanation": {
        "type": "string",
        "required": false,
        "read_only": false,
        "label": "Explanation",
        "help_text": "Explanation to be shown after the question has been answered.",
        "max_length": 2000
    },
    "answer_order": {
        "type": "choice",
        "required": false,
        "read_only": false,
        "label": "Answer Order",
        "help_text": "The order in which the posible answers are displayed to the user",
        "choices": [
            {
                "value": "content",
                "display_name": "Content"
            },
            {
                "value": "random",
                "display_name": "Random"
            },
            {
                "value": "none",
                "display_name": "None"
            }
        ]
    },
    "score": {
        "type": "integer",
        "required": false,
        "read_only": false,
        "label": "Score"
    }
}
```

**Example Request** :

```shell
$ curl -X PUT "http://localhost:8000/api/questions/1/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "lesson": 1, "content": "True or False? In Python 3, the maximum value for an integer is 2^63 - 1?", ... }'
```

**Example Response** :

```json
HTTP 200 OK

{
    "id": 1,
    "lesson": 1,
    "content": "True or False? In Python 3, the maximum value for an integer is 2^63 - 1?",
    "explanation": "In Python 2, there was an internal limit to how large an integer value could be. But that limit was removed in Python 3.\r\n\r\nThis means there is no explicitly defined limit, but the amount of available address space forms a practical limit depending on the machine Python runs on.",
    "answer_order": null,
    "score": 1,
    "answers": [...]
}
```

---

**URL** : `http://localhost:8000/api/questions/{id}/`

**Method** : `PATCH`

**Authentication Pequired** : Yes

**Request Parameters** :

```json
{
    "lesson": {
        "type": "field",
        "required": true,
        "read_only": false,
        "label": "Lesson"
    },
    "content": {
        "type": "string",
        "required": true,
        "read_only": false,
        "label": "Question",
        "help_text": "Enter the question text that you want displayed",
        "max_length": 1000
    },
    "explanation": {
        "type": "string",
        "required": false,
        "read_only": false,
        "label": "Explanation",
        "help_text": "Explanation to be shown after the question has been answered.",
        "max_length": 2000
    },
    "answer_order": {
        "type": "choice",
        "required": false,
        "read_only": false,
        "label": "Answer Order",
        "help_text": "The order in which the posible answers are displayed to the user",
        "choices": [
            {
                "value": "content",
                "display_name": "Content"
            },
            {
                "value": "random",
                "display_name": "Random"
            },
            {
                "value": "none",
                "display_name": "None"
            }
        ]
    },
    "score": {
        "type": "integer",
        "required": false,
        "read_only": false,
        "label": "Score"
    }
}
```

**Example Request** :

```shell
$ curl -X PATCH "http://localhost:8000/api/questions/1/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "lesson": 1, "content": "True or False? In Python 3, the maximum value for an integer is 2^63 - 1?", ... }'
```

**Example Response** :

```json
HTTP 200 OK

{
    "id": 1,
    "lesson": 1,
    "content": "True or False? In Python 3, the maximum value for an integer is 2^63 - 1?",
    "explanation": "In Python 2, there was an internal limit to how large an integer value could be. But that limit was removed in Python 3.\r\n\r\nThis means there is no explicitly defined limit, but the amount of available address space forms a practical limit depending on the machine Python runs on.",
    "answer_order": null,
    "score": 1,
    "answers": [...]
}
```

---

**URL** : `http://localhost:8000/api/questions/{id}/`

**Method** : `DELETE`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X DELETE "http://localhost:8000/api/questions/1/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 204 No Content
```

---