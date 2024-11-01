from django.urls import path
from .views.company_list import company_list
from .views.view_request import request_view
from .views.create_request_form import create_request
from .views.student_schools import student_schools
from .views.create_school_form import create_school
from .views.view_tags import tags_view, add_tag_to_user
from .views.job_experience import job_experience_view

urlpatterns = [
    path("user/schools/", student_schools, name='student_schools'),
    path('tags/<int:user_id>/', tags_view, name = 'user_profile'),
    path('add_tag/<int:user_id>/', add_tag_to_user, name = 'adding_tags'),
    path('request/', request_view, name='request'),
    path('request_form/', create_request, name='request_form'),
    path('school_form/', create_school, name='school_form'),
    path("companies/", company_list, name='company_list'),
    path('tags/<int:user_id>/', tags_view, name='user_profile'),
    path('add_tag/<int:user_id>/', add_tag_to_user, name='adding_tags'),
    path('request/', request_view, name='request'),
    path('request_form/', create_request, name='request_form'),
    path('job_experience/', job_experience_view, name='job_experience'),
]
