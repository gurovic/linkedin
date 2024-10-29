"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.views import view_tags

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/<int:user_id>/', view_tags.profile_view, name='user_profile'),
    path('tags/add/', view_tags.add_tag, name='add_tag'),
    path('tags/<int:tag_id>/delete/', view_tags.delete_tag, name='delete_tag'),
    path('verify-skill/<int:tag_id>/', view_tags.verify_skill, name='verify_skill'),
]
