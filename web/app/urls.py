from django.urls import path
from .views.company_list import company_list
urlpatterns= [
    path("companies/", company_list)
]