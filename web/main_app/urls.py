from django.urls import path
from .views import home, registration

urlpatterns = [
    path('', home, name='home'),
    path('registration/', registration, name='registration')
]
