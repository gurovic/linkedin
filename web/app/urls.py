from django.urls import path

from app.views.event_creation import event_creation
from app.views.event_list import event_list

urlpatterns = [
    path("", event_list, name="index"),
    path("new/", event_creation, name="event_creation"),
]
