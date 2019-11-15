from rest_framework import serializers
from .. import models


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = ('id', 'title',)


class CourseSerializer(serializers.ModelSerializer):
    is_accessible = serializers.SerializerMethodField()

    def get_is_accessible(self, obj):
        user = self.context.get('request').user
        return user.can_access_to_course(obj)

    class Meta:
        model = models.Course
        fields = ('id', 'subject', 'order', 'title', 'overview', 'is_accessible',)


class LessonSerializer(serializers.ModelSerializer):
    is_accessible = serializers.SerializerMethodField()

    def get_is_accessible(self, obj):
        user = self.context.get('request').user
        return user.can_access_to_lesson(obj)

    class Meta:
        model = models.Lesson
        fields = ('id', 'course', 'order', 'title', 'description', 'question_order', 'pass_score', 'is_accessible',)


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        fields = ('id', 'question', 'content', 'correct',)


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True, source='get_answers')

    class Meta:
        model = models.Question
        fields = ('id', 'lesson', 'content', 'explanation', 'answer_order', 'score', 'answers',)
