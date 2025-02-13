from django.urls import path
from knox import views as knox_views

from app.views.account import editable_account_view, uneditable_account_view
from app.views.api_auth_check import AuthCheckView
from app.views.company_list import company_list
from app.views.create_request_form import create_request
from app.views.create_school_form import create_school
from app.views.create_student_school_form import create_or_edit_student_school
from app.views.displaying_universities import student_universities
from app.views.event import EventParticipantsView, EventView
from app.views.event_creation import event_creation
from app.views.event_list import event_list_old
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
from app.views.userskill import (
    SkillEndorsementView,
    UserSkillDeleteView,
    UserSkillView,
)
from app.views.view_request import request_view
from app.views.view_skills import add_skill_to_user, skills_view
from .views.company_api import CompanyView
from .views.search import user_search
from .views.filters import search_by_skills
from .views.angular_uneditable_account_api import user_detail_api_view
from app.views.api_login import LoginView
from app.views.event_list_api import EventListAPIView
from app.views.api_ans_verification import AnsVerificationView
from app.views.search_api import UserSearchAPIView
from app.views.universitystudent_api import (
    CurrentUniversityStudentView,
    UniversityStudentView,
)

urlpatterns = [
    path("student_schools/", student_schools, name="student_schools"),
    path("companies/", company_list, name="company_list"),
    path("skills/<int:user_id>/", skills_view, name="user_skills_old"),
    path("skills/add/", add_skill_to_user, name="add_skills"),
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
    path("events/", event_list_old, name="event_list_old"),
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
    path(r"api/auth/login/", LoginView.as_view(), name='knox_login'),
    path(r"api/auth/logout/", knox_views.LogoutView.as_view(), name='knox_logout'),
    path(r"api/auth/logoutall/", knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path("api/event/", EventView.as_view(), name="events"),
    path(
        "api/event/<int:event_id>/",
        EventView.as_view(),
        name="event_detail",
    ),
    path(
        "api/event/<int:event_id>/participants/",
        EventParticipantsView.as_view(),
        name="event_participants",
    ),
    path("api/universities/", university_list, name="university_list"),
    path(
        "api/user/<int:user_id>/",
        UserDetailView.as_view(),
        name="user-detail",
    ),
    path(
        "api/user/<int:user_id>/skills/",
        UserSkillView.as_view(),
        name="user-skills",
    ),
    path(
        "api/user/<int:user_id>/skill/<int:skill_id>/",
        UserSkillDeleteView.as_view(),
        name="user-skill",
    ),
    path(
        "api/user/<int:user_id>/skill/<int:skill_id>/endorsement/",
        SkillEndorsementView.as_view(),
        name="skill-endorsement",
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
    path('search/search_by_skills', search_by_skills, name='search_by_skills'),
    path('angular/account/<int:user_id>/', user_detail_api_view, name='angular_uneditable_account_api'),
    path('api/event_list', EventListAPIView.as_view(), name ='events_list_api'),
    path('api/ans_verif/<int:request_id>', AnsVerificationView.as_view(), name="ans_verify"),
    path("api/user_search/", UserSearchAPIView.as_view(), name="user_search_api"),
    path("api/company/", CompanyView.as_view(), name="company"),
    path("api/company/<int:company_id>/", CompanyView.as_view(), name="company"),
    path(
        "api/universitystudent/",
         UniversityStudentView.as_view(),
         name="universitystudent",
    ),
    path(
        "api/universitystudent/current/",
        CurrentUniversityStudentView.as_view(),
        name="current_universitystudent",
    ),
]
