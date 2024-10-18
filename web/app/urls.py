from django.urls import path


from .views.view_tags import tags_view

urlpatterns = [
    path('<int:user_id>/', tags_view, name = 'user_profile'),
]