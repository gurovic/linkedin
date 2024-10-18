# users/person_profile_views.py
from django.shortcuts import render, get_object_or_404
from ..models import UserProfile

def user_profile_view(request, user_id):
    user_profile = get_object_or_404(UserProfile, id=user_id)
    context = {
        'user_profile': user_profile
    }
    return render(request, 'user_profile.html', context)
