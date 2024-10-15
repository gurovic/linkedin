from django.contrib import admin
from django.urls import path
from .views import view_request
from .forms import new_request_form

urlpatterns = [
    path('request/', view_request, name='request'),
    path('request_form/', new_request_form, name='request_form'),
]