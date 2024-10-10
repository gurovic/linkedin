from django.urls import path
from .views.student_schools import student_schools

urlpatterns = [
    path("user/<int:user_id>/schools/", student_schools),
]