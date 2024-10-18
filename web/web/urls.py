from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', include("app.urls")),
=======
    path("app/", include("app.urls"))
>>>>>>> remotes/origin/request
]
