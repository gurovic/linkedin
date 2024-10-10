from django.urls import path


from .views.recommendations import recommendations, recommendations_form

urlpatterns = [
    path('', recommendations, name='index'),
    path('form', recommendations_form, name='index'),
]