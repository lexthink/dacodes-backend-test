# CHANGELOG

## 1.0.0 Initial release

- [x] We have courses that contain lessons and lessons that contain questions
- [x] The courses are correlative with previous ones
- [x] The lessons are correlative with previous ones
- [x] The questions for each lesson have no correlation
- [x] All questions for a lesson are mandatory
- [x] Each question has a score
- [x] Each lesson has an approval score that has to be met by the sum of correctly answered questions to approve it
- [x] A course is approved when all lessons are passed.
- [x] There’s no restriction on accessing approved courses
- [x] Only professors can create and manage courses, lessons and questions
- [x] Any student can take a course
- [x] Initially, we’ll need to support these types of questions:
    - [x] Boolean
    - [x] Multiple choice where only one answer is correct
    - [x] Multiple choice where more than one answer is correct
    - [x] Multiple choice where more than one answer is correct and all of them must be answered correctly
- [x] Frontend guys specifically asked for these endpoints for the students to use:
    - [x] Get a list of all courses, telling which ones the student can access
    - [x] Get lessons for a course, telling which ones the student can access
    - [x] Get lesson details for answering its questions
    - [x] Take a lesson (to avoid several requests, they asked to send all answers in one go)
    - [x] Basic CRUD for courses, lessons and questions