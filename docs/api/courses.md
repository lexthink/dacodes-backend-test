# Resource: courses

## Courses

---

**URL** : `http://localhost:8000/api/courses/`

**Method** : `GET`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X GET "http://localhost:8000/api/courses/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 200 OK

[
    {
        "id": 1,
        "subject": 1,
        "order": 0,
        "title": "Python Basics",
        "overview": "This course introduces the basics of Python 3, including conditional execution and iteration as control structures, and strings and lists as data structures. You'll program an on-screen Turtle to draw pretty pictures. You'll also learn to draw reference diagrams as a way to reason about program executions, which will help to build up your debugging skills. The course has no prerequisites. It will cover Chapters 1-9 of the textbook \"Fundamentals of Python Programming,\" which is the accompanying text (optional and free) for this course.\r\n\r\nThe course is for you if you're a newcomer to Python programming, if you need a refresher on Python basics, or if you may have had some exposure to Python programming but want a more in-depth exposition and vocabulary for describing and reasoning about programs.\r\n\r\nThis is the first of five courses in the Python 3 Programming Specialization.",
        "is_accessible": true
    },
    {
        "id": 2,
        "subject": 1,
        "order": 1,
        "title": "Python Functions, Files, and Dictionaries",
        "overview": "This course introduces the dictionary data structure and user-defined functions. You’ll learn about local and global variables, optional and keyword parameter-passing, named functions and lambda expressions. You’ll also learn about Python’s sorted function and how to control the order in which it sorts by passing in another function as an input. For your final project, you’ll read in simulated social media data from a file, compute sentiment scores, and write out .csv files. It covers chapters 10-16 of the textbook “Fundamentals of Python Programming,” which is the accompanying text (optional and free) for this course.\r\n\r\nThe course is well-suited for you if you have already taken the \"Python Basics\" course and want to gain further fundamental knowledge of the Python language. Together, both courses are geared towards newcomers to Python programming, those who need a refresher on Python basics, or those who may have had some exposure to Python programming but want a more in-depth exposition and vocabulary for describing and reasoning about programs.\r\n\r\nThis is a follow-up to the \"Python Basics\" course (course 1 of the Python 3 Programming Specialization), and it is the second of five courses in the specialization.",
        "is_accessible": true
    },
    ...
]
```

---

**URL** : `http://localhost:8000/api/courses/`

**Method** : `POST`

**Authentication Pequired** : Yes

**Request Parameters**

```json
{
    "subject": {
        "type": "field",
        "required": true,
        "read_only": false,
        "label": "Subject"
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
    "overview": {
        "type": "string",
        "required": false,
        "read_only": false,
        "label": "Overview",
        "help_text": "a overview of the course"
    }
}
```

**Example Request** :

```shell
$ curl -X POST "http://localhost:8000/api/courses/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "subject": 1, "order": 0, "title": "Python Basics", ... }'
```

**Example Response** :

```json
HTTP 201 Created

{
    "id": 1,
    "subject": 1,
    "order": 0,
    "title": "Python Basics",
    "overview": "This course introduces the basics of Python 3, including conditional execution and iteration as control structures, and strings and lists as data structures. You'll program an on-screen Turtle to draw pretty pictures. You'll also learn to draw reference diagrams as a way to reason about program executions, which will help to build up your debugging skills. The course has no prerequisites. It will cover Chapters 1-9 of the textbook \"Fundamentals of Python Programming,\" which is the accompanying text (optional and free) for this course.\r\n\r\nThe course is for you if you're a newcomer to Python programming, if you need a refresher on Python basics, or if you may have had some exposure to Python programming but want a more in-depth exposition and vocabulary for describing and reasoning about programs.\r\n\r\nThis is the first of five courses in the Python 3 Programming Specialization.",
    "is_accessible": true
}
```

---

**URL** : `http://localhost:8000/api/courses/{id}/`

**Method** : `GET`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X GET "http://localhost:8000/api/courses/1/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 200 OK

{
    "id": 1,
    "subject": 1,
    "order": 0,
    "title": "Python Basics",
    "overview": "This course introduces the basics of Python 3, including conditional execution and iteration as control structures, and strings and lists as data structures. You'll program an on-screen Turtle to draw pretty pictures. You'll also learn to draw reference diagrams as a way to reason about program executions, which will help to build up your debugging skills. The course has no prerequisites. It will cover Chapters 1-9 of the textbook \"Fundamentals of Python Programming,\" which is the accompanying text (optional and free) for this course.\r\n\r\nThe course is for you if you're a newcomer to Python programming, if you need a refresher on Python basics, or if you may have had some exposure to Python programming but want a more in-depth exposition and vocabulary for describing and reasoning about programs.\r\n\r\nThis is the first of five courses in the Python 3 Programming Specialization.",
    "is_accessible": true
}
```

---

**URL** : `http://localhost:8000/api/courses/{id}/`

**Method** : `PUT`

**Authentication Pequired** : Yes

**Request Parameters** :

```json
{
    "subject": {
        "type": "field",
        "required": true,
        "read_only": false,
        "label": "Subject"
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
    "overview": {
        "type": "string",
        "required": false,
        "read_only": false,
        "label": "Overview",
        "help_text": "a overview of the course"
    }
}
```

**Example Request** :

```shell
$ curl -X PUT "http://localhost:8000/api/courses/1/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "subject": 1, "order": 0, "title": "Python Basics", ... }'
```

**Example Response** :

```json
HTTP 200 OK

{
    "id": 1,
    "subject": 1,
    "order": 0,
    "title": "Python Basics",
    "overview": "This course introduces the basics of Python 3, including conditional execution and iteration as control structures, and strings and lists as data structures. You'll program an on-screen Turtle to draw pretty pictures. You'll also learn to draw reference diagrams as a way to reason about program executions, which will help to build up your debugging skills. The course has no prerequisites. It will cover Chapters 1-9 of the textbook \"Fundamentals of Python Programming,\" which is the accompanying text (optional and free) for this course.\r\n\r\nThe course is for you if you're a newcomer to Python programming, if you need a refresher on Python basics, or if you may have had some exposure to Python programming but want a more in-depth exposition and vocabulary for describing and reasoning about programs.\r\n\r\nThis is the first of five courses in the Python 3 Programming Specialization.",
    "is_accessible": true
}
```

---

**URL** : `http://localhost:8000/api/courses/{id}/`

**Method** : `PATCH`

**Authentication Pequired** : Yes

**Request Parameters** :

```json
{
    "subject": {
        "type": "field",
        "required": true,
        "read_only": false,
        "label": "Subject"
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
    "overview": {
        "type": "string",
        "required": false,
        "read_only": false,
        "label": "Overview",
        "help_text": "a overview of the course"
    }
}
```

**Example Request** :

```shell
$ curl -X PATCH "http://localhost:8000/api/courses/1/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "subject": 1, "order": 0, "title": "Python Basics", ... }'
```

**Example Response** :

```json
HTTP 200 OK

{
    "id": 1,
    "subject": 1,
    "order": 0,
    "title": "Python Basics",
    "overview": "This course introduces the basics of Python 3, including conditional execution and iteration as control structures, and strings and lists as data structures. You'll program an on-screen Turtle to draw pretty pictures. You'll also learn to draw reference diagrams as a way to reason about program executions, which will help to build up your debugging skills. The course has no prerequisites. It will cover Chapters 1-9 of the textbook \"Fundamentals of Python Programming,\" which is the accompanying text (optional and free) for this course.\r\n\r\nThe course is for you if you're a newcomer to Python programming, if you need a refresher on Python basics, or if you may have had some exposure to Python programming but want a more in-depth exposition and vocabulary for describing and reasoning about programs.\r\n\r\nThis is the first of five courses in the Python 3 Programming Specialization.",
    "is_accessible": true
}
```

---

**URL** : `http://localhost:8000/api/courses/{id}/`

**Method** : `DELETE`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X DELETE "http://localhost:8000/api/courses/1/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 204 No Content
```

---

**URL** : `http://localhost:8000/api/courses/{id}/lessons/`

**Method** : `GET`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X GET "http://localhost:8000/api/courses/1/lessons/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
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
    ...
]
```

---

**URL** : `http://localhost:8000/api/courses/{id}/enroll/`

**Method** : `POST`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X POST "http://localhost:8000/api/courses/1/enroll/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 200 OK

{
    "enrolled": true
}
```

---