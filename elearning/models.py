from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from positions.fields import PositionField


ORDER_OPTIONS = (
    ('content', _('Content')),
    ('random', _('Random')),
    ('none', _('None'))
)

class Subject(models.Model):
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=100, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Course(models.Model):
    subject = models.ForeignKey(
        Subject, related_name='courses',
        verbose_name=_("Subject"), on_delete=models.CASCADE)

    order = PositionField(collection='subject')

    title = models.CharField(
        verbose_name=_("Title"),
        max_length=100, blank=False)

    overview = models.TextField(
        verbose_name=_("Overview"),
        blank=True, help_text=_("a overview of the course"))

    def __str__(self):
        return '{}. {}'.format(self.order, self.title)

    def get_previous(self):
        if self.order == 0:
            return None
        return Course.objects.get(subject=self.subject, order=self.order - 1)

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")
        ordering = ['subject', 'order']


class Lesson(models.Model):
    course = models.ForeignKey(
        Course, related_name='lessons',
        verbose_name=_("Course"), on_delete=models.CASCADE)

    order = PositionField(collection='course')

    title = models.CharField(
        verbose_name=_("Title"),
        max_length=100, blank=False)

    description = models.TextField(
        verbose_name=_("Description"),
        blank=True, help_text=_("a description of the lesson"))

    question_order = models.CharField(
        max_length=30, null=True, blank=True,
        choices=ORDER_OPTIONS,
        help_text=_("The order in which the questions"
                    "are displayed to the user"),
        verbose_name=_("Question Order"))

    pass_score = models.PositiveSmallIntegerField(
        blank=True, default=0,
        verbose_name=_("Pass score"),
        help_text=_("Score required to pass lesson."))

    # success_text = models.TextField(
    #     blank=True, help_text=_("Displayed if user passes."),
    #     verbose_name=_("Success Text"))

    # fail_text = models.TextField(
    #     verbose_name=_("Fail Text"),
    #     blank=True, help_text=_("Displayed if user fails."))

    def __str__(self):
        return '{}. {}'.format(self.order, self.title)

    def order_questions(self, queryset):
        if self.question_order == 'content':
            return queryset.order_by('content')
        if self.question_order == 'random':
            return queryset.order_by('?')
        if self.question_order == 'none':
            return queryset.order_by()
        return queryset

    def get_questions(self):
        return self.order_questions(Question.objects.filter(lesson=self))

    def get_previous(self):
        if self.order == 0:
            return None
        return Lesson.objects.get(course=self.subject, order=self.order - 1)

    class Meta:
        verbose_name = _("Lesson")
        verbose_name_plural = _("Lessons")
        ordering = ['course__order', 'order']


class Question(models.Model):
    lesson = models.ForeignKey(
        Lesson, related_name='questions',
        verbose_name=_("Lesson"), on_delete=models.CASCADE)

    content = models.CharField(max_length=1000,
                               blank=False,
                               help_text=_("Enter the question text that "
                                           "you want displayed"),
                               verbose_name=_('Question'))

    explanation = models.TextField(max_length=2000,
                                   blank=True,
                                   help_text=_("Explanation to be shown "
                                               "after the question has "
                                               "been answered."),
                                   verbose_name=_('Explanation'))

    answer_order = models.CharField(
        max_length=30, null=True, blank=True,
        choices=ORDER_OPTIONS,
        help_text=_("The order in which the posible "
                    "answers are displayed to the user"),
        verbose_name=_("Answer Order"))

    allow_multiple_answers = models.BooleanField(
        blank=True, default=False,
        help_text=_("Allow to choose multiple answers"),
        verbose_name=_("Allow Multiple Answer"))

    match_all_answers = models.BooleanField(
        blank=True, default=False,
        help_text=_("All answers must be correct"),
        verbose_name=_("Match All Answers"))

    score = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        self.allow_multiple_answers = self.match_all_answers
        super(Question, self).save(*args, **kwargs)

    def check_if_correct(self, guesses):
        for guess in guesses:
            answer = Answer.objects.get(pk=guess)
            if not answer.correct:
                print(guess)
                return False
        if self.match_all_answers and Answer.objects.filter(question=self, correct=True).exclude(pk__in=guesses).exists():
            return False
        return True

    def order_answers(self, queryset):
        if self.answer_order == 'content':
            return queryset.order_by('content')
        if self.answer_order == 'random':
            return queryset.order_by('?')
        if self.answer_order == 'none':
            return queryset.order_by()
        return queryset

    def get_answers(self):
        return self.order_answers(Answer.objects.filter(question=self))

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")


class Answer(models.Model):
    question = models.ForeignKey(Question, verbose_name=_("Question"), on_delete=models.CASCADE)

    content = models.CharField(max_length=1000,
                               blank=False,
                               help_text=_("Enter the answer text that "
                                           "you want displayed"),
                               verbose_name=_("Content"))

    correct = models.BooleanField(blank=False,
                                  default=False,
                                  help_text=_("Is this a correct answer?"),
                                  verbose_name=_("Correct"))

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
