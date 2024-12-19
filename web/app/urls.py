from django.urls import path

from app.views.account import editable_account_view, uneditable_account_view
from app.views.api_auth_check import AuthCheckView
from app.views.company_list import company_list
from app.views.create_request_form import create_request
from app.views.create_school_form import create_school
from app.views.create_student_school_form import create_or_edit_student_school
from app.views.displaying_universities import student_universities
from app.views.event_list import event_list
from app.views.home import home
from app.views.index import index
from app.views.job_experience import job_experience_view
from app.views.login import user_login
from app.views.logout import logout_request
from app.views.password_change import change_password
from app.views.registration import registration
from app.views.student_schools import student_schools
from app.views.university_api_view import university_list
from app.views.universityview import edit_university_student
from app.views.user_api_view import UserDetailView
from app.views.view_request import request_view
from app.views.view_tags import add_tag_to_user, tags_view
from app.views.event_creation import event_creation
from .views.search import user_search

urlpatterns = [
    path("student_schools/", student_schools, name="student_schools"),
    path("companies/", company_list, name="company_list"),
    path("tags/<int:user_id>/", tags_view, name="user_profile"),
    path("add_tag/<int:user_id>/", add_tag_to_user, name="adding_tags"),
    path("request/", request_view, name="request"),
    path("request_form/", create_request, name="request_form"),
    path(
        "student/<int:student>/universities/",
        student_universities,
        name="student_universities",
    ),
    path(
        "university_student/<int:pk>/edit/",
        edit_university_student,
        name="edit_university_student",
    ),
    path("school_form/", create_school, name="school_form"),
    path("event/new/", event_creation, name="event_creation"),
    path("events/", event_list, name="event_list"),
    path("job_experience/", job_experience_view, name="job_experience"),
    path("", home, name="home"),
    path("registration/", registration, name="registration"),
    path("login/", user_login, name="login"),
    path("logout/", logout_request, name="logout"),
    path(
        "student_school_form/",
        create_or_edit_student_school,
        name="student_school_form",
    ),
    path(
        "student_school_form/<int:pk>/",
        create_or_edit_student_school,
        name="student_school_form",
    ),
    path("index/", index, name="index"),
    path("api/universities/", university_list, name="university_list"),
    path(
        "api/user/<int:user_id>/",
        UserDetailView.as_view(),
        name="user-detail",
    ),
    path(
        "account/<int:user_id>/",
        uneditable_account_view,
        name="uneditable_account",
    ),
    path(
        "account/<int:user_id>/edit/",
        editable_account_view,
        name="editable_account",
    ),
    path("change_password/", change_password, name="change_password"),
    path("api/auth/check/", AuthCheckView.as_view(), name="api_auth_check"),
    path('search/', user_search, name='user_search'),
    
]
