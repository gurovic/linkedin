from django.urls import path
from .views.view_request import request_view
from .views.create_request_form import create_request

urlpatterns = [
    path('request/', request_view, name='request'),
    path('request_form/', create_request, name='request_form'),
]