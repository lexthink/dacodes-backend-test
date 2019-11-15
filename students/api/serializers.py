from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from drf_writable_nested import WritableNestedModelSerializer
from elearning.models import Question
from rest_framework import serializers
from .. import models


class TakenAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TakenAnswer
        fields = ('pk', 'answer',)


class TakenQuestionSerializer(WritableNestedModelSerializer):
    taken_answers = TakenAnswerSerializer(many=True)

    def validate(self, attrs):
        question = attrs['question']
        taken_answers = attrs['taken_answers']

        if len(taken_answers) == 0:
            raise ValidationError(_('You must choose at least one answer.'))

        if not question.allow_multiple_answers and len(taken_answers) > 1:
            raise ValidationError(_('You must choose only one answer.'))

        return attrs

    class Meta:
        model = models.TakenQuestion
        fields = ('pk', 'question', 'taken_answers',)


class TakenLessonSerializer(WritableNestedModelSerializer):
    taken_questions = TakenQuestionSerializer(many=True)
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    def validate(self, attrs):
        lesson = attrs['lesson']
        taken_questions = attrs['taken_questions']
        taken_questions = [taken_question['question'].pk for taken_question in taken_questions]

        if Question.objects.filter(lesson=lesson).exclude(pk__in=taken_questions).exists():
            raise ValidationError(_('All questions for a lesson are mandatory.'))

        return attrs

    class Meta:
        model = models.TakenLesson
        fields = ('pk', 'user', 'lesson', 'taken_questions',)
