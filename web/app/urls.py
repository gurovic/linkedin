from django.urls import path
from .views.view_request import request_view
from .views.create_request_form import create_request
from .views.student_schools import student_schools
from .views.create_school_form import create_school

urlpatterns = [
    path("user/schools/", student_schools, name='student_schools'),
    path('request/', request_view, name='request'),
    path('request_form/', create_request, name='request_form'),
    path('school_form/', create_school, name='school_form'),
]