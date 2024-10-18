from django.urls import path

from .views import friends_in_university, sign_up
from .views.view_request import request_view
from .views.create_request_form import create_request
urlpatterns = [
    path("friends", friends_in_university.get_friends, name="friends in university"),
    path('sign_up', sign_up.sign_up, name='sign_up'), 
  path('request/', request_view, name='request'),
    path('request_form/', create_request, name='request_form'),
]
