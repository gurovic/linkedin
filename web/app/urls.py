from django.urls import path

from .views import sign_up
from .views.create_request_form import create_request
from .views.view_request import request_view

urlpatterns = [
    path('sign_up', sign_up.sign_up, name='sign_up'),
    path('request/', request_view, name='request'),
    path('request_form/', create_request, name='request_form'),
]
