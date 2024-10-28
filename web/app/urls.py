from django.urls import path


from .views.view_tags import tags_view, add_tag_to_user

urlpatterns = [
    path('<int:user_id>/', tags_view, name = 'user_profile'),
    path('<int:user_id>/add_tag/', add_tag_to_user, name = 'adding_tags'),
]