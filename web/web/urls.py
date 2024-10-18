from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
  path('university/', include("app.urls")),
    path('accounts/', include("app.urls")),
  path("app/", include("app.urls"))]
