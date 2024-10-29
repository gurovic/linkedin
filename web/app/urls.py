from django.urls import path


from .views.view_tags import tags_view, add_tag_to_user

urlpatterns = [
    path('tags/<int:user_id>/', tags_view, name = 'user_profile'),
    path('add_tag/<int:user_id>/', add_tag_to_user, name = 'adding_tags'),
]