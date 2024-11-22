from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app.views.view_api import AlumniListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("app/", include("app.urls")),
    path('', include('app.urls')),
    path('api/alumni/', AlumniListView.as_view(), name='alumni-list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

