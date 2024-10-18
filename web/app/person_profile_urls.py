# users/person_profile_urls.py
from django.urls import path
from .views import person_profile_views

urlpatterns = [
    path('profile/<int:user_id>/', person_profile_views.user_profile_view, name='user_profile'),
]
