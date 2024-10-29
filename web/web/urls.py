from django.urls import path
from app.views.views import AlumniListView

urlpatterns = [
    path('api/alumni/', AlumniListView.as_view(), name='alumni-list'),
]
