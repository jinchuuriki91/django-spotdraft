from django.urls import path
from core import views

urlpatterns = [
    path('v1/student', views.StudentView.as_view()),
    path('v1/student/<int:student_id>', views.StudentView.as_view()),
    path('v1/course', views.CourseView.as_view()),
    path('v1/course/<int:course_id>', views.CourseView.as_view()),
    path(
        'v1/student/<int:student_id>/course/<int:course_id>',
        views.subscribe_student_course),
    path(
        'v1/student/<int:student_id>/course/<int:course_id>/feedback',
        views.course_feedback)
]
