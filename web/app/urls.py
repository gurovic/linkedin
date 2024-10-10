from django.urls import path

from .views import index

urlpatterns = [
    path("", index.index, name="index"),
    path("<str:company>/", index.index, name="index")
]