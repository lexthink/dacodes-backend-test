# Resource: lessons

## Lessons

---

**URL** : `http://localhost:8000/api/lessons/`

**Method** : `GET`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X GET "http://localhost:8000/api/lessons/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 200 OK

[
    {
        "id": 1,
        "course": 1,
        "order": 0,
        "title": "General Introduction",
        "description": "In week one you will be introduced to programming in python through lectures and the Runestone textbook - an interactive online textbook built for this course. By the end of the module, you will have run your first python program, and learned how to draw images by writing a program.",
        "question_order": null,
        "pass_score": 3,
        "is_accessible": true
    },
    {
        "id": 20,
        "course": 6,
        "order": 0,
        "title": "Week One",
        "description": "This week we will uncover the \"mystery\" behind the Internet. What happens when you type a URL into your browser so that a webpage magically appears? What is HTML5 and what happened to HTML 1 - 4? We will also cover some practical concepts that you need to master before you begin coding your own pages.",
        "question_order": null,
        "pass_score": 4,
        "is_accessible": true
    },
    ...
]
```

---

**URL** : `http://localhost:8000/api/lessons/`

**Method** : `POST`

**Authentication Pequired** : Yes

**Request Parameters**

```json
{
    "course": {
        "type": "field",
        "required": true,
        "read_only": false,
        "label": "Course"
    },
    "order": {
        "type": "integer",
        "required": false,
        "read_only": false,
        "label": "Order"
    },
    "title": {
        "type": "string",
        "required": true,
        "read_only": false,
        "label": "Title",
        "max_length": 100
    },
    "description": {
        "type": "string",
        "required": false,
        "read_only": false,
        "label": "Description",
        "help_text": "a description of the lesson"
    },
    "question_order": {
        "type": "choice",
        "required": false,
        "read_only": false,
        "label": "Question Order",
        "help_text": "The order in which the questionsare displayed to the user",
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
    "pass_score": {
        "type": "integer",
        "required": false,
        "read_only": false,
        "label": "Pass score",
        "help_text": "Score required to pass lesson."
    }
}
```

**Example Request** :

```shell
$ curl -X POST "http://localhost:8000/api/lessons/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "course": 1, "order": 0, "title": "General Introduction", ... }'
```

**Example Response** :

```json
HTTP 201 Created

{
    "id": 1,
    "course": 1,
    "order": 0,
    "title": "General Introduction",
    "description": "In week one you will be introduced to programming in python through lectures and the Runestone textbook - an interactive online textbook built for this course. By the end of the module, you will have run your first python program, and learned how to draw images by writing a program.",
    "question_order": null,
    "pass_score": 3,
    "is_accessible": true
}
```

---

**URL** : `http://localhost:8000/api/lessons/{id}/`

**Method** : `GET`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X GET "http://localhost:8000/api/lessons/1/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 200 OK

{
    "id": 1,
    "course": 1,
    "order": 0,
    "title": "General Introduction",
    "description": "In week one you will be introduced to programming in python through lectures and the Runestone textbook - an interactive online textbook built for this course. By the end of the module, you will have run your first python program, and learned how to draw images by writing a program.",
    "question_order": null,
    "pass_score": 3,
    "is_accessible": true
}
```

---

**URL** : `http://localhost:8000/api/lessons/{id}/`

**Method** : `PUT`

**Authentication Pequired** : Yes

**Request Parameters** :

```json
{
    "course": {
        "type": "field",
        "required": true,
        "read_only": false,
        "label": "Course"
    },
    "order": {
        "type": "integer",
        "required": false,
        "read_only": false,
        "label": "Order"
    },
    "title": {
        "type": "string",
        "required": true,
        "read_only": false,
        "label": "Title",
        "max_length": 100
    },
    "description": {
        "type": "string",
        "required": false,
        "read_only": false,
        "label": "Description",
        "help_text": "a description of the lesson"
    },
    "question_order": {
        "type": "choice",
        "required": false,
        "read_only": false,
        "label": "Question Order",
        "help_text": "The order in which the questionsare displayed to the user",
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
    "pass_score": {
        "type": "integer",
        "required": false,
        "read_only": false,
        "label": "Pass score",
        "help_text": "Score required to pass lesson."
    }
}
```

**Example Request** :

```shell
$ curl -X PUT "http://localhost:8000/api/lessons/1/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "course": 1, "order": 0, "title": "General Introduction", ... }'
```

**Example Response** :

```json
HTTP 200 OK

{
    "id": 1,
    "course": 1,
    "order": 0,
    "title": "General Introduction",
    "description": "In week one you will be introduced to programming in python through lectures and the Runestone textbook - an interactive online textbook built for this course. By the end of the module, you will have run your first python program, and learned how to draw images by writing a program.",
    "question_order": null,
    "pass_score": 3,
    "is_accessible": true
}
```

---

**URL** : `http://localhost:8000/api/lessons/{id}/`

**Method** : `PATCH`

**Authentication Pequired** : Yes

**Request Parameters** :

```json
{
    "course": {
        "type": "field",
        "required": true,
        "read_only": false,
        "label": "Course"
    },
    "order": {
        "type": "integer",
        "required": false,
        "read_only": false,
        "label": "Order"
    },
    "title": {
        "type": "string",
        "required": true,
        "read_only": false,
        "label": "Title",
        "max_length": 100
    },
    "description": {
        "type": "string",
        "required": false,
        "read_only": false,
        "label": "Description",
        "help_text": "a description of the lesson"
    },
    "question_order": {
        "type": "choice",
        "required": false,
        "read_only": false,
        "label": "Question Order",
        "help_text": "The order in which the questionsare displayed to the user",
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
    "pass_score": {
        "type": "integer",
        "required": false,
        "read_only": false,
        "label": "Pass score",
        "help_text": "Score required to pass lesson."
    }
}
```

**Example Request** :

```shell
$ curl -X PATCH "http://localhost:8000/api/lessons/1/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "course": 1, "order": 0, "title": "General Introduction", ... }'
```

**Example Response** :

```json
HTTP 200 OK

{
    "id": 1,
    "course": 1,
    "order": 0,
    "title": "General Introduction",
    "description": "In week one you will be introduced to programming in python through lectures and the Runestone textbook - an interactive online textbook built for this course. By the end of the module, you will have run your first python program, and learned how to draw images by writing a program.",
    "question_order": null,
    "pass_score": 3,
    "is_accessible": true
}
```

---

**URL** : `http://localhost:8000/api/lessons/{id}/`

**Method** : `DELETE`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X DELETE "http://localhost:8000/api/lessons/1/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 204 No Content
```

---

**URL** : `http://localhost:8000/api/lessons/{id}/questions/`

**Method** : `GET`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X GET "http://localhost:8000/api/lessons/1/questions/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
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

**URL** : `http://localhost:8000/api/lessons/{id}/take/`

**Method** : `POST`

**Authentication Pequired** : Yes

**Request Parameters** :

```json
{
    "taken_questions": {
        "type": "field",
        "required": true,
        "read_only": false,
        "label": "Taken questions",
        "child": {
            "type": "nested object",
            "required": true,
            "read_only": false,
            "children": {
                "question": {
                    "type": "field",
                    "required": true,
                    "read_only": false,
                    "label": "Question"
                },
                "taken_answers": {
                    "type": "field",
                    "required": true,
                    "read_only": false,
                    "label": "Taken answers",
                    "child": {
                        "type": "nested object",
                        "required": true,
                        "read_only": false,
                        "children": {
                            "answer": {
                                "type": "field",
                                "required": true,
                                "read_only": false,
                                "label": "Answer"
                            }
                        }
                    }
                }
            }
        }
    }
}
```

**Example Request** :

```shell
$ curl -X POST "http://localhost:8000/api/lessons/1/take/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "taken_questions": [ { "question": 1, "taken_answers": [ { "answer": 2 } ] }, { "question": 2, "taken_answers": [ { "answer": 4 } ] }, { "question": 3, "taken_answers": [ { "answer": 6 } ] }, { "question": 4, "taken_answers": [ { "answer": 11 }, { "answer": 12 } ] }, { "question": 5, "taken_answers": [ { "answer": 16 } ] } ] }'
```

**Example Response** :

```json
HTTP 200 OK

{
    "lesson_approved": true,
    "course_approved": true
}
```

---