from django.contrib import admin
from . import models


@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


class LessonInline(admin.TabularInline):
    model = models.Lesson
    extra = 0


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'subject']
    search_fields = ['title', 'overview']
    inlines = [LessonInline]


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'course']
    search_fields = ['title', 'description']
    list_filter = ['course']


class AnswerInline(admin.TabularInline):
    model = models.Answer
    extra = 1


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('content', 'lesson', )
    list_filter = ('lesson',)
    search_fields = ('content', 'explanation')
    inlines = [AnswerInline]