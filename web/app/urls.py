from django.urls import path

from .views import sign_up
from .views.create_request_form import create_request
from .views.view_tags import tags_view, add_tag_to_user
from .views.view_request import request_view

urlpatterns = [
    path('sign_up', sign_up.sign_up, name='sign_up'),
    path('tags/<int:user_id>/', tags_view, name = 'user_profile'),
    path('add_tag/<int:user_id>/', add_tag_to_user, name = 'adding_tags'),
    path('request/', request_view, name='request'),
    path('request_form/', create_request, name='request_form'),
]
