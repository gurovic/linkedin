from django.urls import path


from .views.recommendations import recommendations

urlpatterns = [
    path('', recommendations, name='index'),
]