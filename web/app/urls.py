from django.urls import path
from .views.company_list import company_list
from .views.view_request import request_view
from .views.create_request_form import create_request
from .views.displaying_universities import student_universities
from .views.universityview import edit_university_student

urlpatterns = [
    path("companies/", company_list, name='company_list'),
    path('request/', request_view, name='request'),
    path('request_form/', create_request, name='request_form'),
    path('student/<int:student_id>/universities/', student_universities, name='student_universities'),
    path('university_student/<int:pk>/edit/', edit_university_student, name='edit_university_student'),
]