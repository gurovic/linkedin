from django.urls import path


from .views.event_list import event_list

urlpatterns = [
    path('', event_list, name='index'),
]
