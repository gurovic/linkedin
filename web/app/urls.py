from django.urls import path
from .views import request_view
from .views import create_request

urlpatterns = [
    path('request/', request_view, name='request'),
    path('request_form/', create_request, name='request_form'),
]