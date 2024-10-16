from django.urls import path
from .views.view_request import request_view
from .forms.new_request_form import RequestForm

urlpatterns = [
    path('request/', request_view, name='request'),
    path('request_form/', RequestForm, name='request_form'),
]