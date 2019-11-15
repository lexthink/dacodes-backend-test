from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from students.api.serializers import TakenLessonSerializer
from students.models import EnrolledCourse, TakenLesson, TakenQuestion, TakenAnswer
from . import serializers, permissions
from .. import models


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer
    permission_classes = (IsAuthenticated, permissions.IsTeacherOrReadOnly,)

    @action(detail=True)
    def courses(self, request, pk):
        course = self.get_object()
        serializer = serializers.CourseSerializer(course.courses, many=True, context={'request': request})
        return Response(serializer.data)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = (IsAuthenticated, permissions.IsTeacherOrReadOnly,)

    @action(detail=True)
    def lessons(self, request, pk):
        course = self.get_object()
        serializer = serializers.LessonSerializer(course.lessons, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, permissions.CannEnrollToCourse])
    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled': True})


class LessonViewSet(viewsets.ModelViewSet):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer
    permission_classes = (IsAuthenticated, permissions.IsTeacherOrReadOnly,)

    @action(detail=True)
    def questions(self, request, pk):
        lesson = self.get_object()
        serializer = serializers.QuestionSerializer(lesson.get_questions(), many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, permissions.CanTakeLesson])
    def take(self, request, pk=None):
        lesson = self.get_object()
        request.data['lesson'] = lesson.id
        serializer = TakenLessonSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        taken_lesson = serializer.save()
        lesson_approved = taken_lesson.check_if_passed()
        course_approved = False
        if lesson_approved:
            course = taken_lesson.lesson.course
            user = taken_lesson.user
            enrolled_course = EnrolledCourse.objects.get(course=course, user=user)
            course_approved = enrolled_course.check_if_passed()
        return Response({'lesson_approved': lesson_approved, 'course_approved':course_approved})


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = (IsAuthenticated, permissions.IsTeacherOrReadOnly,)


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = models.Answer.objects.all()
    serializer_class = serializers.AnswerSerializer
    permission_classes = (IsAuthenticated, permissions.IsTeacherOrReadOnly,)
