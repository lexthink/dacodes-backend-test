from django.contrib import admin
from django.contrib.auth.models import Group
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name']
    list_filter = ['is_teacher', 'is_student', 'is_staff']


admin.site.unregister(Group)
# admin.site.register(models.TakenLesson)
# admin.site.register(models.TakenQuestion)
# admin.site.register(models.TakenAnswer)
