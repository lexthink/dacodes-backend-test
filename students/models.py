from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from elearning.models import Course, Lesson, Question, Answer


class User(AbstractUser):
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)

    courses = models.ManyToManyField(
        Course, through='EnrolledCourse', related_name='students',
        verbose_name=_("Courses"), blank=True)

    def save(self, *args, **kwargs):
        self.is_student = not self.is_teacher
        super(User, self).save(*args, **kwargs)

    def can_enroll_to_course(self, course):
        if self.is_teacher or self.is_enrolled_to_course(course):
            return False

        if course.order == 0  \
           or self.has_approved_course(course.get_previous()):
            return True

        return False

    def is_enrolled_to_course(self, course):
        return self.courses.filter(id=course.id).exists()

    def has_approved_course(self, course):
        return EnrolledCourse.objects.filter(user=self, course=course, is_approved=True).exists()

    def can_access_to_course(self, course):
        if self.is_teacher \
           or self.has_approved_course(course) \
           or self.is_enrolled_to_course(course):
            return True

        return False

    def has_approved_lesson(self, lesson):
        return TakenLesson.objects.filter(user=self, lesson=lesson, is_approved=True).exists()

    def can_access_to_lesson(self, lesson):
        if self.is_teacher \
           or self.has_approved_lesson(lesson):
            return True

        return False

    def can_take_lesson(self, lesson):
        if not self.can_access_to_course(lesson.course):
            return False

        if self.has_approved_course(lesson.course):
            return False

        if self.has_approved_lesson(lesson):
            return False

        if lesson.order == 0  \
           or self.has_approved_lesson(lesson.get_previous()):
            return True

        return False


class EnrolledCourse(models.Model):
    user = models.ForeignKey(
        User, related_name='+',
        verbose_name=_("User"), on_delete=models.CASCADE)

    course = models.ForeignKey(
        Course, related_name='+',
        verbose_name=_("Course"), on_delete=models.CASCADE)

    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}'.format(self.user, self.course)

    def check_if_passed(self):
        self.is_approved = True

        for lesson in Lesson.objects.filter(course=self.course):
            if not self.user.has_approved_lesson(lesson):
                self.is_approved = False
                break

        self.save()
        return self.is_approved

    class Meta:
        unique_together = (('user','course'),)


class TakenLesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='taken_lessons')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='taken_lessons')
    score = models.PositiveSmallIntegerField(default=0)
    is_approved = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {} : {}'.format(self.user, self.lesson, self.score)

    def check_if_passed(self):
        self.score = 0
        self.is_approved = False

        for question in self.taken_questions.all():
            if question.check_if_passed():
                self.score += question.score
                self.save()

        if self.score >= self.lesson.pass_score:
            self.is_approved = True

        self.save()

        return self.is_approved


class TakenQuestion(models.Model):
    lesson = models.ForeignKey(TakenLesson, on_delete=models.CASCADE, related_name='taken_questions')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='+')
    is_correct = models.BooleanField(default=False)
    score = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return '{} : {}'.format(self.lesson, self.question)

    def check_if_passed(self):
        self.score = 0
        self.is_correct = False

        if self.question.check_if_correct(self.get_answers_as_list()):
            self.is_correct = True
            self.score = self.question.score
            self.save()

        return self.is_correct

    def get_answers_as_list(self):
        return [taken_answer.answer.pk for taken_answer in self.taken_answers.all()]


class TakenAnswer(models.Model):
    question = models.ForeignKey(TakenQuestion, on_delete=models.CASCADE, related_name='taken_answers')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return '{} : {}'.format(self.question, self.answer)
