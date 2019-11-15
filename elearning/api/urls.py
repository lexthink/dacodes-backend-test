from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('subjects', views.SubjectViewSet)
router.register('courses', views.CourseViewSet)
router.register('lessons', views.LessonViewSet)
router.register('questions', views.QuestionViewSet)
router.register('answers', views.AnswerViewSet)

app_name = 'elearning'
urlpatterns = [
    path('', include(router.urls)),
]
