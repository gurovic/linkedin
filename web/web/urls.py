from django.contrib import admin
from django.urls import path
from ..app.views import view_request
from ..app.forms import new_request_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('request/', view_request, name='request'),
    path('request_form/', new_request_form, name='request_form'),
]
