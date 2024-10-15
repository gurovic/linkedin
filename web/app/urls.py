from django.urls import path

from app.views.event_creation import event_creation
from app.views.event_list import event_list
from app.views.friends_in_university import friends_in_university

urlpatterns = [
    path("events/", event_list, name="index"),
    path("events/new/", event_creation, name="event_creation"),
    path("friends", friends_in_university.get_friends, name="friends in university"),
]
