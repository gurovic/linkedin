from django.urls import path

from .views.company_list import company_list
from .views.create_request_form import create_request
from .views.create_school_form import create_school
from .views.create_student_school_form import create_student_school
from .views.displaying_universities import student_universities
from .views.event_list import event_list
from .views.home import home
from .views.index import index
from .views.job_experience import job_experience_view
from .views.login import user_login
from .views.logout import logout_request
from .views.registration import registration
from .views.student_schools import student_schools
from .views.university_api_view import university_list
from .views.universityview import edit_university_student
from .views.user_api_view import UserDetailView
from .views.view_request import request_view
from .views.view_tags import tags_view, add_tag_to_user

urlpatterns = [
    path("student_schools/", student_schools, name='student_schools'),
    path("companies/", company_list, name='company_list'),
    path('tags/<int:user_id>/', tags_view, name='user_profile'),
    path('add_tag/<int:user_id>/', add_tag_to_user, name='adding_tags'),
    path('request/', request_view, name='request'),
    path('request_form/', create_request, name='request_form'),
    path('student/<int:student>/universities/', student_universities, name='student_universities'),
    path('university_student/<int:pk>/edit/', edit_university_student, name='edit_university_student'),
    path('school_form/', create_school, name='school_form'),
    path('event_list/', event_list, name='event_list'),
    path('job_experience/', job_experience_view, name='job_experience'),
    path('', home, name='home'),
    path('registration/', registration, name='registration'),
    path('login/', user_login, name='login'),
    path('logout/', logout_request, name='logout'),
    path('student_school_form/', create_student_school, name='student_school_form'),
    path('index/', index, name='index'),
    path('api/universities/', university_list, name='university_list'),
    path('api/user/<int:user_id>/', UserDetailView.as_view(), name='user-detail'),
]
